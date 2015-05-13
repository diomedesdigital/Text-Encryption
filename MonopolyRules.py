import fileinput
    
def read_line():
    #Input text file
    for line in fileinput.FileInput("/Users/j2y2k3/Desktop/monopoly_rules.txt",inplace=1):
        #Replace strings in text file
            line = line.replace ("Assets","XXXX")
            line = line.replace ("Parking","XXXX")
            line = line.replace ("Roll Snake Eyes","XXXX")
            line = line.replace ("New York Times","XXXX")
            line = line.replace ("money","XXXX")
            line = line.replace ("rule","XXXX")

            print (line)

read_line()


