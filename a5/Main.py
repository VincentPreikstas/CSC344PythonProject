import os
import re
import subprocess

def cParser(fileName):

    #READ FROM FILE
    workingVariable = ''
    lineCounter = 0
    cFile = open(fileName,"r")
    for line in cFile:
        lineCounter += 1
        if "//" in line:
            jaja = 0
        else:
            workingVariable = workingVariable + line + "\n"
            workingVariable = workingVariable.replace("\r", "")

    pattern = re.compile("([a-zA-Z\d_]+)", re.M | re.X)
    out = pattern.findall(workingVariable)
    final = []
    for i in out:
        if i not in final:
            final.append(i)
    final.sort()

    finalFiltered = []
    for i in final:
        if i.isdigit():
            jaja = 1
        else:
            finalFiltered.append(i)

    final = finalFiltered
    #print(finalFiltered)
    #print(fileName)
    #print(final)
    #print(lineCounter)

    #WRITE TO HTTP FILE
    writeFile = open("summary_a1.html", "w")

    string = """<!DOCTYPE html>
    <html>
    <body>
    <h1>C Project HTML!</h1>
    """
    writeFile.write(string)

    string = '<a href="main.c"> main.c </a> \n'
    writeFile.write(string)

    string = "<p> The Number of lines in the file is: " + str(lineCounter) + "</p> \n"
    writeFile.write(string)

    string = "<p> Alphabetical list of identifiers: <br/> \n"

    for term in final:
        string = string + term + "<br/> \n"

    string = string + "</p> \n"
    #print(string)

    writeFile.write(string)

    string = """</body>
    </html>
    """
    writeFile.write(string)

    writeFile.close()
    cFile.close()

def clojureParser(fileName):
    # READ FROM FILE
    workingVariable = ''
    lineCounter = 0
    cFile = open(fileName, "r")
    for line in cFile:
        lineCounter += 1
        if "(comment" in line:
            jaja = 0
        else:
            workingVariable = workingVariable + line + "\n"
            workingVariable = workingVariable.replace("\r", "")

    pattern = re.compile("([a-zA-Z\d_]+)", re.M | re.X)
    out = pattern.findall(workingVariable)
    final = []
    for i in out:
        if i not in final:
            final.append(i)
    final.sort()

    finalFiltered = []
    for i in final:
        if i.isdigit():
            jaja = 1
        else:
            finalFiltered.append(i)

    final = finalFiltered
    #print(fileName)
    #print(final)
    #print(lineCounter)

    # WRITE TO HTTP FILE
    writeFile = open("summary_a2.html", "w")

    string = """<!DOCTYPE html>
        <html>
        <body>
        <h1>Clojure Project HTML!</h1>
        """
    writeFile.write(string)

    string = '<a href="mainProject.clj"> mainProject.clj </a> \n'
    writeFile.write(string)

    string = "<p> The Number of lines in the file is: " + str(lineCounter) + "</p> \n"
    writeFile.write(string)

    string = "<p> Alphabetical list of identifiers: <br/> \n"

    for term in final:
        string = string + term + "<br/> \n"

    string = string + "</p> \n"
    # print(string)

    writeFile.write(string)

    string = """</body>
        </html>
        """
    writeFile.write(string)

    writeFile.close()
    cFile.close()

def scalaParser(fileName):
    # READ FROM FILE
    workingVariable = ''
    lineCounter = 0
    cFile = open(fileName, "r")
    for line in cFile:
        lineCounter += 1
        if "//" in line:
            jaja = 0
        else:
            workingVariable = workingVariable + line + "\n"
            workingVariable = workingVariable.replace("\r", "")

    pattern = re.compile("([a-zA-Z\d-]+)", re.M | re.X)
    out = pattern.findall(workingVariable)
    final = []
    for i in out:
        if i not in final:
            final.append(i)
    final.sort()

    finalFiltered = []
    for i in final:
        if i.isdigit():
            jaja = 1
        else:
            finalFiltered.append(i)

    final = finalFiltered
    # print(fileName)
    # print(final)
    # print(lineCounter)

    # WRITE TO HTTP FILE
    writeFile = open("summary_a3.html", "w")

    string = """<!DOCTYPE html>
            <html>
            <body>
            <h1>Scala Project HTML!</h1>
            """
    writeFile.write(string)

    string = '<a href="Main.scala"> Main.scala </a> \n'
    writeFile.write(string)

    string = "<p> The Number of lines in the file is: " + str(lineCounter) + "</p> \n"
    writeFile.write(string)

    string = "<p> Alphabetical list of identifiers: <br/> \n"

    for term in final:
        string = string + term + "<br/> \n"

    string = string + "</p> \n"
    # print(string)

    writeFile.write(string)

    string = """</body>
            </html>
            """
    writeFile.write(string)

    writeFile.close()
    cFile.close()

def prologParser(fileName):
    # READ FROM FILE
    workingVariable = ''
    lineCounter = 0
    cFile = open(fileName, "r")
    for line in cFile:
        lineCounter += 1
        if "%" in line:
            jaja = 0
        else:
            workingVariable = workingVariable + line + "\n"
            workingVariable = workingVariable.replace("\r", "")

    pattern = re.compile("([a-zA-Z]+)", re.M | re.X)
    out = pattern.findall(workingVariable)
    final = []
    for i in out:
        if i not in final:
            final.append(i)
    final.sort()

    finalFiltered = []
    for i in final:
        if i.isdigit():
            jaja = 1
        else:
            finalFiltered.append(i)

    final = finalFiltered
    # print(fileName)
    # print(final)
    # print(lineCounter)

    # WRITE TO HTTP FILE
    writeFile = open("summary_a4.html", "w")

    string = """<!DOCTYPE html>
                <html>
                <body>
                <h1>Prolog Project HTML!</h1>
                """
    writeFile.write(string)

    string = '<a href="testing.pl"> testing.pl </a> \n'
    writeFile.write(string)

    string = "<p> The Number of lines in the file is: " + str(lineCounter) + "</p> \n"
    writeFile.write(string)

    string = "<p> Alphabetical list of identifiers: <br/> \n"

    for term in final:
        string = string + term + "<br/> \n"

    string = string + "</p> \n"
    # print(string)

    writeFile.write(string)

    string = """</body>
                </html>
                """
    writeFile.write(string)

    writeFile.close()
    cFile.close()

def pythonParser(fileName):
    # READ FROM FILE
    workingVariable = ''
    lineCounter = 0
    cFile = open(fileName, "r")
    for line in cFile:
        lineCounter += 1
        if "#" in line:
            jaja = 0
        else:
            workingVariable = workingVariable + line + "\n"
            workingVariable = workingVariable.replace("\r", "")

    pattern = re.compile("([a-zA-Z\d-]+)", re.M | re.X)
    out = pattern.findall(workingVariable)
    final = []
    for i in out:
        if i not in final:
            final.append(i)
    final.sort()

    finalFiltered = []
    for i in final:
        if i.isdigit():
            jaja = 1
        else:
            finalFiltered.append(i)

    final = finalFiltered
    # print(fileName)
    # print(final)
    # print(lineCounter)

    # WRITE TO HTTP FILE
    writeFile = open("summary_a5.html", "w")

    string = """<!DOCTYPE html>
                <html>
                <body>
                <h1>Python Project HTML!</h1>
                """
    writeFile.write(string)

    string = '<a href="Main.py"> Main.py </a> \n'
    writeFile.write(string)

    string = "<p> The Number of lines in the file is: " + str(lineCounter) + "</p> \n"
    writeFile.write(string)

    string = "<p> Alphabetical list of identifiers: <br/> \n"

    for term in final:
        string = string + term + "<br/> \n"

    string = string + "</p> \n"
    # print(string)

    writeFile.write(string)

    string = """</body>
                </html>
                """
    writeFile.write(string)

    writeFile.close()
    cFile.close()


#YAY PYTHON SO STUFF JUST STARTS HAPPENING HERE
#WRITING INDIVIDUAL HTML

os.chdir('..')

dirpath = os.getcwd()
dirpath += "/a1"
os.chdir(dirpath)
for f_name in os.listdir(dirpath):
    if f_name.endswith(".c"):
        cParser(f_name)

os.chdir('..')

dirpath = os.getcwd()
dirpath += "/a2"
os.chdir(dirpath)
for f_name in os.listdir(dirpath):
    if f_name.endswith(".clj"):
        clojureParser(f_name)

os.chdir('..')

dirpath = os.getcwd()
dirpath += "/a3"
os.chdir(dirpath)
for f_name in os.listdir(dirpath):
    if f_name.endswith(".scala"):
        scalaParser(f_name)

os.chdir('..')

dirpath = os.getcwd()
dirpath += "/a4"
os.chdir(dirpath)
for f_name in os.listdir(dirpath):
    if f_name.endswith(".pl"):
        prologParser(f_name)

os.chdir('..')

dirpath = os.getcwd()
dirpath += "/a5"
os.chdir(dirpath)
for f_name in os.listdir(dirpath):
    if f_name.endswith(".py"):
        pythonParser(f_name)

#DONE WRITING HTML

#WRITE ROOT HTML

os.chdir('..')
indexFile = open("index.html", "w")
string = """<!DOCTYPE html>
                <html>
                <body>
                <h1>Please pick a Link</h1>
                """

indexFile.write(string)

string = '<a href="a1/summary_a1.html"> C Project <br/> </a> \n'
indexFile.write(string)

string = '<a href="a2/summary_a2.html"> Clojure Project <br/> </a> \n'
indexFile.write(string)

string = '<a href="a3/summary_a3.html"> Scala Project <br/> </a> \n'
indexFile.write(string)

string = '<a href="a4/summary_a4.html"> Prolog Project <br/> </a> \n'
indexFile.write(string)

string = '<a href="a5/summary_a5.html"> Python Project </a> \n'
indexFile.write(string)

string = """</body>
                </html>
                """
indexFile.write(string)
#IMPORTANT TO CLOSE FILE OR TAR ARCHIVING WILL NOT WORK LOL
indexFile.close()

#DONE WRITING ROOT HTML

#CREATING The TAR
mylist = ["tar", "-cvf", "project.tar.gz", "/Users/vincentpreikstas/Desktop/csc344"]



string = "tar -cvf project.tar.gz "
helpstring = os.getcwd()
helpstring += "/index.html"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a1/main.c"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a1/summary_a1.html"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a2/mainProject.clj"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a2/summary_a2.html"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a3/Main.scala"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a3/summary_a3.html"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a4/testing.pl"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a4/summary_a4.html"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a5/Main.py"

mylist.append(helpstring)

string = string + helpstring + " "
helpstring = os.getcwd()
helpstring = helpstring + "/a5/summary_a5.html"

mylist.append(helpstring)

string = string + helpstring

for item in mylist:
    print(item)

#otherstring = os.getcwd()
#print(string)
os.chdir('..')
#os.system("tar -czvf project.tar /Users/vincentpreikstas/Desktop/csc344")
#os.system(string)

email = input("please enter your email: ")
#print(email)

emailString = 'mutt -s "CSC 344 Project Tar" -a project.tar.gz -- ' + email + ' < /dev/null'
#print(emailString)

#process = subprocess.run(mylist)
os.system(string)
#process2 = subprocess.run(emailString)
os.system(emailString)


#START SCRATCH AREA
#dirpath = os.getcwd()
#print(dirpath)
#array = os.listdir()
#print(array)




#myFile = open(array[0], "r")
#print(myFile.read())

