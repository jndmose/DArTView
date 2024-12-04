from pathlib import Path
import os

home = Path.home().absolute().as_posix()
mypath = home + "/flask"
if not os.path.isdir(mypath):
    os.makedirs(mypath)


UPLOAD_FOLDER =mypath