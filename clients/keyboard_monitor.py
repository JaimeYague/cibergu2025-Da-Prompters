import urllib.parse
import requests
import keyboard
from constants import *

BUFFER = ""
MAX_BUFFER = 100  # evitar buffers infinitos

def on_key_event(e):
    global BUFFER

    # Solo considerar letras, números, espacios y backspace
    if e.event_type != 'down':
        return

    if e.name == 'space':
        BUFFER += ' '
    elif e.name == 'enter':
        BUFFER += '\n'
    elif e.name == 'backspace':
        BUFFER = BUFFER[:-1]
        return
    elif len(e.name) == 1:
        BUFFER += e.name
    elif e.name == 'shift' or e.name == 'ctrl':
        return
    else:
        # ignorar otras teclas especiales
        return

    # Limitar tamaño del buffer
    BUFFER = BUFFER[-MAX_BUFFER:]

    # Verificar si hay datos sensibles
    encoded = urllib.parse.quote(BUFFER, safe="")  
    response = requests.get(f"{SERVER}/replace/{encoded}")
    sanitized = str(response.text)

    if sanitized != BUFFER:
        print("🔐 Texto sensible detectado.")
        for _ in range(len(BUFFER)):
            keyboard.send('backspace')  # Borrar carácter por carácter
        keyboard.write(sanitized)
        BUFFER = ""  # limpiar buffer después de reemplazar

print("⌨️ Monitoreando teclado... (CTRL+C para salir)")
keyboard.hook(on_key_event)
keyboard.wait()
