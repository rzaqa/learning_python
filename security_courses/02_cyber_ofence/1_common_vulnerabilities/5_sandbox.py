import psutil
import win32api
import time

for proc in psutil.process_iter():
    try:
        process_name = proc.name()
        process_name = process_name.lower()
        if("wireshark" in process_name or "fiddler" in process_name or "sysmon" in process_Name or "System Monitor" in process_name):
            print("One or more debuggers/network analyze tools detected")
            exit()
    except:
        pass


x, y = win32api.GetCursorPos()
time.sleep(10)
x2, y2 = win32api.GetCursorPos()

if x -x2 == 0 and y - y2 == 0:
    print("No mouse movement detected!")
    exit()
else:
    pass


state_right_click = win32api.GetKeyState(0x02)

t_end = time.time() + 30

while time.time() < t_end:
    state = win32api.GetKeyState(0x02)

if state != state_right_click:
    state_right_click = state
    if state < 0:
        print("Right click detected!")
    else:
        print("Right click released!")
else:
    exit()


