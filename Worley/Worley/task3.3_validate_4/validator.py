import sys
from validatelib import *

if __name__ == '__main__':
    result = ExecutionInfo('assigment example', './worley', [1000, 1000], FileInfo('output.bmp', None, 3000054)).run()
    
    sys.exit(result)