import os
import shutil
from zipfile import ZipFile

#author: Milan Labus SD2B
#Date 18/04/2022

def createFolders(folderName):

#Creating the folder if it doesn't already exist
    try:
        os.mkdir(folderName)
        print("Folder Made: ", folderName)
    except FileExistsError:
        print("Folder already exists: ", folderName)

    #subfolders of the root directory
    subfolders=["working","backup"]

    #sub folders of the working subfolder
    workingNames=["pics","docs","movies"]

    #adding the subfolders to the folder created earlier
    for i in subfolders:
        os.mkdir(os.path.join(folderName, i)) #adding the subfolders

    #adding the subfolders of the working folder
    for i in workingNames:
        os.mkdir(os.path.join((folderName + "/working"), i))  #joinging the path and the list of subfolders

    #the files to add to docs
    files = ["CORONAVIRUS.txt,","DANGEROUS.txt","KEEPSAFE.tx", " STAYHOME.txt", "HYGIENE.txt)"]

    for i in files:
        with open((folderName + "/working/docs/"+i),"w") as f:  #passing location and w for write mode
            data = "Wear a mask when indoors"
            f.write(data)                                        #writting the data to the file

    #Creating the subfolders that will go into docs
    docsSubFolders = ["school","party"]

    #adding them into docs by passing the path
    for i in docsSubFolders:
        os.mkdir(os.path.join((folderName + "/working/docs"), i))

#passing the root directory as a parameter
def renameFunction(folderName):

    #checking if the folder exists
    isdir = os.path.isdir((folderName + "/working/docs"))
    if(isdir==False):
        print("error the file doesn't exist")
    else:
        #changing the working directory to docs
        os.chdir((folderName + "/working/docs"))
        allFiles = os.listdir()         #stores all of the files of the docs directory
        for i in allFiles:
            name, txt = os.path.splitext(i)     #splitting the name and txt
            name = name.lower()                 #changing name to lower
            txt = txt.upper()                 #chaning text to upper
            new_name = f"{name}{txt}"          #adding them back togheter
            os.rename(i, new_name)              #changing the old name with the new name


def zipFunction():
    files = os.listdir()

    for i in range(7):
        folderName = 'docs' + str(i + 1) + ".zip"
        with ZipFile(folderName, 'w') as zipObject:  #opening zip file object in w(write) mode
            for i in files:     #looping through files 7 times
                zipObject.write(i)
         #moving from the current folder to the backup folder
        shutil.move((os.getcwd() + "/" + folderName), (r"../../backup/" + folderName ))


#asking for the folder name and then calling all of the fucntions
folderName = input("Enter folder name: ")
createFolders(folderName)
renameFunction(folderName)
zipFunction()