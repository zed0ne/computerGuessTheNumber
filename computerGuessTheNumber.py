import random # to generate random numbers
import secrets
from colorama import Fore,Back,Style
from colorama import init
from colorama import deinit

print(Fore.YELLOW+'\t\t\t\t\t\t>> welcome to "Computer guess the number" game! <<\n'+Fore.RESET)
print(Fore.MAGENTA+'|| Select a number and consider it,\t\t\t\t\t\t\t\t  ||\n|| the computer guesses that number and you will say whether the number is correct or not.\t  ||')
print('|| Type "s", "b", if your number is smaller,bigger or "c" if computer guessed the correct number. ||\n'+Fore.RESET)
try_count = 1
maxi = 1000
mini = -1000
computer_guess = random.randint(-1000,1000) #computer first guess can be 0 to find the number faster
status = input(f'{Fore.CYAN}My first guess is {computer_guess}.{Fore.RESET}{Fore.YELLOW}\nhow is your number (type "c" if my guess was right)? {Fore.RESET}')

while status != 'c':
    if status == 's': 
        try_count += 1
        maxi = computer_guess
        computer_guess = random.randint(mini,computer_guess)        
        print(Fore.CYAN + 'my guess is: ', computer_guess, Fore.RESET)
        status = input(Fore.YELLOW + 'how is your number? ' + Fore.RESET)
    
    if status == 'b':
        try_count += 1
        mini = computer_guess
        computer_guess = random.randint(computer_guess,maxi)        
        print(Fore.CYAN + 'my guess is:', computer_guess, Fore.RESET)
        status = input(Fore.YELLOW + 'how is your number? ' + Fore.RESET)

print(Fore.MAGENTA + 'your number was', computer_guess, 'and i found it with',try_count, 'try(s)!', Fore.RESET)
