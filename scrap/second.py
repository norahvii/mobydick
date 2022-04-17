import sys
import re


string = ""

with open("shortdick.txt","rt") as f:
       for line in f:
           if re.match(">",line):
              line = f.next()
           else:
              line = line.rstrip("\n")
              string = string + line
print(string)
