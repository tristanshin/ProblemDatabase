# this is terribly inefficient
# sorry

import os
import glob

# taken from https://stackoverflow.com/a/4719576
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

# updates line 2 (index 1) of all files in W
# from \usepackage{../tssal} to \usepackage{tssal}
# because I finally put tssal.sty at the proper place
def update_local_tssal():
	os.chdir("W")
	for file in glob.glob("*.tex"):
		replace_line(file,1,"\\usepackage{tssal}\n")
	print("Updated files.")
	print("Changed line 2 of all files in W from\n\t\\usepackage{../tssal}\nto\n\t\\usepackage{tssal}")
	os.chdir("..")
