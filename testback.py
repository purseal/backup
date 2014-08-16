#!/usr/bin/env python

import os
import shutil

testdir = '/home/maria/prog/backup/testdir'
testdir1 = '/home/maria/prog/backup/testdir1'
#testarch = os.system ('$(ls -t *tgz | head -1)')
#print (testarch)

def prepare():
        os.mkdir('testdir')
        testfile = open ('testdir/testfile', 'w')
        testfile.write('some text')
        testfile.close
        print ('prepare done')

def clear():
        if os.path.exists(testdir):
                shutil.rmtree(testdir)
        shutil.rmtree(testdir1)
        #os.remove(testarch)#   я не могу понять, как можно удалить созданный архив. Еси удаять его по имени, то нужно откуда-то взять это имя, сдуать это у меня не получается. Я пыталась удалить просто последний созданный архив (ниже), но в 23 строке testarch принимает значение 32512, а не нужное мне имя последнего файла
        testarch = os.system('$(ls -t *.tgz | head -1)')
        print(testarch)
        os.remove (testarch)
        print ('clear done')

def testcase():
        os.system(r'/home/maria/prog/backup/back.py -c testdir')
        shutil.move(testdir, testdir1)
        os.system(r'/home/maria/prog/backup/back.py -x $(ls -t *.tgz | head -1)')
        print ('testcase done')
        if filecmp.cmpfiles(tesdir, testdir1):
                print('test case 1 - [ok]')
        else:
                print('test case 2 - [fail]')
        shutil.rmtree(testdir)

prepare()
testcase()
clear()
