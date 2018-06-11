
'''
ProjectSync
Hardcoded sync for Nostromo project.

'''
import os
import shutil
import string
#-----------------------------------------------------------------------------
def FindFolders(dList):
	foundSubDirs = False
	subDirs = []
	for d in dList:
		if os.path.exists(d) and os.path.isdir(d):
			
			srcAbsPaths.append(d)
			trgAbsPaths.append(d.replace(sourceRoot, targetRoot, 1))

			if len(os.listdir(d)) > 0:
				foundSubDirs = True
			for s in os.listdir(d):
				sFull = os.path.join(d,s)
				if os.path.isdir(sFull) and s not in excludeFolders:
					subDirs.append(sFull)

	if foundSubDirs == True:
		FindFolders(subDirs)

#-----------------------------------------------------------------------------
def CreateFolders():
	for t in trgAbsPaths:
		if(os.path.exists(t)):
			continue
		print("Creating New Folder : " + t)
		os.mkdir(t)
#-----------------------------------------------------------------------------
def CopyFiles():
	for root, dirs, files in os.walk(sourceRoot):
		for f in files:
			srcFile = os.path.abspath(os.path.join(root,f))
			srcOnlyPath, fname = os.path.split(srcFile)
			trgOnlyPath = srcOnlyPath.replace(sourceRoot, targetRoot, 1)
			trgFile = os.path.join(trgOnlyPath, fname)

			if(os.path.isfile(trgFile)):
				trgTime = os.path.getmtime(trgFile)
				srcTime = os.path.getmtime(srcFile)
				if(srcTime > trgTime):
					print("Copying Modified File : " + srcFile)
					shutil.copy(srcFile, trgFile)
			else:
				if(os.path.exists(trgOnlyPath)):
					print("Copying New File : " + srcFile)
					shutil.copy(srcFile, trgFile)

		#print(filepath)
#-----------------------------------------------------------------------------
def syncNostromo(sourceRoot, targetRoot):
	if not os.path.exists(sourceRoot) or not os.path.exists(targetRoot):
		return
	print("Both folders exists")
	folderList = []
	folderList.append(sourceRoot)
	FindFolders(folderList)
	CreateFolders()
	CopyFiles()

#-----------------------------------------------------------------------------
# -- START HERE --
#-----------------------------------------------------------------------------
print("Assets sync started...")
projectName = "003_Nostromo"

sourceRoot = os.path.join("d:\\work\\Unity_Projects\\",projectName)
#sourceRoot = os.path.join(sourceRoot, "Assets")

targetRoot = os.path.join("d:\\cloud\\Google Drive\\Projects\\", projectName)
#targetRoot = os.path.join(targetRoot, "Assets")
if(not os.path.exists(targetRoot)):
	os.makedirs(targetRoot)

excludeFolders = ["Library", "ProjectSettings", "Temp"]
filePaths = []
srcAbsPaths = []
trgAbsPaths = []

syncNostromo(sourceRoot, targetRoot)

print("Assets sync finished...")
