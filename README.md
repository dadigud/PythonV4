# Download clean-Up

This script is designed to categorize a download folder by moving the files to their appropriate directory. 

## Authors
* Alex Kári Ívarsson, alexi15@ru.is
* Daði Guðvarðarson, dadi15@ru.is
* Jón Heiðar Sigmundsson, jonhei15@ru.is

## Modules
The following modules are needed to run the script:
* guessit
* pathlib_revised

To install the required modules, run the following commands
```bash 
For windows
py -m pip install pathlib_revised
py -m pip install guessit
```

## Running the script
```bash
py clean.py [-h] [-s] [-allowed, -a] [-banned, -b] root destination
```
```bash
positional arguments:
  root          Folder to be sorted
  destination   Destination folder of sort

optional arguments:
  -h, --help    show this help message and exit
  -s            Sort and move files in root to destination
  -allowed, -a  Add or remove allowed movie file extensions
  -banned, -b   Add or remove banned movie file extensions
```

