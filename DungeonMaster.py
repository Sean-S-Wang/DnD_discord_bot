import os
import numpy as np
import json
from datetime import datetime
from pathlib import Path


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


class DungeonMaster:

    def __init__(self, name, character_class='Dungeon Master'):
        self.character_dictionary = {}
        self.name = name
        self.character_dictionary[name] = CharacterDatabase(name, character_class)
        self.log = []
        self.campaign = None

    @staticmethod
    def roll_dice(dice_in_roll=[6]):
        results_of_roll = np.zeros(dice_in_roll.__len__())
        for current_roll, number_of_sides_on_dice in enumerate(dice_in_roll):
            results_of_roll[current_roll] = np.random.randint(1, high=np.max(number_of_sides_on_dice))
        return results_of_roll

    def check_character_database(self, character_name):
        print(self.character_dictionary[character_name].__dict__)

    def add_character_to_database(self, character_name=None, character_class=None, strength=0, dexterity=0, intellect=0):
        # TODO: Make it so it just asks for the information not already provided in the function call
        if character_name is None or character_class is None:
            print("What is the character's name?")
            character_name = input()

            while(self.check_if_character_in_db(character_name)):
                print("Character name already exists in database, please choose a different character name.")
                character_name = input()

            print("What is the character's class?")
            character_class = input()
            print("What is the character's strength?")
            strength = input()
            print("What is the character's dexterity?")
            dexterity = input()
            print("What is the character's intellect?")
            intellect = input()


        self.character_dictionary[character_name] = CharacterDatabase(character_name, character_class,
                                                                      strength, dexterity, intellect)

    def check_if_character_in_db(self, character_name):

        if character_name in self.character_dictionary.keys():
            return True
        else:
            return False




    def initiate_versus_roll(self, list_of_players, list_of_dice):

        for player_idx, player in enumerate(list_of_players):

            if not isinstance(player, CharacterDatabase):
                print("character is not an instance of Class CharacterDatabase")
                continue

            roll_result = self.roll_dice(dice_in_roll=list_of_dice)
            player_name = player.character_name

            # print("The roll result of " + str(player_name) + " is " + roll_result)
            print(player_name, roll_result)

    def add_note(self, note):
        self.log.append(note)

    def create_campaign(self):
        print("What is the name of this campaign?")
        campaign_name = input()
        self.campaign = Campaign(campaign_name)

    def load_campaign(self):
        # TODO: make this load a campaign from a DB or json or something
        # Just creates a default campaign for now
        self.campaign = Campaign("The Lord of the Rings")
        self.log = ["Gandalf is OP", "Left off at the mines of Moria"]
        self.add_character_to_database(character_name="Debbie", character_class="DaZhu", strength=30, dexterity=0, intellect=5000)
        self.add_character_to_database(character_name="Sean", character_class="Husbando", strength=10, dexterity=10, intellect=0)

    def resume_campaign(self):
        dm_command = None
        while dm_command is not "end campaign":
            print("What does the DM want to do?")
            dm_command = input()
            if dm_command.lower() == "roll for initiative":
                print(self.roll_dice(dice_in_roll=[20]))
            elif dm_command.lower() == "initiate combat":
                # TODO: initiate versus roll
                pass
            elif dm_command.lower() == "add character":
                self.add_character_to_database()
            elif dm_command.lower() == "end campaign":
                self.end_campaign()
                break
            elif dm_command.lower() == "check character":
                print("what is the character's name?")
                name = input()
                try:
                    self.check_character_database(name)
                except KeyError:
                    if yes_or_no("That character doesn't exist, do you want to add him?"):
                        self.add_character_to_database()
                    else:
                        pass
            elif dm_command.lower() == "versus roll":
                print("Who is participating in the roll?")
                names = input()
                names = names.split(' ')
                character_list = []
                fail_character_search = False
                for name in names:
                    if not (name in self.character_dictionary.keys()):
                        print(name + " does not exist!")
                        fail_character_search = True
                        break
                    character_list.append(self.character_dictionary[name])
                if fail_character_search is True:
                    continue
                print("What dice will be used in the roll?")
                dice = input()
                dice = dice.split(' ')
                try:
                    dice = [int(i) for i in dice]
                except ValueError:
                    print("Please use valid dice numbers!")
                    continue
                self.initiate_versus_roll(character_list, dice)
            else:
                print("the DM can't do that")

    def end_campaign(self):
        print("Saving campaign...")
        # TODO: Save campaign stuff to a database or text file or something
        self.campaign.last_saved = datetime.now()
        print("Campaign saved on: " + self.campaign.last_saved.strftime("%d/%m/%Y %H:%M:%S"))


class CharacterDatabase:

    def __init__(self, name, character_class, strength=0, dexterity=0, intellect=0):
        self.character_name = name
        self.character_class = character_class
        self.strength = strength
        self.dexterity = dexterity
        self.intellect = intellect


class Campaign:

    def __init__(self, campaign_name):
        self.date_created = datetime.now()
        self.campaign_name = campaign_name
        self.last_saved = datetime.now()
        self.campaign_filename = Path(campaign_name+".json")


def main():
    print("Testing")


if __name__ == "__main__":
    main()
