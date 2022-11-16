import os
import sys

work = sys.argv[1]

w = open("./work.txt", "r+")
w.write(str(work))
w.close()