from django.db import models

# Create your models here.


class Jeju:
    def __init__(self, option):
        print("시작하자")
        day = option.data['date']
        people = option.data['Number']
        user = option.data['user']
        month = option.data['date'][2]
        relationship = option.data['relationship']

    def plane(self):
        pass

    def accommodation(self):
        pass

    def activty(self):
        pass

    def tourism(self):
        pass

    def olle(self):
        pass

    def restaurant(self):
        pass

    def shop(self):
        pass
