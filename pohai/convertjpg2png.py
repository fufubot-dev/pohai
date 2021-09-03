import os
import glob
import re

for file in glob.glob('*.jpg'):
    file = re.sub('.jpg','', file)
    file2 = file[:-4]
    os.system('ffmpeg -y -i ' + file + '.jpg ' + file + '.png')
    os.system('rm -rf ' + file + '.jpg')