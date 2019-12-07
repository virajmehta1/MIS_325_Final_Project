#Text-based Military-Scenario Game

import random
import time
from colorama import init
from colorama import Fore, Back, Style

init()

def displayIntro():
    print(Fore.GREEN + "You are a soldier trapped deep behind enemy lines")
    print(Fore.GREEN + "you come to a crossroads on your retreat, it is dark, but you know one path leads home")
    print(Fore.GREEN + "where you will find your support team and recieve a purple heart for your bravery")
    print(Fore.GREEN + "while the other leads through an enemy scouting camp that will shoot you on site")
    print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path will you choose? (1 or 2): ")
    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("you hear soldiers talking, that must be a good sign...")
    time.sleep(2)
    print("But a spotlight shines on you...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)
    if chosenPath == str(correctPath):
        print(Fore.CYAN + "That light was from your support team looking for you!")
        time.sleep(1)
        print(Fore.CYAN + "Welcome home soldier!")
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)
    else:
        print(Fore.RED + "The light came from the enemy spotting you lurking around")
        time.sleep(2)
        print(Fore.RED + "causing them to yell and rain down machine gun fire")
        time.sleep(1)
        print(Fore.RED + "you lie in your own pool of blood...taking your last few breaths")
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")


