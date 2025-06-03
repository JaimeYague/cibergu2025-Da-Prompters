import urllib.parse
import requests
from pyperadaptor import pyperclip, waitForNewPaste
from constants import *


print("PysingScan listening clipboard...")
while True:
    txt = waitForNewPaste()
    if(DEV):
        print(f"CLIPBOARD: {txt}")

    # 2. URL-encodear la cadena entera
    encoded = urllib.parse.quote(txt, safe="")  

    response = requests.get(f"{SERVER}/replace/{encoded}")
    out = str(response.text)

    if(DEV):
        print(f"FILTERED:  {out}")

    pyperclip.copy(out)

