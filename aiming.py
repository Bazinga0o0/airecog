import time
import multiprocessing as mp
import win32con
import win32api
import math

snapping = False #if true, the aimbot will snap to the target, turn off to use snapping_value
snapping_value = 50 #best between 30 and 100, lower is slower
smooth = True #if true, the aimbot will move the mouse smoothly to the target, based on the smoothing value
smoothing = 0.95 #best between 0.9 and 1, lower is slower

def aim(q_target):
    while True:    
        try:
            target = q_target.get()
        except mp.queues.Empty:
            continue
        except Exception as e:
            print(e)
        if target and target != (0,0,0):
            if win32api.GetAsyncKeyState(win32con.VK_XBUTTON1) < 0:
                in_view, dx, dy = target
                diff = 1
                if in_view and not (dx==0 and dy==0) and not snapping:
                    diff = snapping_value/math.sqrt(dx**2 + dy**2)
                if diff > 1:
                    diff = 1
                moveMouse((in_view, dx*diff, dy*diff))
        time.sleep(.001)
def moveMouse(target):
    in_view, dx, dy = target
    if smooth:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx*smoothing), int(dy*smoothing), 0, 0)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx), int(dy), 0, 0)
        
