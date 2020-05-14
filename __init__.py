from mycroft import MycroftSkill, intent_file_handler


class Calm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calm.intent')
    def handle_calm(self, message):
        self.speak_dialog('calm')


def create_skill():
    return Calm()

