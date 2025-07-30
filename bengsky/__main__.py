import sys
import os
from .tools import rctf, ctfd

def main():
    if sys.argv[1] == 'ctfd':
        url = sys.argv[2]
        passwd = os.getenv('CTFD_USER')
        user = os.getenv('CTFD_PASSWORD')
        if url == '':
            print("PLEASE SET CTFD URL bengsky ctfd <url>")
            return
        if user == '':
            print("PLEASE SET CTFD_USER TO YOUR ENV")
            return
        if passwd == '':
            print("PLEASE SET CTFD_PASSWORD TO YOUR ENV")
            return
        ctfd.main(url, user, passwd)

        return
    elif sys.argv[1] == 'rctf':
        url = os.getenv('RCTF_URL')
        if url == '':
            print("PLEASE SET RCTF_URL TO YOUR ENV")
            return
        rctf.main(url)

if __name__ == "__main__":
    main()
