# a simple script which renames every file from Whatsapp standard format into
# a proper name, using last modified date
# e.g. IMG-20200401-WA0057 => IMG-YYYYMMDD-HHMMSS

# dag7 - 2020

import datetime
import os
import sys
from os import listdir
from os.path import isfile, join


def whats_validator(full_file_name):
    # check if file is valid
    # IMG-YYYYMMDD-WAXXXX.very_long_extension
    filename_without_ext = full_file_name.split(".")[0]

    if len(filename_without_ext) != 19 or "WA" not in filename_without_ext:
        return False
    return True


def main(path, files):
    for name in files:
        if not whats_validator(name):
            print(name + " doesn't appear to be a photo named in Whatsapp standards.\n"
                         "Try to rename it in a Whatsapp photo " +
                  "format like IMG-YYYYMMDD-WAXXXX.ext\n"
                  "Skipping...\n")
            continue

        separator = ""

        splitted_one = name.split("-")
        splitted_two = splitted_one[2].split(".")

        del splitted_one[-1]

        timestamp = os.path.getmtime(path + os.path.sep + name)
        dt = str(datetime.datetime.fromtimestamp(timestamp).time())
        ending = separator.join(dt.split(":"))

        separator = "-"
        pieces_of_new_name = [f for f in splitted_one]
        pieces_of_new_name.append(ending)

        new_name = separator.join(pieces_of_new_name) + "." + splitted_two[1]

        print("Renaming " + path + os.path.sep + name + " in " + new_name + " ...\n")

        os.rename(path + os.path.sep + name, path + os.path.sep + new_name)

    print("!! DONE !! Thank you for having used this script. Have a nice day!\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            print("\nGiven Whatsapp Images folder, or any folder you like, it renames each file\n" +
                  "from Whatsapp format to a standard one, basing itself on last modified date.\n" +
                  "Ex.  IMG-YYYYMMDD-WAXXXX => IMG-YYYYMMDD-HHMMSS\n\n"
                  "Usage: \n"
                  "\t-h: show this message\n"
                  "\t-p: changes the path. Ex WAProperRenamer.py -p C:\\Users\\User\\Desktop"
                  "will scan the desktop folder\n"
                  "NOTE: if folder name contains spaces, remember to enclose the path with single quotes.\n"
                  "EX.WAProperRenamer.py -p 'My Folder'\n")
            exit(0)

        if sys.argv[1] == "-p":
            if(len(sys.argv) == 2):
                print("You haven't specified any folder! Make sure to specify a folder!\n")
                exit(1)

            path = os.curdir + os.path.sep + sys.argv[2]

            if not os.path.exists(path):
                print("This directory doesn't exist! Make sure you have specified the right directory!\n")
                exit(1)

            if not os.path.isdir(path):
                print("This doesn't seem to be a directory. Make sure you have specified a directory and not a file!\n")
                exit(1)
        else:
            print("Bad option!\nUsage: WAProperRenamer -h\n")
            exit(1)

    else:
        print("No options specified, current folder will be used.")
        print("Help: WAProperRenamer -h")
        print()
        input("Press CTRL+C to exit or press ENTER to continue...")

        path = os.curdir

    files = [f for f in listdir(path) if isfile(join(path, f))]

    separator = ""
    main(path, files)
