# validate data

async def is_note(note):
    # check well-formedness
    if (
        not isInstance(note, dict)
        or "note_type" not in note
        or "data" not in note
        or "fields" not in note.data
        or "cards" not in note.data
        or not isInstance(note.data, dict)
    ): return False
    # check to make sure cloze field exists
    if "cloze" not in note.data:
        return False
    return True

async def is_card(card):
    pass
