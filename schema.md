# Data structures #

This file contains documentation for data formats for JSON and the database

## JSON Data ##

Data to formats to be sent to/from client applications to backend via HTTP requests. In requests, ALL data must be enclosed in a singleton list, and empty lists are invalid.

### Note ###

Data structure for storing a unit of information to memorize. Can translate to
several flashcards (`NoteType: CARD`) or
[cloze-deletions](https://en.wikipedia.org/wiki/Cloze_test) (`NoteType: CLOZE`). Corresponds to at least one Card.
Eventually support more types, in addition to adding custom types.

* int id: the note's id
* int owner: id of the owner's account
* String note-type: the note's type. Can be 'CLOZE' xor 'CARD'
* Obj data:
  * IF `CLOZE`:
    * String text: card text with cloze-item notation, i.e. "console.log({{1}})"
    * Obj cloze: map cloze fields number and its contents
    * i.e. `{1: "console.log('Hello World')"}`
  * IF `CARD`:
    * Obj fields: maps field names to field contents
  * list cards: maps front:back field names for each card


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
Example usage `CLOZE` type note
```
[{
  id: 1,
  owner: 0,
  note_type: "CLOZE",
  data: {
    text: "Generate a 2x1 numpy i32 array filled with zeros:\n {{1}}",
    // cards get embedded in the notes that define them
    cards: [
      ...
    ],
    cloze: {
      1: res = np.zeros((2, 1))
    }
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
