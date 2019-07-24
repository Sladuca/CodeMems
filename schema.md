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
* String note-type: the note's type. Can be 'CLOZE' xor 'CARD'
* Obj data:
  * IF `CLOZE`:
    * String text: card text with cloze-item notation, i.e. "console.log({{1}})"
    * Obj cloze: map cloze fields number and its contents
    * i.e. `{1: "console.log('Hello World')"}`
  * IF `CARD`:
    * Obj fields: maps field names to field contents
    * Obj cards: maps front:back field names for each card


Example function signature `CARD` type note:
```
[{
  id: 1,
  note_type: "CARD",
  data: {
    fields: {
      "API Function": "numpy.zeros function signature",
      "Parameters": "shape, dtype (optional), order (optional)",
      "Return-value": "ndarray with all zeros"
    },
    cards: {
    ["API Function", "Parameters"],
    ["API Function", "Return-value"]
    }
  }
}]
```
Example usage `CLOZE` type note
```
[{
  id: 2,
  note_type: "CLOZE",
  data: {
    text: "Generate a 2x1 numpy i32 array filled with zeros:\n {{1}}",
    cloze: {
      1: res = np.zeros((2, 1))
    }
  }
}]
```

### Card ###

Data structure for storing a specific review item and it's scheduling information. Corresponds to 1 Note.

* int id
* int note-id
* Obj scheduling-info: see below
* int no: cloze deletion number if associated note is `CLOZE` type, `null` otherwise
* String front:
  * IF associated `note` is type `CLOZE`, same as `note.data.text`, but with cloze insertion replaced with '[...]'
  * IF associated `note` is type `CARD`, key of an entry in `note.data.cards` with the field name of the answer appended afterwards in parenthesis
* String back:
  * IF associated `note` is type `CLOZE`, same as `note.data.text`, but with cloze insertion made with
  * IF associated `note` is type `CARD`, value of an entry in `note.data.cards`

Example function signature card from above `CARD` type example:
```
[{
  id: 1
  scheduling-info: {...},
  no: null,
  front: "numpy.zeros (Parameters)",
  back: "shape, dtype (optional), order (optional)"
}]
```

### Scheduling Info ###
object containing scheduling info. For now, just date for next review.

example:
```
{
  next-review: 2020-01-01T00:00:00.000Z
}
```

## DB data

We're using MongoDB, so it's exactly the same!
