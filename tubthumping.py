from collections import deque

class Them(object):
    def __init__(self):
        pass

    def can_keep_down(self, person):
        return person.can_be_kept_down

class Me(object):
    def __init__(self):
        self.can_be_kept_down = False
        self.am_I_down = False

    def get_knocked_down(self):
        self.am_I_down = True
        print("I get knocked down")
        if not self.can_be_kept_down:
            self.am_I_down = False
            print("but I get up again")

class Him(object):
    def __init__(self):
        self.drinks = deque(['Whiskey', 'Vodka', 'Lager', 'Cider'])
        self.times = deque(["Good", "Best"])

    def whats_he_doing(self):
        while self.drinks:
            print(f"He drinks a {self.drinks.popleft()} drink,")
        while self.times:
            print(f"He sings the songs that remind him of the {self.times.popleft()} times")

while True:
    I = Me()
    You = Them()
    He = Him()
    for x in range(4):
        I.get_knocked_down()
        print(f"Can you keep me down: {You.can_keep_down(I)}")
    He.whats_he_doing()
