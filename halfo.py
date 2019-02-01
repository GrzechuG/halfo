#!/usr/bin/python3
import os
import sys

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def cmd(command):
    return os.popen(command).read()


def float_analysis(number):
    print ("Number is a decimal.")
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")
    print("Binary representation: "+str(int(bin(number)[2:])))
    print("Hexadecimal representation: " + str((hex(number)[2:])))
    print("")


def number_analysis(number):
    print("Number is an integer.")
    print("Number consists of "+str(len(str(number)))+" digits.")
    if number % 2 == 0:
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")
    print("Binary representation: "+str(int(bin(number)[2:])))
    print("Hexadecimal representation: " + str((hex(number)[2:])))
    print("")


def defineWikipedia(arg):

    try:

        import urllib.request, json
        with urllib.request.urlopen("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="+arg.replace(" ", "_")) as url:
            data = json.loads(url.read().decode())
            out=(str(data).split("'extract':")[1].split("'}")[0])
            if not "may refer to" in out:
                print(arg+" definition:")
                print(out)
            else:
                print("Cannot find proper definition. Word has many meanings.")
    except Exception as e:
        #print(e)
        pass

def python_analysis(contents):
    print("Imports: ")
    for line in contents.split("\n"):
        if line.startswith("import "):
            print(" " * len("import  ") + line.split("import ")[1])
    for line in contents.split("\n"):
        if line.startswith("from "):
            print(" " * len("import  ") + line.replace("import", ", is imported:"))
    print("Functions: ")
    for line in contents.split("\n"):
        if line.startswith("def "):
            print(" " * len("import  ") + line.split("def ")[1])

def file_analysis(filename):
    realpath=cmd("realpath "+filename)
    file_type=cmd("file '"+filename+"'")
    print("Realpath: "+realpath)
    print(file_type)
    if "text" in file_type:
        #print("File contents:")
        contents = open(filename, "r").read()
        print("Lines: "+str(len(contents.split("\n"))))
        print("Characters: " + str(len(contents)))
    if "Python script" in file_type:
        python_analysis(contents)

    pass

def dir_analysis(filename):
    realpath = cmd("realpath " + filename)
    print("Realpath: " + realpath)


    pass

arg = ""

for i in range(1, len(sys.argv)):
        n = sys.argv[i]
        arg=arg+" "+str(n)
if len(arg)>1:
    arg=arg[1:]
print("Analyzing: '"+arg+"'")
print("------------------------------------")
#Classify string type
comm=cmd("whatis "+arg+" 2>&1")
if not "nothing appropriate" in comm:
    print(""+comm)


defineWikipedia(arg)

if os.path.isfile(arg):
    print(arg +" is a file.")
    file_analysis(arg)

if os.path.isdir(arg):
    print(arg+" is a directory.")
    dir_analysis(arg)


if arg.isdigit():
    print(arg +" is a number.")
    number_analysis((int(arg)))

if isfloat(arg) and "." in arg:
    print(arg +" is a number.")
    float_analysis((float(arg)))


