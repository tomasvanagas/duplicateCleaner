#!/bin/python3
import json
import os

##############################################
# Clean other folder
##############################################
goodPhotos = {}
recoveredPhotos = {}

with open("samp.shasum", "r") as foto: # find ./originalFolder -type f -exec shasum -a256 {} \; | tee -a originalFolder.shasum
    for line in foto.readlines():
        line = line.replace("\n", "").replace("\r", "")
        fileHash = line.split(" ", 1)[0]
        filePath = line.split(" ", 1)[1].strip()

        if(fileHash not in goodPhotos):
            goodPhotos[fileHash] = []

        goodPhotos[fileHash].append(filePath)


with open("toReduce.shasum", "r") as foto: # find ./folderToClean -type f -exec shasum -a256 {} \; | tee -a folderToClean.shasum
    for line in foto.readlines():
        line = line.replace("\n", "").replace("\r", "")
        fileHash = line.split(" ", 1)[0]
        filePath = line.split(" ", 1)[1].strip()

        if(fileHash in goodPhotos):
            if(os.path.isfile(filePath)):
                print("REMOVING: " + fileHash + " " + filePath + " (GOOD PATH: " + str(goodPhotos[fileHash]) + ")")
                os.remove(filePath)
            else:
                print("Does not exist: " + filePath)
##############################################



'''
##############################################
# Clean same folder from duplicates
##############################################
allPhotos = {}
with open("hdd600.shasum", "r") as foto: # find ./folderToClean -type f -exec shasum -a256 {} \; | tee -a folderToClean.shasum
    for line in foto.readlines():
        line = line.replace("\n", "").replace("\r", "")
        fileHash = line.split(" ", 1)[0]
        filePath = line.split(" ", 1)[1].strip()

        
        if(fileHash not in allPhotos):
            allPhotos[fileHash] = []

        allPhotos[fileHash].append(filePath)

print(json.dumps(allPhotos, indent=4))

for key in allPhotos:
    count = len(allPhotos[key])
    if(count > 1):
        for i in range(count - 1):
            filePath = allPhotos[key][i]
            print("REMOVING: " + key + " " + filePath)
            os.remove(filePath)
##############################################            

'''



