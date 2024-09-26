import random

def get_user_choice():
    choice = input("Escolha uma opção (pedra, papel, tesoura): ").lower()
    while choice not in ['pedra', 'papel', 'tesoura']:
        choice = input("Escolha inválida. Tente novamente (pedra, papel, tesoura): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['pedra', 'papel', 'tesoura'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == 'pedra' and computer_choice == 'tesoura') or          (user_choice == 'papel' and computer_choice == 'pedra') or          (user_choice == 'tesoura' and computer_choice == 'papel'):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Você escolheu: {user_choice}")
    print(f"O computador escolheu: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()