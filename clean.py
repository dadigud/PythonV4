import os
from collections import defaultdict as D
import guessit
import shutil


# Main
def clean(dl, target):
    ef = dl + '/' + 'Episodes'  # Path to the Episodes folder
    df = dl + '/' + 'Movies'    # Path to the Movies folder

    # Make folders if non existent
    if not os.path.exists(ef):
        os.makedirs(ef)
    if not os.path.exists(df):
        os.makedirs(df)

    # List of available file extensions
    # TODO: Read from file ( be able to add and remove allowed extensions)
    file_extensions = ['.avi', '.mp4', '.mkv']

    # Dictionary of movies and folders
    movies_dict = D(list)
    folder_dict = D(list)

    movie_list = []

    # TODO: Clean up
    for filename in os.listdir(dl):
        if os.path.isdir(dl + '/' + filename):
            if filename[0].isalpha():
                folder_dict[filename[0].lower()].append(filename)
            else:
                folder_dict[filename[0]].append(filename)
        else:
            if os.path.splitext(dl + filename)[-1].lower() in file_extensions:
                if filename[0].isalpha():
                    shutil.move(dl + '/' + filename, ef)
                    movie_list.append(guessit.guessit(filename))

    # Priting info for each movie
    # TODO: Make a folder with each filename if non existent
    # TODO: Move the right file into the created/existent folder

    #for i in my_list:
       # for x, y in i.items():
           # print(str(x).title(), ':', str(y).title())
