'''
CARD OPS
The notes_api performs all functions on card data, from creation to destruction
'''

async def create_cards(note, mongoClient):
    '''
    given a note, generate all corresponding cards and add them to the database
    if they already exist, update them
    '''
    pass

async def read_cards(ids, mongoClient):
    '''
    return list of cards with the given id
    '''
    pass

async def delete_cards(note, mongoClient):
    '''
    given a note, delete all of its corresponding cards
    '''
    pass

async def update_cards(note, mongoClient):
    '''
    given a note, update all of its corresponding cards to match it
    '''
    pass
