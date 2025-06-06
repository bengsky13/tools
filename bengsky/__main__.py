import sys
import os
from .tools import rctf

def main():
    if sys.argv[1] == 'ctfd':
        return
    elif sys.argv[1] == 'rctf':
        url = os.getenv('RCTF_URL')
        if url == '':
            print("PLEASE SET RCTF_URL TO YOUR ENV")
            return
        rctf.main(url)

if __name__ == "__main__":
    main()
