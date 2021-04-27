import os
os.chdir("L")

def standard(contest, numproblems, year):
    for i in range(1, numproblems + 1):
        filename = contest.replace(' ','') + '-' + str(year) + '-' + str(i) + '.tex'
        lfile = open(filename, 'w+')
        lfile.write(str(year) + ' ' + contest + ' \#' + str(i))
        lfile.close()

def AMC(year,test):
    for i in range(1,26):
        filename = "AMC" + test + "-" + str(year) + "-" + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " AMC " + test + " \#" + str(i))
        lfile.close()

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

def Putnam(year,version):
    for i in range(1,7):
        filename = "Putnam-" + str(year) + "-" + version + str(i) + ".tex"
        lfile = open(filename,"w+")
        lfile.write(str(year) + " Putnam " + version + str(i))
        lfile.close()

def TARML(year):
    problems = []
    for i in range(1,11):
        problems.append("I" + str(i))
    for i in range(1,3):
        for j in range(1,4):
            problems.append("R" + str(i) + "." + str(j))
    for problem in problems:
        filename = "TARML-" + str(year) + "-" + problem + ".tex"
        lfile = open(filename,"w+")
        if problem[0] == "R":
            problem = problem[:2] + "-" + problem[-1]
        lfile.write(str(year) + " TARML " + problem)
        lfile.close()

standard('IMO', 6, 2020)
