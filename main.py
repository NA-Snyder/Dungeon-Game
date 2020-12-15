#!/usr/bin/env python3

import random


class Enemy:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def take_damage(self):
        damage = Weapon.attack
        self.damage -= Weapon.attack
        starting_health = self.health
        if starting_health - damage > 0:
            self.health -= damage
        else:
            self.health = 0
            damage = starting_health


goblin = Enemy(2, 1)
bat = Enemy(1, 2)


class Weapon:
    def __init__(self, armor, attack):
        self.armor = armor
        self.attack = attack

    def take_damage(self):
        damage = Enemy.attack
        self.damage -= Enemy.attack
        starting_health = self.armor
        if starting_health - damage > 0:
            self.armor -= damage
        else:
            self.health = 0
            damage = starting_health


sword_shield = Weapon(3, 1)
estoc_dagger = Weapon(2, 2)
magic_staff = Weapon(1, 3)


class Reward:
    def __init__(self, gold_pieces):
        self.gold_pieces = gold_pieces


small_chest = Reward(10)
large_chest = Reward(30)


def room_encounter():
    encounter = random.randint(1, 5)
    if encounter == 1:
        print("You see a goblin.")
    elif encounter == 2:
        print("You see a bat.")
    elif encounter == 3:
        print("You see a small chest.")
    elif encounter ==4:
        print("You see a large chest.")
    else:
        print("You see nothing.")
    return

# def combat():

# def rooms():
#     rooms = 3
#     add_room = random.randint(0, 3)
#     rooms + add_room = rooms


def main():

    print("Do you want to enter the dungeon? Yes(y) or No(n).")
    dung_entry = input()
    if dung_entry == "y":
        print("What is your starting equipment?")
        equip = input("1 = sword and shield, 2 = estoc and dagger, and 3 = magic staff")
        for equip in range(1, 3):
            if equip == 1:
                print("You have equipted the sword and shield.")
                break
            elif equip == 2:
                print("You have equipted the estoc and dagger.")
                break
            elif equip == 3:
                print("You have equipted the magic staff.")
                break
            else:
                print("That is not a valid response, try again.")
        print("You have entered the first room.")
        room_encounter()
        room = input(f"Do you want to continue? Yes(y) or No(n).") # create loop for entering next room.
        if room == "y":
            print("You have entered the next room.")
            room_encounter()
            room3 = input(f"Do you want to continue? Yes(y) or No(n).")
            if room3 == "y":
                print("You have entered the final room.")
                room_encounter()
            elif room3 == "n":
                print("You have exited the dungeon.")
                quit()
            else:
                print("That is not a valid response, try again.")
        elif room == "n":
            print("You have exited the dungeon.")
            quit()
        else:
            print("That is not a valid response, try again.")
    elif dung_entry == "n":
        print("You did not enter the dungeon.")
        quit()
    else:
        print("That is not a valid response, try again.")


main()