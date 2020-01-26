from DungeonMaster import DungeonMaster
from argparse import ArgumentParser
import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # Parse inputs
    parser = ArgumentParser(description='dnd game entrypoint', prog='run_game')

    parser.add_argument('-n', '--campaign_name', dest='campaign_name', required=True)
    parser.add_argument('-d', '--dm_name', dest='dm_name', required=True)
    parser.add_argument('-r', '--rule_set', dest='rule_set', required=False, default='Pathfinder')

    args, unknown = parser.parse_known_args(args)

    if unknown:
        print("Unknown input arguments: ")
        print(unknown)
        return

    print("Welcome to " + args.campaign_name + ". Your DM is " + args.dm_name)

    dm1 = DungeonMaster(args.dm_name)

    # Initiative Roll
    print(dm1.roll_dice([6, 10, 20]))

    # Add character to game
    dm1.add_character_to_database("Debbie", "Mage", strength=10, dexterity=10, intellect=10)
    dm1.check_character_database("Debbie")
    dm1.add_character_to_database("George", "Warrior", strength=20, dexterity=10, intellect=0)
    dm1.check_character_database("George")


if __name__ == "__main__":
    main()