import sys
import os
from argparse import ArgumentParser
from .tools import rctf, ctfd

def main():
    if sys.argv[1] == 'ctfd':
        if sys.argv[1] == '':
            print("Usage: bengsky ctfd <url>")
            return
        parser = ArgumentParser(description='Simple CTFd-based scraper for challenges gathering')
        parser.add_argument('--data', metavar='data', type=str, help='Populate from challs.json')
        parser.add_argument('--proxy', metavar='proxy', type=str, help='Request behind proxy server')
        parser.add_argument('--path', metavar='path', type=str, help='Target directory, default: CTF', default='CTF')
        parser.add_argument('--worker',  metavar='worker', type=int, help='Number of threads, default: 10', default=10)
        parser.add_argument('--scheme',  metavar='scheme', type=str, help='URL scheme, default: https', default='https')
        parser.add_argument('--enable-cloud', help='Permit file download from a cloud drive, default=False', action='store_true')
        parser.add_argument('--override', help='Override existed chall file', action='store_true')
        parser.add_argument('--no-download', help='Don\'t download chall file', action='store_true')
        parser.add_argument('--export', help='Export challenges directory as zip, default=False', action='store_true')
        
        args, unknown = parser.parse_known_args()
        args.url = sys.argv[2]
        args.user = os.getenv('CTFD_USER')
        args.passwd = os.getenv('CTFD_PASSWORD')
        ctf  = ctfd.CTFdScrape(args)
        print(os.getcwd())
        if args.data or args.url:
            if args.user and args.passwd:
                ctf.authenticate()
                ctf.getChallenges()
            else:
                ctf.parseConfig(args.data)
                ctf.nofile = True
                ctf.createArchive()
                ctf.review()
        else:
            parser.error('too few arguments')
            return
    elif sys.argv[1] == 'rctf':
        url = os.getenv('RCTF_URL')
        if url == '':
            print("PLEASE SET RCTF_URL TO YOUR ENV")
            return
        rctf.main(url)

if __name__ == "__main__":
    main()
