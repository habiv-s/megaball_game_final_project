import random


class Event:
    def __init__(self, ticks, mag):
        self.ticks = ticks
        self.magnitude = mag


class ScreenShake:
    def __init__(self, game):
        self.game = game

        self.x = 0
        self.y = 0

        self.events = []

    def add_event(self, ticks, magnitude, queue=False):
        if ticks < 0 or magnitude <= 0:
            return

        if len(self.events) > 0 and not queue:
            return

        self.events.append(Event(ticks, magnitude))

    def update(self):
        if len(self.events) > 0:
            events = self.events[0]
            events.ticks -= 1
            if events.ticks == 0:
                self.events.pop(0)
                self.x = 0
                self.y = 0
            else:
                self.x = random.randint(-events.magnitude, events.magnitude)
                self.y = random.randint(-events.magnitude, events.magnitude)
