import random
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
