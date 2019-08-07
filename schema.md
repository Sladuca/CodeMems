# Data structures #

This file contains documentation for data formats for JSON and the database

## JSON Data ##

Data to formats to be sent to/from client applications to backend via HTTP requests. In requests, ALL data must be enclosed in a singleton list, and empty lists are invalid. Protocol buffers may actually be incredibly useful when sending / receiving data between services, especially since we 

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



### Note ###

Data structure for storing a unit of information to memorize. Corresponds to at least one Card.
Right now, provide

* `int id`: the note's id
* `int owner`: id of the owner's account
* `String note_type`: the note's type. Right now, only `card`
* `Obj data`:
  * `Obj fields`: maps field names to field contents
  * `list cards`: contains `(front, back)` ordered pairs, representing the content on a card, where `front` and `back` are entries in `fields`


Example function signature `CARD` type note:
```
[{
  id: 1,
  owner: 0
  note_type: "CARD",
  data: {
    fields: {
      "API Function": "numpy.zeros function signature",
      "Parameters": "shape, dtype (optional), order (optional)",
      "Return value": "ndarray with all zeros"
    },
    // cards get embedded in the notes that define them
    cards: [
      ...
    ]
  }
}]
```

### Card ###

Data structure for storing a specific review item and its scheduling information. Corresponds to 1 Note.

* int no: cloze deletion number if associated note is `CLOZE` type, arbitrary otherwise (used as identifier with parent note)
* Obj scheduling-info: see below
* String prompt:
  * IF associated `note` is type `CLOZE`, same as `note.data.text`, but with cloze insertion replaced with
  ```// answer here```
  * IF associated `note` is type `CARD`, arbitrary text entered by user with the key of at least one entry in `note.data` in handlebars (`{{}}`).
* String answer (only exists IF associated `note` is type `CARD`):
  * same as prompt, but for the answer

Example function signature cards from above `CLOZE` type example:
```
[
  {
    id: 0,
    scheduling_info: {...},
    prompt: "Generate a 2x1 numpy i32 array filled with zeros:\n// answer here",
  },
]
```

Example function signature cards from above `CARD` type example:
```
[
  {
    id: 0,
    scheduling_info: {...},
    prompt: "Parameters of {{API Function}}",
    answer: "{{Parameters}}",
  },
  {
    id: 1,
    scheduling_info: {...},
    prompt: "Retval of {{API Function}}",
    answer: "{{Return value}}",
  },
  {
    id: 2,
    scheduling_info: {...},
    prompt: "what numpy function takes {{Parameters}} as parameters and returns {{Return Value}}?"
    answer: "{{API Function}}"
  }
]
```

### Scheduling Info ###
object containing scheduling info. For now, just date for next review and the number of the bin for Leitner system.

example:
```
{
  next-review: 2020-01-01T00:00:00.000Z,
  bin: 0
}
```

## DB data

We're using MongoDB, so it's exactly the same!
