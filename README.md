# Direct to review
## Rationale
Someone did want to hide the number of cards to review. Which requires
to skip overview.

Furthermore, I personnaly never use overview; so I'm winning time
here. Even if I'm not sure I'm winning more time than what I spent
developping it.

The gear now contains an "overview" button, for people actually
wanting to go to overview.

This deals with the three main way of accessing review: clicking on a
deck name, pressing the shortcut "s" or "/".

## Incompatible add-ons
The [progress bar](https://ankiweb.net/shared/info/2091361802) won't start when you install this add-on. 

## Internal
It changes:
* `AnkiQt.onOverview` by calling directly `onReview`
* `AnkiQt.onStudyDeck`
* `AnkiQt.onStudyKey`

## Version 2.0
None

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-direct-to-review
Addon number| [1024346707](https://ankiweb.net/shared/info/1024346707)
