# -*- coding: utf-8 -*-

import requests
from common.logger import Log

class Blog():
    log = Log()

    def login(self):
        url = 'http://sps.cecook.net/login/ajaxLogin'
