# -*- coding: utf-8 -*-

import json
import base
from quest.db.data import QuestData

# /quest/post
class Handler(base.BaseHandler):
    def get(self):
        self.render('/statics/quest_input.html')
        return

    def post(self):
        res = QuestData.create_entity(self)
        self.response.write(res)
        return
