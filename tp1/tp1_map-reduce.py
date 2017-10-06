### Library ###
import csv
import math

### Input reader ###
with open("input.csv") as fi:             # open the input file
    csvi = csv.reader(fi)                 # import the csv file
    i=0                                   # row counter
    map_list=[]                           # list declaration
    for row in csvi:                      # read the rows
        row_str = str(row[0]).split(";")  # split each col
        j=0                               # col counter
        
### Mapper ###
        for char in row_str:                           # read the cols
            map_list.append([j, str(i) + "-" + char])  # add to the list (key = number of the col, value = number of the row + value)
            j+=1                                       # col incrementation
        i+=1                                           # row incrementation
    
### Shuffle and sort ###
    map_list.sort()                                                                        # sort the list
    dim = int(math.sqrt(len(map_list)))                                                    # dimension of the matrix
    for i in range (0, dim):                                                               # 
        exec("reducer"+str(i)+"=[]")                                                       # reducer initialisation
        for j in range (0, dim):                                                           #
            exec("reducer"+str(i)+".append(["+str(i)+", '"+str(map_list[i*6+j][1])+"'])")  # distribute the couple (key, value)
        
### Reducer ###
    for i in range (0, dim):                                            #
        for j in range (0, dim):                                        #
            exec("reducer"+str(i)+"[j] = reducer"+str(i)+"[j][1][2:]")  # reduce the value

### Output writer ###
with open('output.csv', 'w', newline='') as fo:   # open the output file
    csvo = csv.writer(fo, delimiter=';')          # set the parameters
    for i in range (0, dim):                      # 
        exec("csvo.writerow(reducer"+str(i)+")")  # export data