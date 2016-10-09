# -*- coding: utf-8 -*-
import base
from quest.db.data import QuestData

# /quest/get
class Handler(base.BaseHandler):
    
    def get(self):
        quest_array = QuestData.query().order(-QuestData.date).fetch(10)
        values = { 'quest_array':quest_array }
        self.render('/statics/quest_list.html', values)