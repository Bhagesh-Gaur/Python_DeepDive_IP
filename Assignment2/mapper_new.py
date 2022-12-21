"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    word = line.split()
    print("%s\t%s" % (word[0], word[1]))
