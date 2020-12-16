#!/usr/bin/env python3

import random


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
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


goblin = Enemy('goblin', 2, 1)
bat = Enemy('bat', 1, 2)


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


def combat():
    while (Weapon.health > 0) and (Enemy.health > 0):
        print(f"Your health is {Weapon.health}.")
        print(f"{Enemy.name}'s health is {Enemy.health}.")
        Enemy.health -= Weapon.attack
        print(f"Your health is {Weapon.health}.")
        print(f"{Enemy.name}'s health is {Enemy.health}.")
        if Enemy.health <= 0:
            print(f"{Enemy.name} has died.")
            break
        Weapon.health -= Enemy.attack
        print(f"Your health is {Weapon.health}.")
        print(f"{Enemy.name}'s health is {Enemy.health}.")
        if Weapon.health <= 0:
            print("You have died.")
            break




def main():

    dung_entry_loop = ()
    while dung_entry_loop == ():
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
            rooms = random.randint(0, 3) + 3
            room_num = 1
            while rooms != 0:
                print(f"You have entered room {room_num}.")
                room_encounter()
                # if room_encounter() == 1 or 2:
                    # combat() ## run combat function
                # elif room_encounter() == 3 or 4:
                    # reward() ## run reward function
                room = input(f"Do you want to continue? Yes(y) or No(n).")
                if room == "y":
                    rooms -= 1
                    room_num += 1
                elif room == "n":
                    print("You have exited the dungeon.")
                    quit()
                else:
                    print("That is not a valid response, try again.")
            print("You have reached the end of the dungeon. Thanks for playing!")
            break
        elif dung_entry == "n":
            print("You did not enter the dungeon.")
            quit()
        else:
            print("That is not a valid response, try again.")


main()