import os
import http.server
import socketserver

import requests
from PIL import Image
from dotenv import load_dotenv


PORT = 8080

load_dotenv()

"""
This place is not a place of honor...
no highly esteemed deed is commemorated here...
nothing valued is here...

This program will send you cats if you are sad.
It's a hack build on top of SimpleHTTPRequestHandler.
"""


def random_cat_name():
    r = requests.get("https://randomuser.me/api/")
    print(f"random_name: {r.status_code}")

    json = r.json()
    return json["results"][0]["name"]["first"]


def random_cat_url():
    r = requests.get("https://api.thecatapi.com/v1/images/search", allow_redirects=True)
    print(f"random_cat_url: {r.status_code}")

    json = r.json()
    return json[0]["url"]


def shrink_cat(path):
    image = Image.open(path)
    image.thumbnail((400, 400))
    image.save(path)


def download_random_cat():
    url = random_cat_url()
    r = requests.get(url, allow_redirects=True)
    print(f"download_random_cat: {r.status_code}")

    location = f"cats/{url.split('/').pop()}"
    with open(location, "wb") as f:
        f.write(r.content)
        f.close()

    shrink_cat(location)

    return location


def send_cat():
    token = os.environ["PUSHOVER_API_KEY"]
    user = os.environ["PUSHOVER_USER_KEY"]

    if token == "":
        print("PUSHOVER_API_KEY was not set")

    if user == "":
        print("PUSHOVER_USER_KEY was not set")

    cat_name = random_cat_name()
    cat_picture = download_random_cat()

    r = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": token,
            "user": user,
            "message": f"{cat_name} needs your attention.",
        },
        files={"attachment": (f"{cat_name}", open(cat_picture, "rb"), "image/jpeg")},
    )
    print(f"send_cat: {r.status_code}")


class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        "": "application/octet-stream",
        ".manifest": "text/cache-manifest",
        ".html": "text/html",
        ".png": "image/png",
        ".jpg": "image/jpg",
        ".svg": "image/svg+xml",
        ".css": "text/css",
        ".js": "application/x-javascript",
        ".wasm": "application/wasm",
        ".json": "application/json",
        ".xml": "application/xml",
    }

    # hohoho what a mighty hack this is
    # future employers, please look away
    def translate_path(self, path: str) -> str:
        if path == "/":
            path = "/web/"

        if path.endswith("send_cat/"):
            send_cat()
            path = "/"

        return super().translate_path(path)


httpd = socketserver.TCPServer(("localhost", PORT), HttpRequestHandler)

try:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
