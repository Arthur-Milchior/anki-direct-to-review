from aqt import mw
from aqt.main import AnkiQt
from aqt.qt import *


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


def onStudyKey(self):
    self.onReview()


AnkiQt.onStudyKey = onStudyKey

for shortcut in mw.findChildren(QShortcut):
    key = shortcut.key().toString()
    if key == "S":
        shortcut.disconnect()
        shortcut.activated.connect(mw.onStudyKey)
        break


def onStudyDeck(self):
    from aqt.studydeck import StudyDeck
    ret = StudyDeck(
        self, dyn=True, current=self.col.decks.current()['name'])
    if ret.name:
        self.col.decks.select(self.col.decks.id(ret.name))
        self.onReview()


AnkiQt.onStudyDeck = onStudyDeck

m = mw.form
m.actionStudyDeck.triggered.disconnect()
m.actionStudyDeck.triggered.connect(mw.onStudyDeck)
