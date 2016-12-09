import os
import guessit
import shutil
import time
import re



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
                    shutil.move(os.path.join(root, file),os.path.join(dir,file))
    for Dir in rootDirs:
        if Dir not in bannedDirs:
            if os.path.isdir(os.path.join(dir, Dir)):
                shutil.rmtree(os.path.join(dir, Dir))


def sort_files(root_path):
    now = time.localtime()

    file_extensions = ['.avi', '.mp4', '.mkv', '.m4v', '.mov', '.wmv']  # Allowed video file extensions
    banned_extensions = ['.srt', '.jpg', '.torrent', '.gif', '.nfo']    # Banned file extensions

    ef = root_path + '/' + 'Episodes'   # Path to the Episodes folder
    mf = root_path + '/' + 'Movies'     # Path to the Movies folder
    sf = root_path + '/' + 'Songs'      # Path to the Songs folder
    df = root_path + '/' + 'Documents'  # Path to the Documents folder
    pf = root_path + '/' + 'Programs'   # Path to the Programs folder
    rf = root_path + '/' + 'Random'     # Path to the Random folder
    zf = root_path + '/' + 'Zipped'     # Path to the Zipped folder

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
    print(now, time.localtime())

pathAlex = 'C:/Users/alex/Documents/glósur/2.ar/python/verk4/downloads/'
sort_files(pathAlex)


#sort_files('/home/dadi15/Github/downloads')
