import random
while True:
    print('plz make your choice:)')
    choice=input()
    choice=choice.lower()
    print('your choice is',choice)
    choices=['rock','paper','scissor']
    computer_choice = choices[random.randint(0,2)]
    print('computer choice is',computer_choice)

    if choice == 'rock':
        if computer_choice == 'rock':
            print('its a tie')
        elif computer_choice == 'paper':
            print('soory...you loose...')
        elif computer_choice == 'scissor':
            print('you win!!!..')

    if choice == 'paper':
        if computer_choice == 'paper':
            print('its a tie')
        elif computer_choice == 'scissor':
            print('soory...you loose...')
        elif computer_choice == 'rock':
            print('you win!!!..')

    if choice == 'scissor':
        if computer_choice == 'scissor':
            print('its a tie')
        elif computer_choice == 'rock':
            print('sorry...you loose...')
        elif computer_choice == 'paper':
            print('you win!!!..')

    print()



