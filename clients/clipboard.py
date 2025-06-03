import requests
from pyperadaptor import pyperclip, waitForNewPaste
from constants import SERVER, DEV

# CLIENT

print("PysingScan listening clipboard...")
while True:
    txt = waitForNewPaste()


    if DEV:
        print(f"CLIPBOARD: {txt}")

    payload = {"mensaje": txt}
    response = requests.post(f"{SERVER}/replace", json=payload)
    out = str(response.text)

    if DEV:
        print(f"FILTERED:  {out}")

    pyperclip.copy(out)
