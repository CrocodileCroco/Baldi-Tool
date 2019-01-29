from shutil import copyfile
import os

nombrecopie = 4
actucopie = 0
baldifiles = []

replim = input("Name of replacement image (MUST END WITH .PNG OR OTHER) : ")
replem = input("What name the files you want to replace starts with? : ")

list_of_files = os.listdir(os.getcwd()) #list of files in the current directory
for each_file in list_of_files:
    if each_file.startswith(replem):  #since its all type str you can simply use startswith
        print(each_file)
        baldifiles.append(each_file)

print(baldifiles)
print("--------")


nombrecopie = len(baldifiles)

for i in baldifiles:
    copyfile(replim, i)

os.system("pause")



#while actucopie != nombrecopie:
#    actufichier = actucopie + 1
#    actucopi2 = "charles" + str(actufichier) + ".png"
#    copyfile('charlestemp.png', actucopi2)
#    print(str(actucopie))
#    actucopie = actucopie + 1