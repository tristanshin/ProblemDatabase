import os
os.chdir("P")

def standard(contest, numproblems, year):
	for i in range(1, numproblems + 1):
		filename = contest + '-' + str(year) + '-' + str(i) + '.tex'
		os.system('touch ' + filename)
		os.system('open ' + filename)

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
        os.system("touch " + filename)
        os.system("open " + filename)

def OMO(contest):
    path = "~/Dropbox/OMO/" + contest + "/problems"
    season = "Fall"
    if contest[0] == "S":
        season = "Spring"
    for i in range(1,31):
        problemnum = str(i)
        if len(problemnum) == 1:
            problemnum = "0" + problemnum
        pfile = open("OMO-" + season + "_20" + contest[-2:] + "-" + str(i) + ".tex","w+")
        os.chdir(os.path.expanduser(path))
        orig = open("prob" + problemnum + ".tex","r")
        for line in orig:
            if line[:5] == "\item":
                pass
            elif line[:11] == "\proposedby":
                break
            else:
                pfile.write(line)
        orig.close()
        pfile.close()
        os.chdir(os.path.expanduser("~/Dropbox/LaTeX/ProblemDatabase/P"))

def Putnam(year,version):
    for i in range(1,7):
        filename = "Putnam-" + str(year) + "-" + version + str(i) + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

def TARML(year):
    problems = []
    for i in range(1,11):
        problems.append("I" + str(i))
    for i in range(1,3):
        for j in range(1,4):
            problems.append("R" + str(i) + "." + str(j))
    for problem in problems:
        filename = "TARML-" + str(year) + "-" + problem + ".tex"
        os.system("touch " + filename)
        os.system("open " + filename)

standard('IMO', 6, 2020)
