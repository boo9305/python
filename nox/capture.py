import win32gui
import win32ui
import win32con
import win32api
import time
import numpy
from PIL import Image
from ctypes import windll
import cv2 


def window_capture(window):
    hwnd = None

    #hwnd = win32gui.FindWindow(None, window)
    hwnd = window

    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    #print(result)
    #print(saveBitMap)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    if result == 1:
        numpy_im = numpy.array(im)  
        cv_im = cv2.cvtColor(numpy_im, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('a',cv_im);
        #cv2.waitKey()
        return cv_im;
    else :
        return None;
        
        #im_re.save("./res/test.png")   
if __name__ == '__main__':
    c = window_capture('NoxPlayer2')
    
        #PrintWindow Succeeded
        #print('success')
    #    im_re = im.resize((960,540))
    #    im_re.save("./res/test.png")

    #img = cv2.imread('./res/test.png', 0)
    #return img;
    #img2 = cv2.resize(img,(960,480), interpolation=cv2.INTER_LINEAR)
    #cv2.imshow('a',img)
    ##img2 = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
    #cv2.imshow('a',img)
    #cv2.waitKey()

    ##img1 = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
    #img.imshow()
