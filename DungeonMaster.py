import os
import numpy as np


def roll_dice(dice_in_roll=[6]):
    results_of_roll = np.zeros(dice_in_roll.__len__())
    for current_roll, number_of_sides_on_dice in enumerate(dice_in_roll):
        results_of_roll[current_roll] = np.random.randint(1, high=np.max(number_of_sides_on_dice))
    return results_of_roll


class DungeonMaster:

    def __init__(self, name, character_class='Dungeon Master'):
        self.character_dictionary = {}
        self.name = name
        self.character_dictionary[name] = CharacterDatabase(name, character_class)

    def check_character_database(self, character_name):
        print(self.character_dictionary[character_name].__dict__)

    def add_character_to_database(self, character_name, character_class, strength=0, dexterity=0, intellect=0):
        self.character_dictionary[character_name] = CharacterDatabase(character_name, character_class,
                                                                      strength, dexterity, intellect)

    def initiate_versus_roll(self, list_of_players, list_of_dice):

        for player_idx, player in enumerate(list_of_players):

            if not isinstance(player, CharacterDatabase):
                print("character is not an instance of Class CharacterDatabase")
                continue

            roll_result = roll_dice(dice_in_roll=list_of_dice[player_idx])
            player_name = player.character_name

            # print("The roll result of " + str(player_name) + " is " + roll_result)
            print(player_name, roll_result)




class CharacterDatabase:

    def __init__(self, name, character_class, strength=0, dexterity=0, intellect=0):
        self.character_name = name
        self.character_class = character_class
        self.strength = strength
        self.dexterity = dexterity
        self.intellect = intellect


def main():
    print("Dungeon Master Demo")


    dungeon_master = DungeonMaster("Sean")
    player1 = CharacterDatabase("Debb", "mage", 10,12,13)
    player2 = CharacterDatabase("Poo", "witcher", 5,5,5)

    dungeon_master.initiate_versus_roll([player1, player2], [[6,10], [6]])



if __name__ == "__main__":
    main()
