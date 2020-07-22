from mycroft import MycroftSkill, intent_file_handler
import wiringpi

#give pin numbers (the set up I run uses the GPIO pin numbering )
red_front = 16
green_front = 20
blue_front = 27

red_back = 22
green_back = 21
blue_back = 17

wiringpi.wiringPiSetupGpio() #this comand tells the program to use the GPIO pinout

#these comands set up each pin as outputs
wiringpi.pinMode(red_back, 1)
wiringpi.pinMode(blue_back, 1)
wiringpi.pinMode(green_back, 1)
wiringpi.pinMode(red_front, 1)
wiringpi.pinMode(blue_front, 1)
wiringpi.pinMode(green_front, 1)

#thest comands create the ablity for PWM on each pin with the range of each
wiringpi.softPwmCreate(red_front, 0, 100)
wiringpi.softPwmCreate(blue_front, 0, 100)
wiringpi.softPwmCreate(green_front, 0, 100)
wiringpi.softPwmCreate(red_back, 0, 100)
wiringpi.softPwmCreate(blue_back, 0, 100)
wiringpi.softPwmCreate(green_back, 0, 100)


#now we start the skill
class Startuplight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.add_event('mycroft.ready', self.handler_mycroft_ready)
        self.add_event('recognizer_loop:wakeword', self.handler_wakeword)

#this function causes the lights to fade teal when ready to go
    def handler_mycroft_ready(self, message):
        for brightness in range(0,100):
            wiringpi.softPwmWrite(blue_back, brightness)
            wiringpi.softPwmWrite(blue_front, brightness)
            wiringpi.softPwmWrite(green_back, brightness)
            wiringpi.softPwmWrite(green_front, brightness)
            wiringpi.delay(10)
        for brightness in reversed(range(0,100)):
            wiringpi.softPwmWrite(blue_back, brightness)
            wiringpi.softPwmWrite(blue_front, brightness)
            wiringpi.softPwmWrite(green_back, brightness)
            wiringpi.softPwmWrite(green_front, brightness)
            wiringpi.delay(10)

#this code fades white when the code word is reconginzed
    """def handler_wakeword(self, message):
        for brightness in range(0,100):
            wiringpi.softPwmWrite(blue_back, brightness)
            wiringpi.softPwmWrite(blue_front, brightness)
            wiringpi.softPwmWrite(green_back, brightness)
            wiringpi.softPwmWrite(green_front, brightness)
            wiringpi.softPwmWrite(red_back, brightness)
            wiringpi.softPwmWrite(red_front, brightness)
        for brightness in reversed(range(0,100)):
            wiringpi.softPwmWrite(blue_back, brightness)
            wiringpi.softPwmWrite(blue_front, brightness)
            wiringpi.softPwmWrite(green_back, brightness)
            wiringpi.softPwmWrite(green_front, brightness)
            wiringpi.softPwmWrite(red_back, brightness)
            wiringpi.softPwmWrite(red_front, brightness)"""







def create_skill():
    return Startuplight()
