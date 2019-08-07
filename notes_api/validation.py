'''
VALIDATION
data integrity checks for all note-related data being recieved by the server from clients.
'''

async def is_note(note):
    # check well-formedness
    if (
        not isInstance(note, dict)
        or "note_type" not in note
        or "data" not in note
        or "fields" not in note.data
        or not isInstance(note.data, dict)
    ): return False
    # check to make sure card references are not present
    if "card" in note:
        return False
    return True
