import os
import guessit
import shutil


def sort_files(root_path):
    file_extensions = ['.avi', '.mp4', '.mkv']

    ef = root_path + '/' + 'Episodes'  # Path to the Episodes folder
    mf = root_path + '/' + 'Movies'    # Path to the Movies folder

    # Make folders if non existent
    if not os.path.exists(ef):
        os.makedirs(ef)
    if not os.path.exists(mf):
        os.makedirs(mf)

    title = ''
    filetype = ''

    for filename in os.listdir(root_path):
        if not os.path.isdir(root_path + '/' + filename):
            if os.path.splitext(root_path + filename)[-1].lower() in file_extensions:
                    movie_info = guessit.guessit(filename)
                    for x, y in movie_info.items():
                        if x == 'title':
                            title = str(y)
                        if x == 'type':
                            filetype = str(y)

                        if title != '' and filetype == 'episode':
                            if not os.path.exists(ef + '/' + title.title()):
                                os.makedirs(ef + '/' + title.title())
                                shutil.move(root_path + '/' + filename, ef + '/' + title.title())
                            else:
                                shutil.move(root_path + '/' + filename, ef + '/' + title.title())
                            title = ''
                            filetype = ''
                        elif title != '' and filetype == 'movie':
                            if not os.path.exists((mf + '/' + title).title()):
                                os.makedirs(mf + '/' + title.title())
                                shutil.move(root_path + '/' + filename, mf + '/' + title.title())
                            else:
                                shutil.move(root_path + '/' + filename, mf + '/' + title.title())
                            title = ''
                            filetype = ''

sort_files('C:/ACCESS/mockdl')
