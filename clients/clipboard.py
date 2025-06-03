import urllib.parse
import requests

from pyperadaptor import pyperclip, waitForNewPaste

SERVER = "http://localhost:5000"


print("PysingScan listening clipboard...")
while True:
    txt = waitForNewPaste()
    print(f"CLIPBOARD: {txt}")

    # 2. URL-encodear la cadena entera
    encoded = urllib.parse.quote(txt, safe="")  

    response = requests.get(f"{SERVER}/replace/{encoded}")
    out = str(response.text)

    print(f"FILTERED:  {out}")

    pyperclip.copy(out)

