data = []
data['req'] = """import requests
URL = "HOST"
data = {
    "abc":"def"
}
headers = {
    "abc":"def"
}
req = requests.post(URL, data=data)
req = requests.get(URL)

"""
data['flask'] = """from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("id", "")
    return name

@app.route("/post", methods=["POST"])
def getPost():
    username = request.form.get("username")
    password = request.form.get("password")
    return username,password

if __name__ == "__main__":
    app.run(debug=True)
"""
data['pwn'] = """from pwn import *

context.terminal = ["tmux", "split-window", "-h", "-c", os.getcwd()]
context.encoding = "utf-8"


def start(argv=None, *a, local=None, remote=None, debug=None, **kw):
    argv = argv or [exe.path]
    local, remote, debug = local or {}, remote or {}, debug or {}

    if args.LOCAL and args.GDB:
        io = gdb.debug(argv, gdbscript=gdbscript, *a, **debug, **kw)
    elif args.LOCAL:
        io = process(argv, *a, **local, **kw)
    else:
        io = connect(host, port, *a, **remote, **kw)
    if args.GDB and not args.LOCAL:
        pid = int(subprocess.check_output(["pgrep", "chall"]))
        sysroot = f"/proc/{pid}/root"
        attach(pid, gdbscript=gdbscript, sysroot=sysroot, exe="chall", *a, **debug, **kw)

    return io


gdbscript = \"\"\"
b main
c
\"\"\"
host, port = args.HOST or "localhost", args.PORT or 1337
exe = context.binary = ELF(args.EXE or "./chall", False)

io = start()



io.interactive()
"""
print(data)
data['gopher'] = """import requests
req = requests.Request(
    method='POST',
    url='http://example.com/login',
    headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data='username=admin&password=admin'
)
prepared = req.prepare()
gopher_url = convert_to_gopher(prepared)


"""+data['req']

def main(what):
    with open("solve.py", "w") as f:
        f.write(data[what])