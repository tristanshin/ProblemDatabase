import os
os.chdir("L")

def CCAMB(year):
    problems = []
    for i in range(1,16):
        problems.append("I" + str(i))
    for i in range(1,11):
        problems.append("T" + str(i))
    for i in range(1,6):
        for j in range(1,5):
            problems.append("L" + str(i) + "." + str(j))
    for i in range(1,5):
        problems.append("TB" + str(i))

    for problem in problems:
        filename = "CCAMB-" + str(year) + "-" + problem + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " CCAMB " + problem)
        lfile.close()
    

def OMO(contest):
    season = "Fall"
    if contest[0] == "S":
        season = "Spring"
    for i in range(1,31):
        lfile = open("OMO-" + season + "_20" + contest[-2:] + "-" + str(i) + ".tex","w+")
        lfile.write("OMO " + season + " 20" + contest[-2:] + " " + "\#" + str(i))
        lfile.close()

def USAMO(year):
    for i in range(1,7):
        filename = "USAMO-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " USAMO \#" + str(i))
        lfile.close()

def USAMO(year):
    for i in range(1,7):
        filename = "USAJMO-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " USAJMO \#" + str(i))
        lfile.close()
