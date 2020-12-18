#!/usr/bin/env python3

import random
import time
import sys


def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


class Weapon:
    def __init__(self, health, attack, total_gold):
        self.health = health
        self.attack = attack
        self.total_gold = total_gold

    def treasure(self, chest):
        self.total_gold += chest.gold_pieces
        delay_print(f"You have {self.total_gold} gold pieces.")
        return self.total_gold


sword_shield = Weapon(3, 1, 0)
estoc_dagger = Weapon(2, 2, 0)
magic_staff = Weapon(1, 3, 0)


class Reward:
    def __init__(self, gold_pieces):
        self.gold_pieces = gold_pieces


# small_chest = Reward(10)
# large_chest = Reward(30)
nothing = "You see nothing.\n"


def room_encounter():
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


def combat(weapon, enemy):
    while (weapon.health > 0) and (enemy.health > 0):
        delay_print(f"Your health is {weapon.health}.\n")
        delay_print(f"The {enemy.name}'s health is {enemy.health}.\n")
        time.sleep(0.5)
        delay_print(f"You attack the {enemy.name}.\n")
        enemy.health -= weapon.attack
        # delay_print(f"Your health is {weapon.health}.\n")
        time.sleep(0.5)
        delay_print(f"The {enemy.name}'s health is {enemy.health}.\n")
        if enemy.health <= 0:
            delay_print(f"The {enemy.name} has died.\n")
            break
        time.sleep(0.5)
        delay_print(f"The {enemy.name} attacks you.\n")
        weapon.health -= enemy.attack
        # time.sleep(0.5)
        # delay_print(f"Your health is {weapon.health}.\n")
        time.sleep(0.5)
        # delay_print(f"The {enemy.name}'s health is {enemy.health}.\n")
        if weapon.health <= 0:
            delay_print("You have died.\n")
            delay_print("Game Over.")
            quit()
            break


def main():

    dung_entry_loop = ()
    while dung_entry_loop == ():
        delay_print("Do you want to enter the dungeon? Yes(y) or No(n).\n")
        dung_entry = input()
        if dung_entry == "y":
            for x in range(0, 100):
                delay_print("What is your starting equipment?\n")
                equip = int(input("1 = sword and shield, 2 = estoc and dagger, and 3 = magic staff\n"))
                if equip == 1:
                    delay_print("You have equipted the sword and shield.\n")
                    champion = sword_shield
                    break
                elif equip == 2:
                    delay_print("You have equipted the estoc and dagger.\n")
                    champion = estoc_dagger
                    break
                elif equip == 3:
                    delay_print("You have equipted the magic staff.\n")
                    champion = magic_staff
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