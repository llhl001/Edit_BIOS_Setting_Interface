import os
import subprocess
from os import listdir
from os.path import isfile, join	

password = 'password'

def getCmd(fileType) :
	if (fileType == "_bios.txt") :
		return "s"
	else :
		return "bt"

def chooseFile(fileType) :
	# choose setting file in BIOSsetting folder
	# return the file name
	if (not showList(fileType)) :
		return "-1"

	folderPath = os.getcwd() + '/BIOSsetting/'
	fileList = listdir(folderPath)

	while (True) :
		fileNum = int(input("Please input file number (exit : 0) : "))
		if (fileNum == 0) :
			return "-1"
		if (fileNum <= 0 or fileNum > len(fileList)) :
			print("<<File number error>>")
		else :
			i = 0
			for myFile in fileList :
				fullPath = join(folderPath, myFile)
				if (isfile(fullPath) and myFile.find(fileType) != -1) :
					# count file number
					i += 1
				if (i == fileNum) :
					# find the need file and return the file name
					print("Choose : ("+str(fileNum)+") "+myFile)
					print('')
					return myFile
			print("<<No such file>>")

			
def showList(fileType) :
	# show all setting files in BIOSsetting folder
	# if there are no setting file, return False
	# else return True

	print('')
	#check folder exists OR empty OR not
	folderPath = os.getcwd() + '/BIOSsetting/'
	if (not os.path.isdir(folderPath)) :
		print("no any setting file exist")
		return False

	fileList = listdir(folderPath)
	i = 0

	for myFile in fileList :
		fullPath = join(folderPath, myFile)
		if (isfile(fullPath) and myFile.find(fileType) != -1) :
			i += 1
			print("("+str(i)+") "+myFile)
	if (i == 0) :
		print("no any setting file exist")
		return False

	print('')
	return True

	
def showOrder() :
	# input a boot order and modify setting file
	# finally import new setting file into BIOS

	process = subprocess.Popen("echo "+password+" |sudo -S ./h2ouve-lx64 -gbt temp.txt;exec", shell=True)
	process.communicate()
	# export current order

	print('')
	print("<<Current Boot Order>>")

	list = ["FLOPPY", "CDROM", "HARDDISK", "USB", "OTHER_DRIVER"]
	i = 0

	with open("temp.txt", 'r') as f_in :
		find = False		# if find Boot Type, find = True
		for line in f_in :	# find setting name
			if   (not find) :
				if (line == "========== H2OUVE Boot Type ==========\n") :
					find = True
			else :
				if   (line == "=====================================\n") :
					# replaceing end, write the thing left into output file
					break
				else :
					for option in list :
						if (line.find(option) != -1) :
							i+=1
							print("("+str(i)+") "+option)
							break


def save(fileType) :
	# input a file name and save current setting in the specific folder

	folderPath = os.getcwd() + '/BIOSsetting/'
	cmd = getCmd(fileType)
	# check file exists or not
	while(True) :
		fileName = input('Please input file name (exit : 0): ')
		if (fileName == "0") :
			return
		if (os.path.isfile(folderPath+fileName+'_bios.txt')) :
			# have to input a new name
			print("File already exists !")
		else :	# file not exist, this name can be used
			break

	# if save setting file's folder not exists, create new folder "BIOSsetting"
	try :	
		if (not os.path.isdir(folderPath)) :
			os.makedirs(folderPath)
	except PermissionError:
		print("permission denied")

	filePath = folderPath + fileName + fileType

	# save current BIOS setting
	process = subprocess.Popen("echo "+password+" |sudo -S ./h2ouve-lx64 -g"+cmd+" "+filePath+";exec", shell=True)		
	process.communicate()
	


def bootType() :
	# input a boot type selection and modify setting file
	# finally import new setting file to BIOS
	while (True) :
		print('')
		print("<<Boot Type List>>")
		print("(1) Dual Boot Type  (Default)")
		print("(2) Legacy Boot Type")
		print("(3) UEFI Boot Type")
		print('')
		typeNum = input("Please enter type number (exit : 0) : ")
		print('')
		if (typeNum == "0") :
			return
		if (typeNum == "1") :
			typeName = "Dual Boot Type"
			break
		elif (typeNum == "2") :
			typeName = "Legacy Boot Type"
			break
		elif (typeNum == "3") :
			typeName = "UEFI Boot Type"
			break
		else :
			print("type number error")

	process = subprocess.Popen("echo "+password+" |sudo -S ./h2ouve-lx64 -gs test.txt;exec", shell=True)
	process.communicate()
	# export current BIOS setting

	with open("test.txt", 'r') as f_in, open("result.txt", 'w') as f_out:
		find = False		# if find Boot Type, find = True
		isReplace = False	# if all selection are replaced finish, isReplace = True
		for line in f_in :	# find setting name
			output = line
			if   (not find and not isReplace) :
				if (line == "(0x79, 1, 0xB07398139D839CF0, 0xEA) Boot Type\n") :
					find = True
			elif (find and not isReplace) :
				if   (not len(line) or line.startswith('#') or line.startswith('\n')) :
					# replaceing end, write the thing left into output file
					isReplace = True
				elif (line.find(typeName) != -1) :           # find selection
					if (line.find('[ ]') != -1) :        # [ ] -> [*]
						output = line.replace('[ ]','[*]')	
				elif (line.find(typeName) == -1) :           # didn't find
					if (line.find('[*]') != -1) :        # [*] -> [ ]
						output = line.replace('[*]','[ ]')
				else :
					isReplace = True

			f_out.write(output)

	process = subprocess.Popen("echo "+password+" |sudo -S ./h2ouve-lx64 -ss result.txt;exec", shell=True)
	# import new BIOS setting
	process.communicate()
	process = subprocess.Popen("echo "+password+" |sudo rm -f test.txt;sudo rm -f result.txt", shell=True)


def bootOrder() :
	
	showOrder()
	list = ["FLOPPY", "CDROM", "HARDDISK", "USB", "OTHER_DRIVER"]
	inputNumList = []
	while(True) :
		i = 0
		inputNumList.clear()
		print('')
		print("Please enter your prefer order (range : 1~5) ")
		print("<< exit : 0 >>")
		with open("temp.txt", 'r') as f_in, open("result.txt", 'w') as f_out:
			find = False		# if find Boot Type, find = True
			isReplace = False	# if all selection are replaced finish, isReplace = True
			for line in f_in :	# find setting name
				output = line
				if   (not find and not isReplace) :
					if (line == "========== H2OUVE Boot Type ==========\n") :
						find = True
				elif (find and not isReplace) :
					if   (line == "=====================================\n") :
					# replaceing end, write the thing left into output file
						isReplace = True
					else :
						for option in list :
							if (line.find(option) != -1) :
								num = int(input("("+str(i+1)+") "+option+" : "))
								if (num == 0) :
									return
								inputNumList.append(num)
								num-=1
								output = line.replace('['+str(i)+']','['+str(num)+']')
								i+=1
								break

				f_out.write(output)
		if (inputCorrectNum(inputNumList)) :
			break
		print('')
		print("Input number Error.")

	process = subprocess.Popen("echo "+password+" |sudo -S ./h2ouve-lx64 -sbt result.txt;exec", shell=True)
	# import new BIOS setting
	process.communicate()
	process = subprocess.Popen("echo "+password+" |sudo rm -f temp.txt;sudo rm -f result.txt", shell=True)

def inputCorrectNum(inputList) :
	numList = [1, 2, 3, 4, 5]
	
	for inputNum in inputList :
		find = False
		for num in numList :
			if (inputNum == num) :
				find = True
				numList.remove(num)
				break
		if (not find) :
			return False

	return True

def change(fileName, fileType) :	
	cmd = getCmd(fileType)
	folderPath = os.getcwd() + '/BIOSsetting/'
	fullPath = join(folderPath, fileName)					
	process = subprocess.Popen("echo "+password+" |sudo -S ./h2ouve-lx64 -s"+cmd+" "+fullPath+";exec", shell=True)
	process.communicate()
	print('')


command = -1

while(command != "0") :
	print('')
	print('')
	print("*******************H2OUVE Tool********************")
	print("***  0. Exit                                   ***")
	print("--------------- BIOS Setting (all) ---------------")
	print("***  1. Show BIOS Setting file List            ***")
	print("***  2. Export Current BIOS Setting            ***")
	print("***  3. Import BIOS Setting                    ***")
	print("--------------- Boot Order Setting ---------------")
	print("***  4. Show Boot Order Setting file List      ***")
	print("***  5. Show Current Boot Order                ***")
	print("***  6. Export Current Boot Order Setting      ***")
	print("***  7. Import Boot Order Setting              ***")
	print("--------------- Change BIOS Setting --------------")
	print("***  8. Change Boot Type                       ***")
	print("***  9. Change Legacy Boot Order               ***")
	print("**************************************************")
	print('')
	command = input("Input a choice : ")
	
	if   (command == "0") :
		print("quit")
	elif (command == "1") :
		showList("_bios.txt")
	elif (command == "2") :
		save("_bios.txt")
	elif (command == "3") :
		fileName = chooseFile("_bios.txt")
		if (fileName != "-1") :		# find the need file
			change(fileName, "_bios.txt")
	elif (command == "4") :
		showList("_order.txt")					
	elif (command == "5") :	
		showOrder()	
	elif (command == "6") :
		save("_order.txt")
	elif (command == "7") :
		fileName = chooseFile("_order.txt")
		if (fileName != "-1") :		# find the need file
			change(fileName, "_order.txt")
	elif (command == "8") :
		bootType()
	elif (command == "9") :
		bootOrder()
	else :
		print("Please enter again.")



