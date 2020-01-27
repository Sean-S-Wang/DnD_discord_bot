from DungeonMaster import DungeonMaster, yes_or_no
from argparse import ArgumentParser
import sys


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # Parse inputs
    parser = ArgumentParser(description='dnd game entrypoint', prog='run_game')

    parser.add_argument('-d', '--dm_name', dest='dm_name', required=True)
    parser.add_argument('-n', '--campaign_name', dest='campaign_name', required=False, default=None)
    parser.add_argument('-r', '--rule_set', dest='rule_set', required=False, default='Pathfinder')

    args, unknown = parser.parse_known_args(args)

    if unknown:
        print("Unknown input arguments: ")
        print(unknown)
        return

    dm1 = DungeonMaster(args.dm_name)
    # Create a new campaign
    if yes_or_no(r"Do you want to start a new campaign?"):
        dm1.create_campaign()
        dm1.resume_campaign()
    else:
        if yes_or_no("Do you want to load a old campaign?"):
            # Load a campaign
            dm1.load_campaign()
            # Resume the gameplay loop
            dm1.resume_campaign()
        else:
            pass
        print("There's nothing left do do...")

    print("Thank you for using the DnD Bot")


if __name__ == "__main__":
    main()