import os

paths = ['circuit5/']
for path in paths:
    files = os.listdir(path)
    for name_o_file in files:
        #print( name_o_file)
        f = open(path +name_o_file ,"r")
        lab = name_o_file.split(".")[0][-1]
        for line in f:
            #print( line)
            if line.find('responsetimea1') != -1:
                print(name_o_file, line.strip("\n"))