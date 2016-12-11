import os
import guessit
import shutil
import sys
import re
import uinput
from pathlib_revised import Path2
import argparse


# Moves file from A to B. If the folder
# does not exist, we create it
def move_me(abp, fon, fn):
    if not os.path.exists(fon):
        os.makedirs(fon)
    shutil.move(abp, fon + '/' + fn)


def sp(abs_path):
    return os.path.splitext(abs_path)[-1].lower()


# Moves everything from all sub-dirs into root
def move_from_folders(root_dir, banned_dirs):
    exists = []
    seen = set()
    root_dirs = [x for x in os.listdir(root_dir) if x not in banned_dirs]

    for File in root_dirs:
        if not os.path.isdir(os.path.join(root_dir, File)):
            exists.append(File)
    for root, dirs, files in os.walk(root_dir):
        if root not in banned_dirs and dirs not in banned_dirs:
            for file in files:
                if file not in seen and file not in exists:
                    seen.add(file)
                    x = Path2(os.path.join(root, file))
                    y = Path2(os.path.join(root_dir, file))
                    shutil.move(x.extended_path, y.extended_path)
    for Dir in root_dirs:
        if Dir not in banned_dirs:
            if os.path.isdir(os.path.join(root_dir, Dir)):
                shutil.rmtree(os.path.join(root_dir, Dir))


def main():
    root_path = sys.argv[1]     # Source path
    if not os.path.exists(root_path):
        sys.exit('Source path does not exist...')

    targ_path = sys.argv[2]     # Destination path
    if not os.path.exists(targ_path):
        os.makedirs(targ_path)


    #if uinput.user_input() == 1:
def mainsort(root_path, targ_path):
    # Source path
    print(root_path)
    if not os.path.exists(root_path):
        sys.exit('Source path does not exist...')

    # Destination path
    if not os.path.exists(targ_path):
        os.makedirs(targ_path)

    print('\nSorting...')

    db = uinput.get_from_db()
    file_extensions = db[0]               # Allowed video file extensions
    banned_extensions = db[1]             # Banned file extensions
    music_extensions = ['.mp3', '.flac', '.m4a', '.wav']    # Defined music extensions

    ef = targ_path + '/' + 'Episodes'   # Path to the Episodes folder
    mf = targ_path + '/' + 'Movies'     # Path to the Movies folder
    sf = targ_path + '/' + 'Songs'      # Path to the Songs folder
    df = targ_path + '/' + 'Documents'  # Path to the Documents folder
    pf = targ_path + '/' + 'Programs'   # Path to the Programs folder
    rf = targ_path + '/' + 'Random'     # Path to the Random folder
    zf = targ_path + '/' + 'Zipped'     # Path to the Zipped folder

    sorted_dirs = [ef, mf, sf, df, pf, rf, zf]
    move_from_folders(root_path, sorted_dirs)

    title = ''                          # Title of the file
    filetype = ''                       # Filetype
    season = ''                         # Season of episode
    episode = ''                        # Number of episode

    sorted_files = 0
    removed_files = 0

    for filename in os.listdir(root_path):
        abs_path = root_path + '/' + filename
        if not os.path.isdir(abs_path):
            if sp(abs_path) in file_extensions:
                movie_info = guessit.guessit(filename)

                # Collect file information
                for key, val in movie_info.items():
                    if key == 'title':
                        title = str(val)
                    if key == 'type':
                        filetype = str(val)
                    if key == 'season':
                        season = str(val)
                    if key == 'episode':
                        episode = str(val)

                # If we find an episode with a title and season number
                # it is added to the correct folder according to season number
                if title != '' and season != '' and filetype == 'episode':
                    if not os.path.exists(ef + '/' + title.title() + '/' + 'Season ' + season):
                        os.makedirs(ef + '/' + title.title() + '/' + 'Season ' + season)
                    shutil.move(abs_path, ef + '/' + title.title() + '/' + 'Season ' + season)
                    title, filename, season = '', '', ''
                    sorted_files += 1

                # If we find an episode with a title, an episode number but not a season
                # number, it is added to the root folder of the correct Tv show
                elif title != '' and season == '' and episode != '' and filetype == 'episode':
                    if not os.path.exists(ef + '/' + title.title()):
                        os.makedirs(ef + '/' + title.title())
                    shutil.move(abs_path, ef + '/' + title.title())
                    title, filename, season = '', '', ''
                    sorted_files += 1

                # If the file type has a title and is a movie
                # it is added to theMovies folder
                elif title != '' and filetype == 'movie':
                    if not os.path.exists(mf + '/' + title.title()):
                        os.makedirs(mf + '/' + title.title())
                    shutil.move(abs_path, mf + '/' + title.title())
                    title, filename, season = '', '', ''
                    sorted_files += 1

            # Here we sort out any zipped files. They are added to
            # the Zipped folder and grouped into their own folder
            elif re.search(".r\d+|rar|part", filename):
                mi = guessit.guessit(filename)
                for key, val in mi.items():
                    if key == 'title':
                        move_me(abs_path, zf + '/' + str(val).split()[0], filename)
                        sorted_files += 1
                        break

            # In this block of code, we sort out all other file extensions
            # that need to be taken care of. They are either removed or
            # Moved into their own folder
            elif sp(abs_path) in banned_extensions:
                os.remove(abs_path)
                removed_files += 1
            elif sp(abs_path) in music_extensions:
                move_me(abs_path, sf, filename)
                sorted_files += 1
            elif sp(abs_path) == '.exe':
                move_me(abs_path, pf, filename)
                sorted_files += 1
            elif sp(abs_path) == '.txt':
                move_me(abs_path, df, filename)
                sorted_files += 1

    for file in os.listdir(root_path):
        abs_path = root_path + '/' + file
        if not os.path.isdir(abs_path):
            move_me(abs_path, rf, file)
            sorted_files += 1

    print('Sorting complete!\n\nSorted ' + str(sorted_files) + ' files')

def addremoveallowed(root, dest):
    uinput.user_input('2')

def addremovebanned(root, dest):
    uinput.user_input('3')

parser = argparse.ArgumentParser(description='Categories a folder of episodes and movies to their '
                                             'appropriate directory.')
parser.add_argument('root', metavar='root',
                   help='Folder to be sorted')
parser.add_argument('dest', metavar='destination',
                   help='Destination folder of sort')
parser.add_argument('-s', dest='accumulate', action='store_const',
                   const=mainsort, default=mainsort,
                   help='Sort and move files in root to destination')

parser.add_argument('-allowed, -a', dest='accumulate', action='store_const',
                   const=addremoveallowed, default=mainsort,
                   help='Add or remove allowed movie file extensions')

parser.add_argument('-banned, -b', dest='accumulate', action='store_const',
                   const=addremovebanned, default=mainsort,
                   help='Add or remove banned movie file extensions')

args = parser.parse_args()
args.accumulate(args.root, args.dest)

# if __name__ == '__main__':
#     main()
