import os
import guessit
import shutil
import time
import re
import move_files

# def move_me(abp, fon, fn):
#     if not os.path.exists(fon):
#         os.makedirs(fon)
#     shutil.move(abp, fon + '/' + fn)


def group_rar(root_path):
    for filename in os.listdir(root_path):
        aps = root_path + '/' + filename
        if re.search(".r\d+|rar", filename):
            fn = re.split(".r\d+|rar", filename)[0]
            fpath = root_path + '/' + fn

group_rar('/home/dadi15/Github/downloads')
