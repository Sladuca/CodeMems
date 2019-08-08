# Data structures

This file contains documentation for data formats for JSON and the database

## JSON Data 

Data to formats to be sent to/from client applications to backend via HTTP requests. In requests, ALL data must be enclosed in a singleton list, and empty lists are invalid. Protocol buffers may actually be incredibly useful when sending / receiving data between services, especially since we have so many services. In fact, that's probably what we should do. 

At the moment, there are 4 major data structures. Conceptually, they are:


* Note
  * A Note is a unit of information that a user wants to remember.
  * For example, a Note may represent a function signature, containing a function’s parameters, return value, and behavior.
* Card
  * A card is an atomic piece of information associated with a Note, most of the time manifesting as a flashcard-like thing. Each Note corresponds to possible multiple cards, depending on what the user wishes to remember.
  * Going with the function signature example, a user may have a card that asks what the function returns, and a card that asks what parameters it takes
* Deck
  * A deck is a collection of notes, with the intended purpose of holding all of the notes on a particular topic.
  * Still following the same example, the function signature could be in a deck containing notes on a particular library / framework, for instance.
* Review
  * A review is a unit of data that characterizes a specific review of a specific card.
  * This is to serve as training data for an ML model that attempts to optimize the time for users to review their cards.



### Note

Data structure for storing a unit of information to memorize. Corresponds to at least one Card.
Right now, provide

* `id _id`: the note's id
* `id owner`: id of the owner's account
* `id deck`: id of the deck this note belongs to
* `String note_type`: the note's type. Right now, only `card`
* `Obj data`:
  * `Obj fields`: maps field names to field contents
  * `list cards`: contains `(front, back)` ordered pairs, representing the content on a card, where `front` and `back` are entries in `fields`

Example function signature `CARD` type note:
```
[{
  id: 1,
  owner: 0,
  deck: 0,
  note_type: "CARD",
  data: {
    fields: {
      "API Function": "numpy.zeros function signature",
      "Parameters": "shape, dtype (optional), order (optional)",
      "Return value": "ndarray with all zeros"
    },
    cards: [
      ("API Function", "Parameters"),
      ("API Function": "Return Value"),
    ],
  },
}]
```

### Card

Data structure for storing a specific review item and its scheduling information. Corresponds to 1 Note.

* `id _id`: id of the card
* `id owner`: id of the user who owns the card
* `id note`: id of the note this card corresponds to
* `id deck`: id of the deck this card belongs to
* `Date due`: date the card is due for review
* `Obj scheduling_info`: see below
* `String front`: html appearance of the front of the card
* `String back`: html appearance of the back of the card

Example:
```
[{
    id: 1,
    owner: 0,
    note: 1,
    deck: 0,
    due: 2020-01-01T00:00:00.000Z
    scheduling_info: {
        // see below
    },
    front: "numpy.zeros function signature",
    back: "ndarray with all zeros"
}]
```

### Scheduling Info
object containing scheduling info. For now, just the number of the bin for Leitner system.

example:
```
{
  bin: 0
}
```

### Deck
a collection of notes. Generally, this will by by topic.

* `id _id`: id of the deck
* `id owner`: id of the owner of the deck
* `String name`: name of the deck

Example:
```
[{
    id: 0,
    owner: 0,
    name: "Numpy"
}]
```

## DB data

We're using MongoDB, so it's exactly the same! (for now...)
