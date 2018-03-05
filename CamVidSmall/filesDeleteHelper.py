# -*- coding: utf-8 -*-

# a script to help in deleting relevant files in label folder, given that I 
# manually delete some files in the main folder

import glob, os
import numpy as np


def deleteExtraFilesInLabelFolder(mainFolder, labelFolder):
    ## main folder
    # go into the main folder
    os.chdir(mainFolder)
    # finds files in this folder
    filesCol = glob.glob("*.png")
    ## number of files in the main folder
    numFilesCol = len(filesCol)
    
    # go to parent folder
    os.chdir("..")
    
    ## label folder - where we want to find files that are not in main folder and delete them
    os.chdir(labelFolder)
    filesLab = glob.glob("*.png")
    
    # create a hashmap to check the presense of the file in the main folder
    ## number of files in the label folder
    numFilesLab = len(filesLab)
    hashMapLab = np.full(numFilesLab, False)
    
    
    ## go through the files in Label folder and check for each file if it exists in 
    # the main folder - if it does the record in hashMapLab as True, otherwise record
    #  as False
    numFilesPreserved = 0
    for i in range(numFilesLab):
        
        # first get only the file name
        cf = filesLab[i].split(".")[0]
        
        # then remove the appending _L i.e. last two chars
        currentFile = cf[0:-2]
        
        print("Current file: ", currentFile)
        
        # now check this file name with each file in the main folder
        for j in range(numFilesCol):
            currentMainFile = filesCol[j].split(".")[0]
            
            if(currentFile == currentMainFile):
                print("Checking if ", currentFile, " == ", currentMainFile, " ---> ", currentFile == currentMainFile )
                numFilesPreserved = numFilesPreserved + 1
                hashMapLab[i] = True
                break
            
        if(hashMapLab[i] == False):
            print("Deleting...", filesLab[i])
            os.remove(filesLab[i])
            print("...done")
    
    assert(numFilesPreserved == numFilesCol), "Error: something is wrong - #files in main folder != #files selected in label folder"
    
    os.chdir("..")
    return
    
deleteExtraFilesInLabelFolder("test", "test_labels")
deleteExtraFilesInLabelFolder("train", "train_labels")
deleteExtraFilesInLabelFolder("val", "val_labels")

