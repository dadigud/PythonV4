import os
import guessit
import shutil


def move_me(abp, path, fon, fn):
    if not os.path.exists(path + '/' + 'Songs'):
        os.makedirs(path + '/' + 'Songs')
    shutil.move(abp, path + '/' + 'Songs' + '/' + fn)


def sort_files(root_path):
    file_extensions = ['.avi', '.mp4', '.mkv', '.m4v']
    banned_extensions = ['.srt', '.jpg', '.torrent']
    ef = root_path + '/' + 'Episodes'  # Path to the Episodes folder
    mf = root_path + '/' + 'Movies'    # Path to the Movies folder

    # Make folders if non existent

    title = ''
    filetype = ''

    for filename in os.listdir(root_path):
        abs_path = root_path + '/' + filename
        if not os.path.isdir(abs_path):
            if os.path.splitext(abs_path)[-1].lower() in file_extensions:
                movie_info = guessit.guessit(filename)
                for x, y in movie_info.items():
                    if x == 'title':
                        title = str(y)
                    if x == 'type':
                        filetype = str(y)

                    if title != '' and filetype == 'episode':
                        if not os.path.exists(ef):
                            os.makedirs(ef)
                        if not os.path.exists(ef + '/' + title.title()):
                            os.makedirs(ef + '/' + title.title())
                            shutil.move(abs_path, ef + '/' + title.title())
                        else:
                            shutil.move(abs_path, ef + '/' + title.title())
                        title = ''
                        filetype = ''
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
            elif os.path.splitext(abs_path)[-1].lower() in banned_extensions:
                os.remove(abs_path)
            elif os.path.splitext(abs_path)[-1].lower() == '.mp3':
                move_me(abs_path, root_path, 'Songs', filename)
            elif os.path.splitext(abs_path)[-1].lower() == '.exe':
                move_me(abs_path, root_path, 'Programs', filename)
            elif os.path.splitext(abs_path)[-1].lower() == '.txt':
                move_me(abs_path, root_path, 'Documents', filename)


sort_files('C:/Users/dadig/Downloads')
