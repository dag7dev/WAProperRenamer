# WAProperRenamer
Simple Python script which given 'Whatsapp Images' folder, or any folder you like, it renames each file
from Whatsapp format to a standard one, basing itself on last modified date.

Ex.  IMG-YYYYMMDD-WAXXXX => IMG-YYYYMMDD-HHMMSS

## How to use it
You will need Python3 to run this script.

**DO NOT** try to run it with Python2 because it won't work.


If you have ```git```, clone this repo with:

```git clone https://github.com/dag7dev/WAProperRenamer.git```

and place this script wherever you want.


If you don't have git, [click here](https://github.com/dag7dev/WAProperRenamer/archive/master.zip) and place this script wherever you want.

## Usage:
Write directly on Windows or Linux:
```
python3 WAProperRenamer.py
```
### Options:
```
-h: show this message
-p: changes the path. Ex WAProperRenamer.py -p C:\\Users\\User\\Desktop"
will scan the desktop folder

If no options are specified, it will be used the folder where the script is.
```
