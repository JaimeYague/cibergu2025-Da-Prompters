from pyperadaptor import pyperclip, waitForNewPaste
import requests

SERVER = "http://localhost:5000"


print("PysingScan listening clipboard...")
while True:
    txt = waitForNewPaste()
    print(f"CLIPBOARD: {txt}")
    response = requests.get(f"{SERVER}/replace/{txt}")
    out = str(response.text)

    print(f"FILTERED:  {out}")

    pyperclip.copy(out)

