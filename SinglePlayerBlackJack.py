#Single Player BlackJack (Modified)

from random import choice

def run():
    '''Begins the program, and handles whether or not the player would like to continue playing.'''
    running = True
    welcome()
    gameplay()
    while running:
        print('\nType \'Start\' to play!\nType \'End\' anytime to end.')
        first = input()
        if first.lower() not in ('start', 'end'):
            print('Invalid Entry. Try Again.')
        elif first.lower() == 'end':
            print('\nThanks for playing!')
            running = False
        else:
            gameplay()


def welcome():
    '''Prints the welcome banner of the game.'''
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Welcome to Single-Player BlackJack (Modified Edition)!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    rules()


def rules():
    '''Prints the rules of the game.'''
    print('RULES OF THE GAME:')
    print('----------------------------------------------------------------------')
    print('The objective of the game is to reach the value 21, which is achieved')
    print('through the addition of the values of the cards themself.\n')
    print('Each card has its own numeric value, with a 2 of hearts equaling 2,')
    print('and a 7 of spades equaling 7 for instance.\n')
    print('For face cards (i.e. King of Spades, Queen of Hearts) the value')
    print('always be 10.\n')
    print('For any Ace, the user must determine whether they would like for its')
    print('value to be a 1 or 11.\n')
    print('In this modified version, the user must select the Ace value at the')
    print('start of the game. Will you take the chance and play big?\n')
    print('If the user were to go over the value of 21, they would then \'bust\',')
    print('losing the game.\n')
    print('If the user were to settle with any value before 21, they would')
    print('effectively be playing against the dealer, and if the dealer\'s cards')
    print('equates to a higher value, the user loses.')
    print('----------------------------------------------------------------------\n')
    commands()


def commands():
    '''Prints the commands of the game.'''
    print('COMMANDS OF THE GAME:')
    print('---------------------------------------------------------------------')
    print('Hit:   Request the dealer for another card.')
    print('Stand: Lock in your hand as your final hand and the dealer will show.')
    print('---------------------------------------------------------------------')


def gameplay():
    '''
    Handles the entire gameplay; the function keeps track of the player's current total, as well as
    determines whether or not the player has busted. The function determines the winner of the game
    and prints a message based on whether or not the user has won.
    '''
    print('Will Aces count as 1 or 11?')
    deck = select_deck()

    player = player_hand(deck)
    dealer = dealer_hand(deck)

    player_total = player[0][1] + player[1][1]

    if player_total == 21:
        print('BlackJack! You Win!')
        return

    continued = True
    while continued:
        print(f'Your hand contains: {player}\n')
        print(f'The dealer\'s hand contains: {dealer[0]}\n')
        print('Hit or Stand?')
        action = input()
        if action.lower() not in ('hit', 'stand'):
            print('Invalid Entry. Try Again.')
        elif action.lower() == 'hit':
            new_card = choice(deck)
            deck.remove(new_card)
            player.append(new_card)
            player_total += new_card[1]
            if player_total == 21:
                print(f'Your hand contains: {player}\n')
                print(f'The dealer\'s hand contains: {dealer[0]}\n')
                print('BlackJack! You Win!')
                return
            elif player_total > 21:
                print(f'Your hand contains: {player}\n')
                print(f'The dealer\'s hand contains: {dealer[0]}\n')
                print('Bust! You lose.')
                return 
        else:
            continued = False

    print(f'Your hand contains: {player}\n')
    print(f'The dealer\'s hand contains: {dealer}\n')
    dealer_total = dealer[0][1] + dealer[1][1]
    if dealer_total > 21:
        print('You win!')
        return
    elif dealer_total >= player_total:
        print('You lose!')
        return
    else:
        print('You win!')
        return


def select_deck():
    '''
    Selects the deck which will be used; since the player predetermines the value of Ace in each round,
    the decks are identical with the exception of the Ace values. Returns a set of tuples which
    contains the deck information.
    '''
    while True:
        deck_choice = int(input())
        if deck_choice not in (1, 11):
            print('Invalid Entry. Try Again.')
        elif deck_choice == 1:
            deck = [('2 of Hearts', 2), ('2 of Diamonds', 2), ('2 of Clubs', 2), ('2 of Spades', 2),
                    ('3 of Hearts', 3), ('3 of Diamonds', 3), ('3 of Clubs', 3), ('3 of Spades', 3),
                    ('4 of Hearts', 4), ('4 of Diamonds', 4), ('4 of Clubs', 4), ('4 of Spades', 4),
                    ('5 of Hearts', 5), ('5 of Diamonds', 5), ('5 of Clubs', 5), ('5 of Spades', 5),
                    ('6 of Hearts', 6), ('6 of Diamonds', 6), ('6 of Clubs', 6), ('6 of Spades', 6),
                    ('7 of Hearts', 7), ('7 of Diamonds', 7), ('7 of Clubs', 7), ('7 of Spades', 7),
                    ('8 of Hearts', 8), ('8 of Diamonds', 8), ('8 of Clubs', 8), ('8 of Spades', 8),
                    ('9 of Hearts', 9), ('9 of Diamonds', 9), ('9 of Clubs', 9), ('9 of Spades', 9),
                    ('10 of Hearts', 10), ('10 of Diamonds', 10), ('10 of Clubs', 10), ('10 of Spades', 10),
                    ('Jack of Hearts', 10), ('Jack of Diamonds', 10), ('Jack of Clubs', 10), ('Jack of Spades', 10),
                    ('Queen of Hearts', 10), ('Queen of Diamonds', 10), ('Queen of Clubs', 10), ('Queen of Spades', 10),
                    ('King of Hearts', 10), ('King of Diamonds', 10), ('King of Clubs', 10), ('King of Spades', 10),
                    ('Ace of Hearts', 1), ('Ace of Diamonds', 1), ('Ace of Clubs', 1), ('Ace of Spades', 1)]
            return deck
        else:
            deck = [('2 of Hearts', 2), ('2 of Diamonds', 2), ('2 of Clubs', 2), ('2 of Spades', 2),
                    ('3 of Hearts', 3), ('3 of Diamonds', 3), ('3 of Clubs', 3), ('3 of Spades', 3),
                    ('4 of Hearts', 4), ('4 of Diamonds', 4), ('4 of Clubs', 4), ('4 of Spades', 4),
                    ('5 of Hearts', 5), ('5 of Diamonds', 5), ('5 of Clubs', 5), ('5 of Spades', 5),
                    ('6 of Hearts', 6), ('6 of Diamonds', 6), ('6 of Clubs', 6), ('6 of Spades', 6),
                    ('7 of Hearts', 7), ('7 of Diamonds', 7), ('7 of Clubs', 7), ('7 of Spades', 7),
                    ('8 of Hearts', 8), ('8 of Diamonds', 8), ('8 of Clubs', 8), ('8 of Spades', 8),
                    ('9 of Hearts', 9), ('9 of Diamonds', 9), ('9 of Clubs', 9), ('9 of Spades', 9),
                    ('10 of Hearts', 10), ('10 of Diamonds', 10), ('10 of Clubs', 10), ('10 of Spades', 10),
                    ('Jack of Hearts', 10), ('Jack of Diamonds', 10), ('Jack of Clubs', 10), ('Jack of Spades', 10),
                    ('Queen of Hearts', 10), ('Queen of Diamonds', 10), ('Queen of Clubs', 10), ('Queen of Spades', 10),
                    ('King of Hearts', 10), ('King of Diamonds', 10), ('King of Clubs', 10), ('King of Spades', 10),
                    ('Ace of Hearts', 11), ('Ace of Diamonds', 11), ('Ace of Clubs', 11), ('Ace of Spades', 11)]
            return deck


def player_hand(deck):
    '''Returns a two-list of tuples containing the hand of the player.'''
    player_card1 = choice(deck)
    player_card2 = choice(deck)
    deck.remove(player_card1)
    deck.remove(player_card2)
    return [player_card1, player_card2]


def dealer_hand(deck):
    '''Returns a two-list of tuples containing the hand of the dealer.'''
    dealer_card1 = choice(deck)
    dealer_card2 = choice(deck)
    deck.remove(dealer_card1)
    deck.remove(dealer_card2)
    return [dealer_card1, dealer_card2]
                

if __name__ == '__main__':
    run()
    
