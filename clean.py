import os
import guessit
import shutil
import sys
import re
import uinput
from pathlib_revised import Path2


def move_me(abp, fon, fn):
    if not os.path.exists(fon):
        os.makedirs(fon)
    shutil.move(abp, fon + '/' + fn)


def MoveFolder1(dir, bannedDirs):
    Exists = []
    seen = set()
    rootDirs = [x for x in os.listdir(dir) if x not in bannedDirs]
    for File in rootDirs:
        if not os.path.isdir(os.path.join(dir, File)):
            Exists.append(File)
    for root, dirs, files in os.walk(dir):
        if root not in bannedDirs and dirs not in bannedDirs:
            for file in files:
                if file not in seen and file not in Exists:
                    seen.add(file)
                    x = Path2(os.path.join(root, file))
                    y = Path2(os.path.join(dir, file))
                    shutil.move(x.extended_path, y.extended_path)
    for Dir in rootDirs:
        if Dir not in bannedDirs:
            if os.path.isdir(os.path.join(dir, Dir)):
                shutil.rmtree(os.path.join(dir, Dir))


def main():
    root_path = sys.argv[1]
    targ_path = sys.argv[2]
    if uinput.user_input() == 1:
        file_extensions = ['.avi', '.mp4', '.mkv', '.m4v', '.mov', '.wmv']  # Allowed video file extensions
        banned_extensions = ['.srt', '.jpg', '.torrent', '.gif', '.nfo', '.png', '.sfv']    # Banned file extensions

        ef = targ_path + '/' + 'Episodes'   # Path to the Episodes folder
        mf = targ_path + '/' + 'Movies'     # Path to the Movies folder
        sf = targ_path + '/' + 'Songs'      # Path to the Songs folder
        df = targ_path + '/' + 'Documents'  # Path to the Documents folder
        pf = targ_path + '/' + 'Programs'   # Path to the Programs folder
        rf = targ_path + '/' + 'Random'     # Path to the Random folder
        zf = targ_path + '/' + 'Zipped'     # Path to the Zipped folder

        sortedDirs = [ef, mf, sf, df, pf, rf, zf]
        MoveFolder1(root_path, sortedDirs)

        title = ''                          # Title of the file
        filetype = ''                       # Filetype
        season = ''                         # Season of episode
        episode = ''                        # Number of episode

        for filename in os.listdir(root_path):
            abs_path = root_path + '/' + filename
            if not os.path.isdir(abs_path):
                if os.path.splitext(abs_path)[-1].lower() in file_extensions:
                    movie_info = guessit.guessit(filename)
                    for key, val in movie_info.items():
                        if key == 'title':
                            title = str(val)
                        if key == 'type':
                            filetype = str(val)
                        if key == 'season':
                            season = str(val)
                        if key == 'episode':
                            episode = str(val)

                    if title != '' and season != '' and filetype == 'episode':
                        if not os.path.exists(ef):
                            os.makedirs(ef)
                        if not os.path.exists(ef + '/' + title.title()):
                            os.makedirs(ef + '/' + title.title())
                        if not os.path.exists(ef + '/' + title.title() + '/' + 'Season ' + season):
                            os.makedirs(ef + '/' + title.title() + '/' + 'Season ' + season)
                            shutil.move(abs_path, ef + '/' + title.title() + '/' + 'Season ' + season)
                        else:
                            shutil.move(abs_path, ef + '/' + title.title() + '/' + 'Season ' + season)

                        title = ''
                        filetype = ''
                        season = ''

                    elif title != '' and season == '' and episode != '' and filetype == 'episode':
                        if not os.path.exists(ef):
                            os.makedirs(ef)
                        if not os.path.exists(ef + '/' + title.title()):
                            os.makedirs(ef + '/' + title.title())
                        shutil.move(abs_path, ef + '/' + title.title())

                        title = ''
                        filetype = ''
                        season = ''

                    elif title != '' and filetype == 'movie':
                        if not os.path.exists(mf):
                            os.makedirs(mf)
                        if not os.path.exists(mf + '/' + title.title()):
                            os.makedirs(mf + '/' + title.title())
                            shutil.move(abs_path, mf + '/' + title.title())
                        else:
                            shutil.move(abs_path, mf + '/' + title.title())

                        title = ''
                        filetype = ''
                        season = ''

                elif re.search(".r\d+|rar|part", filename):
                    mi = guessit.guessit(filename)
                    if not os.path.exists(zf):
                        os.makedirs(zf)
                    for key, val in mi.items():
                        if key == 'title':
                            file_name = str(val)
                            fpath = zf + '/' + file_name.split()[0]
                            move_me(abs_path, fpath, filename)
                            break

                elif os.path.splitext(abs_path)[-1].lower() in banned_extensions:
                    os.remove(abs_path)
                elif os.path.splitext(abs_path)[-1].lower() == '.mp3':
                    move_me(abs_path, sf, filename)
                elif os.path.splitext(abs_path)[-1].lower() == '.exe':
                    move_me(abs_path, pf, filename)
                elif os.path.splitext(abs_path)[-1].lower() == '.txt':
                    move_me(abs_path, df, filename)
        for file in os.listdir(root_path):
            abs_path = root_path + '/' + file
            if not os.path.isdir(abs_path):
                move_me(abs_path, rf, file)

        print('Sorting complete!')

if __name__ == '__main__':
    main()
