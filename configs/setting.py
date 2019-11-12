#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Youshumin
@Date: 2019-10-11 11:24:53
@LastEditors: Youshumin
@LastEditTime: 2019-11-12 11:29:35
@Description: 
'''

import os

debug = os.environ.get("RUN_ENV")

if debug == "prod":
    pass
    # from configs.cfg.rbac import ADMIN_LIST, RBAC_DB, RBAC_ECHO
    # from configs.cfg.sanguo import GAME_MANAGER_DB, GAME_MANAGER_ECHO, ONLY_READ_DB
else:
    pass
    # from configs.cfg_dev.rbac import ADMIN_LIST, RBAC_DB, RBAC_ECHO
    # from configs.cfg_dev.sanguo import GAME_MANAGER_DB, GAME_MANAGER_ECHO, ONLY_READ_DB
    # from configs.cfg_dev.rbac import ALLOW_HOST

PATH_APP_ROOT = os.path.abspath(
    os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))))

COOKIE_SECRET = "0wEE^@!TKGwbC0p@nyY4*Cm*8ojzulHC48HT620YJl^zE6qE"
PROJECT_NAME = "CuTeeyes"
ALLOW_HOST = []
LOGFILE = "/data/logs/rbac.log"
