from aqt import mw
from aqt.main import AnkiQt


def realOverview(self):
    self.col.reset()
    self.moveToState("overview")


def onOverview(self):
    self.onReview()


def onReview(self):
    self.col.startTimebox()
    self.moveToState("review")


AnkiQt.onOverview = onOverview
AnkiQt.realOverview = realOverview
AnkiQt.onReview = onReview
