import win32gui
import win32con
import win32api
import time


child_handle = []

def all_ok(hwnd, param):
    name = win32gui.GetWindowText(hwnd)
    print(name)
   
    
    if name == 'ScreenBoardClassWindow' :
        child_handle.append(hwnd)     
def screen_ok(hwnd, param):
    name = win32gui.GetWindowText(hwnd)
   
    if name == param :
        print(name, param)
        child_handle.append(hwnd)     

def get_window(name):
    w = None
    w = win32gui.FindWindow(None, name)
    return w;

def get_child_window(hwnd):
    name = win32gui.GetWindowText(hwnd)
    print(name)
    win32gui.EnumChildWindows(hwnd, screen_ok, 'ScreenBoardClassWindow')
    return child_handle[0]

def mouse_click(w, x, y):
    lParam = win32api.MAKELONG(x ,y)

    win32api.PostMessage(w, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    time.sleep(0.2)
    win32api.PostMessage(w, win32con.WM_LBUTTONUP, 0, lParam)
    #time.sleep(1)
    #win32api.PostMessage(w, win32con.WM_LBUTTONUP, 0, lParam)


def esc_click(w):
    #print('esc click!!!')
    
    win32api.PostMessage(w, win32con.WM_ACTIVATEAPP, True, 0);
    win32api.PostMessage(w, win32con.WM_SETFOCUS, True, 0);
    #win32api.PostMessage(w, win32con.WM_ACTIVATE, True, 0);
    #win32api.PostMessage(w, win32con.WM_INPUT, win23con.RIM_INPUT, 0);
    
    win32api.PostMessage(w, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
    win32api.PostMessage(w, win32con.WM_CHAR, 27, 0)   
    win32api.PostMessage(w, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)
    #time.sleep(0.5)
    win32api.PostMessage(w, win32con.WM_ACTIVATE, True, 0)
	