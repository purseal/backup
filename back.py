#!/usr/bin/env python

import sys
from datetime import datetime
import tarfile

now_time = datetime.now()
time_name = '%d_%d_%d_%d_%d_%d' % (now_time.year, now_time.month, now_time.day, now_time.hour, now_time.minute, now_time.second)
if sys.argv[1]=='-c':
        nametar = (sys.argv[2]) + '_' + (time_name) + '.tgz'
        tar=tarfile.open (nametar,"w:gz")
        tar.add (sys.argv[2])
        tar.close()
        print ('archive created')
elif sys.argv[1]=='-x':
        nametar='/home/prog/backup/'+sys.argv[2]
        tar = tarfile.open(sys.argv[2], 'r:gz')
        tar.extractall()
        tar.close()
        print ('archive extracted')
#elif sys.argv[2]=='-xl':
else:
        print('wrong parametr')
