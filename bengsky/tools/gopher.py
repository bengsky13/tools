import urllib.parse
import requests

def convert_to_gopher(prepared: requests.PreparedRequest) -> str:
    host = prepared.url.split('/')[2]
    path = prepared.path_url or '/'
    method = prepared.method.upper()
    body = prepared.body or ''
    headers = prepared.headers

    payload = f"{method} {path} HTTP/1.1\r\nHost: {host}\r\n"
    for k, v in headers.items():
        payload += f"{k}: {v}\r\n"
    payload += "\r\n"

    if isinstance(body, bytes):
        body = body.decode()

    payload += body

    gopher_payload = urllib.parse.quote(payload)
    return f"gopher://{host}/_{gopher_payload}"


def usage():
    print("""import requests
req = requests.Request(
    method='POST',
    url='http://example.com/login',
    headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data='username=admin&password=admin'
)
prepared = req.prepare()
gopher_url = convert_to_gopher(prepared)""")