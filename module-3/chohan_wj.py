"""Cho-Han dice game (brownfield assignment for CSD325, Module 3.2).

Original program: Al Sweigart, Big Book of Small Python Projects.
Modified by: Walter Jacobo
Assignment: CSD325 Module 3.2 - Brownfield + Flowchart

Changes from the original:
- Changed both player input prompts to "WJ:".
- Changed the house fee on a winning bet from 10% to 12%.
- Added a notice and a 10-mon bonus for dice totals of 2 or 7.
- Documented changes while retaining the original program structure.
"""

import random
import sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
If the dice total is 2 or 7, you receive a 10 mon bonus!
''')  # WJ: Explain the new bonus before the game starts.

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('WJ: ')  # WJ: Use my initials for the input prompt.
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('WJ: ').upper()  # WJ: Use the same initials for this prompt.
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add winnings to the purse.
        house_fee = pot * 12 // 100  # WJ: House now collects 12%, rounded down to whole mon.
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot  # Subtract the lost bet from the purse.
        print('You lost!')

    # WJ: Award a 10-mon bonus for a total of 2 or 7, win or lose.
    dice_total = dice1 + dice2
    if dice_total == 2 or dice_total == 7:
        print('The dice total is', dice_total, '- you got a 10 mon bonus!')
        purse = purse + 10

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
