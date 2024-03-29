#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Youshumin
@Date: 2019-08-21 11:13:46
@LastEditors: Youshumin
@LastEditTime: 2019-11-12 12:40:56
'''
import logging
import logging.config
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.log import enable_pretty_logging
from tornado.options import define, options

from configs.setting import COOKIE_SECRET, PROJECT_NAME, LOGFILE
debug = os.environ.get("RUN_ENV")
# PATH_APP_ROOT = os.path.abspath(
#     os.path.join(os.path.abspath(os.path.dirname(__file__))))

LOG = logging.getLogger(__name__)


class LogHandler(object):
    """设置tornado 日志信息 当设置RUN_ENV为prod的时候进行文件输出,否则控制台"""

    def __init__(self):
        if debug == "prod":
            define("log_file_prefix", default=LOGFILE)
            define("log_rotate_mode", default="time",)
            define("log_rotate_when", default="D")
            define("log_rotate_interval", default=1)
            define("log_file_num_backups", default=60)
            define("log_to_stderr", default=False)
        super(LogHandler, self).__init__()


LogHandler()


class RouteHandler(object):
    """注册路由"""

    def __init__(self):
        """
        需要配置这里实现注册路由... 
            自动注册路由的方式可以继承 application实现
            我这边是想实现像flask蓝本一样实现注册...所以暂时设置为这样
        """

        from rbac import handler

        from oslo.web.route import route
        self.route = route
        super(RouteHandler, self).__init__()


class Application(tornado.web.Application, RouteHandler):
    """初始化application"""

    def __init__(self):
        # from apps.main.main import route
        configs = dict(
            # emplate_path=os.path.join(PATH_APP_ROOT, "templates"),
            debug=options.debug,
            cookie_secret=COOKIE_SECRET,
            autoescape=None,
        )
        RouteHandler.__init__(self)
        tornado.web.Application.__init__(
            self, self.route.get_urls(), **configs)


class WebApp():
    """应用启动唯一入口"""

    def __init__(self):
        """
            初始化启动信息
                运行环境 debug
                运行ip host
                启动端口 port
        """
        if debug != "prod":
            define("debug", default=True, help="enable debug mode")
        else:
            define("debug", default=False, help="enable debug mode")
        define("host", default="0.0.0.0", help="run on this host", type=str)
        define("port", default="18080", help="run on this port", type=int)

    def run(self):
        enable_pretty_logging()
        http_server = tornado.httpserver.HTTPServer(Application(),
                                                    xheaders=True)
        if options.debug:
            logging.getLogger().setLevel(logging.DEBUG)
            http_server.listen(options.port, address=options.host)
            LOG.info("start app [%s] for %s:%s", PROJECT_NAME, options.host,
                     options.port)
        else:
            http_server.listen(options.port, address=options.host)
            LOG.info("start app [%s] for %s:%s", PROJECT_NAME, options.host,
                     options.port)
        try:
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            tornado.ioloop.IOLoop.instance().stop()

    def stop(self):
        tornado.ioloop.IOLoop.instance().stop()


def web_app():
    return WebApp()
