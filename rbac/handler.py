#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Youshumin
@Date: 2019-11-12 12:38:15
@LastEditors: Youshumin
@LastEditTime: 2019-11-12 12:39:40
@Description: 
'''
from oslo.web.requesthandler import MixinRequestHandler
from oslo.web.route import route


@route("/test")
class TestHandler(MixinRequestHandler):

    def get(self):
        self.send_ok(data=dict(ok="xx"))
        return
