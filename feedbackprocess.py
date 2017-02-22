#!/usr/bin/python
import sys
import re
import tempfile
temp_file = ""
d = {"1" : "one",
     "2": "two",
     "3": "three",
     "4": "four",
     "5": "five"
     }
if len(sys.argv) < 2:
    raise Exception("Supply file Name")

def remove_lines():
    fr = open(sys.argv[1],"r") # input file
    #fw = open(sys.argv[2],"w") # output temp file
    fw = tempfile.NamedTemporaryFile(delete=False) # output file
    global temp_file
    temp_file = fw.name;
    print "temp_file is" + temp_file
    prev_line = ""
    for line in fr:
        if re.match("^\"2017",line):
            final_line = line
            prev_line = line
        else:
            final_line = prev_line.strip("\n") + line
        fw.write(final_line)
    fr.close()
    fw.close()

def transform_column(col_num):
    fr = open(temp_file,"r")
    fw = open(sys.argv[2],"w") #output file
    for line in fr:
        line_list = line.split(",")
        col = line_list[col_num]
        for k,v in d.iteritems():
            new_col = ""
            if k in col:
                new_col = k
                #print "matched " + k 
                break;
            elif v.lower() in col.lower():
                new_col = k
                #print "matched " + v
                break;
            else:
                new_col = col
        print "col was " + col + "and new_col is " + new_col
        line_list[col_num] = new_col
        line_new = ",".join(line_list)
        fw.write(line_new)
remove_lines()    
transform_column(3)
