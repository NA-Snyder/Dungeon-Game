#!/usr/bin/env python3
"""Roguelike game | Author: Nathan Snyder"""

# Imports necessary dependencies.
import random
import time
import sys


def delay_print(s):
    """Printing function that prints one character at a time."""
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Enemy:
    """Class that defines attributes to enemies that player character may make contact with."""
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


class Vocation:
    """Class that defines attributes for the player character to select at the beginning of the game."""
    def __init__(self, health, attack, total_gold):
        self.health = health
        self.attack = attack
        self.total_gold = total_gold

    def treasure(self, chest):
        self.total_gold += chest.gold_pieces
        delay_print(f"You have {self.total_gold} gold pieces.")
        return self.total_gold


fighter = Vocation(3, 1, 0)
strider = Vocation(2, 2, 0)
mage = Vocation(1, 3, 0)


class Reward:
    """Class the assigns attributes to rewards that the player character may make contact with."""
    def __init__(self, gold_pieces):
        self.gold_pieces = gold_pieces


nothing = "You see nothing.\n"


def room_encounter():
    """Function for random room encounters. Also assigns attributes from the classes to the objects."""
    encounter = random.randint(1, 5)
    if encounter == 1:
        delay_print("You see a goblin.\n")
        goblin = Enemy('goblin', 2, 1)
        return ("foe", goblin)
    elif encounter == 2:
        delay_print("You see a bat.\n")
        bat = Enemy('bat', 1, 2)
        return ("foe", bat)
    elif encounter == 3:
        delay_print("You see a small chest.\n")
        small_chest = Reward(10)
        return ("reward", small_chest)
    elif encounter == 4:
        delay_print("You see a large chest.\n")
        large_chest = Reward(30)
        return ("reward", large_chest)
    elif encounter == 5:
        return ("nothing", nothing)
    return


def combat(vocation, enemy):
    """Combat function between the player character and an enemy that they come into contact with."""
    while (vocation.health > 0) and (enemy.health > 0):
        delay_print(f"Your health is {vocation.health}.\n")
        delay_print(f"The {enemy.name}'s health is {enemy.health}.\n")
        time.sleep(0.5)
        delay_print(f"You attack the {enemy.name}.\n")
        enemy.health -= vocation.attack
        time.sleep(0.5)
        delay_print(f"The {enemy.name}'s health is {enemy.health}.\n")
        if enemy.health <= 0:
            delay_print(f"The {enemy.name} has died.\n")
            break
        time.sleep(0.5)
        delay_print(f"The {enemy.name} attacks you.\n")
        vocation.health -= enemy.attack
        time.sleep(0.5)
        if vocation.health <= 0:
            delay_print("You have died.\n")
            delay_print("Game Over.")
            quit()
            break


def main():
    """Runs game"""
    dung_entry_loop = ()
    while dung_entry_loop == ():
        delay_print("Do you want to enter the dungeon? Yes(y) or No(n).\n")
        dung_entry = input()
        if dung_entry == "y":
            for x in range(0, 100):
                delay_print("What is your vocation?\n")
                equip = int(input("1 = Fighter, 2 = Strider, and 3 = Mage\n"))
                if equip == 1:
                    delay_print("You have chosen Fighter.\n")
                    champion = fighter
                    break
                elif equip == 2:
                    delay_print("You have chosen Strider.\n")
                    champion = strider
                    break
                elif equip == 3:
                    delay_print("You have chosen Mage.\n")
                    champion = mage
                    break
                else:
                    delay_print("That is not a valid response, try again.\n")
            rooms = random.randint(0, 3) + 3
            room_num = 1
            while rooms != 0:
                delay_print(f"You have entered room {room_num}.\n")
                room_experience, item = room_encounter()
                if room_experience == "foe":
                    combat(champion, item)  # run combat function
                elif room_experience == "reward":
                    champion.treasure(item)  # run treasure function
                elif room_experience == "nothing":
                    delay_print(nothing)
                room = input(f"Do you want to continue? Yes(y) or No(n).\n")
                if room == "y":
                    rooms -= 1
                    room_num += 1
                elif room == "n":
                    delay_print("You have exited the dungeon.\n")
                    quit()
                else:
                    delay_print("That is not a valid response, try again.\n")
            delay_print("You have reached the end of the dungeon.\n")
            delay_print(f"You have collected {champion.total_gold} gold pieces. Thanks for playing!\n")
            break
        elif dung_entry == "n":
            delay_print("You did not enter the dungeon.\n")
            quit()
        else:
            delay_print("That is not a valid response, try again.\n")


main()
