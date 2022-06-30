import os, sys
import time

file = open(sys.argv[(1)], sys.argv[(2)])
file = file.read()
file = bytes(file, 'utf-8')

wrf = open(sys.argv[(3)], "wb")
wrf.write(file)


print("Showing binary in 5 secs CTRL+C to cancle console output the file is written")
time.sleep(6)
print(file)
