import os
import glob
import re

for file in glob.glob('*.png'):
    file = re.sub('.png','', file)
    file2 = file[:-4]
    os.system('ffmpeg -y -i ' + file + '.png ' + file + '.jpg')
    os.system('rm -rf ' + file + '.png')