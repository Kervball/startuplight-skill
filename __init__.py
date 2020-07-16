from mycroft import MycroftSkill, intent_file_handler


class Startuplight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('startuplight.intent')
    def handle_startuplight(self, message):
        self.speak_dialog('startuplight')


def create_skill():
    return Startuplight()

