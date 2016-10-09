from google.appengine.ext import ndb

class QuestData(ndb.Model):
    name = ndb.StringProperty()
    img_url = ndb.StringProperty()
    grade = ndb.IntegerProperty()
    quest_resili = ndb.IntegerProperty()
    contents = ndb.StringProperty()
    status = ndb.IntegerProperty()
    owner_name = ndb.StringProperty()
    player_name = ndb.StringProperty()
    feedback = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @staticmethod
    def create_entity(self):
        quest = QuestData()
        quest.name = self.request.get('name')
        quest.img_url = "hoge"
        quest.grade = 0
        quest.quest_resili = 0
        quest.contents = self.request.get('contents')
        quest.status = 0
        quest.owner_name = "hoge"
        quest.player_name = "hoge" 
        quest.feedback = 0
        quest.put()
        return "done"