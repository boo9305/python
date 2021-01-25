import capture
import cv2 
import time
import psutil
import os 
import match;
import win32
import pos;

from matplotlib import pyplot as plt 

class Macro():
    hwnd = None
    def __init__(self,h, action, l):
        self.macro_list = []
        self.hwnd = h
        self.start = time.time()
        self.step = 0;
        self.action= action;

        #if who == 'hunt' :
        #    self.macro_list += pos.hunt();
        #elif who == 'test' :
        #    self.macro_list.append({'delay' : 3 , 'btn' : 'map'})
        #    self.macro_list.append({'delay' : 3 , 'btn' : 'map-exit'})
        #elif who == 'recovery' :
        #    self.macro_list += pos.recovery()
        #elif who == 'dogam':
        #    self.macro_list.append({'delay' : 1, 'btn' : 'dogam1'})
        #if action == 'recovery'
        self.init()
        self.macro_list += l   
            #self.macro

        print('# start %s %d macro!!' % (action, len(self.macro_list)))
    def __del__(self):
        self.macro_list = [] 

    def init(self):
        win32.esc_click(self.hwnd)
        win32.esc_click(self.hwnd)
        #win32.esc_click(self.hwnd)
        #win32.esc_click(self.hwnd)
        self.macro_list.append({'delay' : 1 , 'btn' : 'title-no'})
    
    def end(self):
        if self.step == len(self.macro_list):
            print('# end macro!!!')
            return True;
        return False;
    def run(self):

        # 현재시간 - 시작시간 = 딜레이
        delay = time.time() - self.start;
        print('%s delay time : %d , %d' % (self.action , delay, self.hwnd))
        
        for i, dic in enumerate(self.macro_list):
            if self.step == i and delay > dic['delay']:
                print("run macro step %d, %s ,%d" % (self.step , self.macro_list[i]['btn'] , len(self.macro_list)) )
                win32.mouse_click(self.hwnd, pos.btn_pos[self.macro_list[i]['btn']][0] , pos.btn_pos[self.macro_list[i]['btn']][1])
                self.step = self.step + 1;
                self.start = time.time();
                break;


def mouse_event(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('btn_pos[\'\'] = (%d, %d) ' %(x,y))
        #win32.mouse_click(h,x,y)


class WindowMacro():
    
    def __init__(self, title, isShow=False):
        self.action = {}
        self.isShow = isShow;
    
        self.title = "cv" + title 
        
        if self.isShow:
            cv2.namedWindow(self.title)
            cv2.moveWindow(self.title,800,100)
            cv2.setMouseCallback(self.title,mouse_event)
        
        self.h = win32.get_window(title) # dosa
        self.now_action = ""

    def set_action(self, key, value):
        print(key,value)
        self.action[key] = value;
        self.now_action = key;

    def get_normal(self):
        r = ""
        if self.isShow:        
            img = capture.window_capture(self.h)  
            r = match.normal_check(img)
        return r;

    def get_text(self):
        r = ""
        if self.isShow:        
            img = capture.window_capture(self.h)  
            r = match.dogam(img)
        return r;
            #cv2.imshow(self.title,img)
            #key = cv2.waitKey(1)      
    def stop(self):
        self.action = {}

    def run(self):
        for k, v in self.action.items():
            if self.now_action != '' and self.now_action != k:
                continue;
            if v['m'] != None:
                if v['m'].end():
                    v['timer'] = time.time();
                    v['repeat'] -= 1
                    self.now_action = ''
                    v['m'] = None;
                else :    
                    v['m'].run()
            else :
                delay = time.time() - v['timer'] ;
                #print(k, v)
                if v['repeat'] > 0:
                    print("%s %s delay %d..." % (self.h, k,delay))
                
                if delay > v['delay'] and v['repeat'] > 0 :
                    v['m'] = Macro(self.h, k, pos.action[k])
                    
                    self.now_action = k

        if self.isShow:        
            img = capture.window_capture(self.h)  
            #r = match.dogam(img)
            cv2.imshow(self.title,img)
            key = cv2.waitKey(1)        
        
            if key == ord('q') :  # 'q' exit
                print('q click')
                cv2.destroyAllWindows()
                exit()
        #return r
    def exit(self):
        cv2.destroyAllWindows()
        exit()

class Loop():
    key = ""
    
 #   start_hunting = time.time()
 #   start_recovery = time.time()
    
    action = {}

    def __init__(self):
        cv2.namedWindow('window')
        cv2.setMouseCallback('window',mouse_event)
        
        self.h1 = win32.get_window('NoxPlayer1') # dosa
        self.h2 = win32.get_window('NoxPlayer2') # dosa
        self.h3 = win32.get_window('NoxPlayer3') # dosa
        self.h4 = win32.get_window('NoxPlayer4') # dosa
        
        #self.action['hunt'] = {'delay' : 1 , 'timer' : time.time() , 'm' : None }
        #action['hunting'] = {'delay' : 3 , 'timer' : time.time() , 'm' : None }
        #self.action['recovery'] = {'delay' : 3 , 'timer' : time.time() , 'm' : None }
        #self.action['dogam'] = {'delay' : 1 , 'timer' : time.time() , 'm' : None }
        self.now_action = ""

    def set_action(self, key, value):
        self.action[key] = value;
        print(key, value)

    def run(self):
        key = ''
        #while h1:
        for k, v in self.action.items():
            print(len(self.action))
            if self.now_action != '' and self.now_action != k:
                continue;
            if len(v['m']) != 0:
                for m in v['m']:
                    if m.end():
                        v['timer'] = time.time();
                        v['repeat'] -= 1
                        now_action = ''
                        v['m'].remove(m)
                    else :    
                        m.run()
            else :
                delay = time.time() - v['timer'] ;
                print("%s delay %d..." % (k,delay))
                
                if delay > v['delay'] and v['repeat'] > 0 :
                    if k == 'sell_expr':
                        v['m'].append(Macro(self.h1, k, pos.action['sell_expr1']))
                        v['m'].append(Macro(self.h2, k, pos.action['sell_expr2']))
                        v['m'].append(Macro(self.h3, k, pos.action['sell_expr3']))
                        v['m'].append(Macro(self.h4, k, pos.action['sell_expr4']))

                    else:
                        v['m'].append(Macro(self.h1, k, pos.action[k]))
                        v['m'].append(Macro(self.h2, k, pos.action[k]))
                        v['m'].append(Macro(self.h3, k, pos.action[k]))
                        v['m'].append(Macro(self.h4, k, pos.action[k]))

                    self.now_action = k
                    
        img = capture.window_capture(self.h1)  
        r = match.dogam(img)
        cv2.imshow('window',img)
        key = cv2.waitKey(1)        
        
        if key == ord('q') :  # 'q' exit
            print('q click')
            cv2.destroyAllWindows()
            exit()

        return r
    def exit(self):
        cv2.destroyAllWindows()
        exit()

# macro class instance
if __name__ == '__main__' :
    l = Loop();
    l.run();


        # elif key == ord('h') : # 'h' home event
        #     home();
        # elif key == ord('n') : # 'n' end macro
        #     m = None;
        # elif key == ord('m') : # 'm' run marco
        #     m = Macro(h);


        
        #hp_mp_bar(img)
        #exp_bar(img)
        #map_text(img)

        #cv2.rectangle(img, (58,50), (200,85) , (255,0,255), 3)

        #cv2.imshow('w', img)
        #cv2.waitKey(1000)
        #plt.imshow(img),plt.show()

        #win32.mouse_click(h, 761,73)
        #match.text_match('m4')
        #win32.keyboard_click(h, 'w')
        #match.match('m2', c)
        
        

        #pid = os.getpid()
        #current_process = psutil.Process(pid)
        #current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2.**20
        #print(f"BEFORE CODE: Current memory KB   : {current_process_memory_usage_as_KB: 9.3f} KB")

    #cv2.imshow('c',c)
    #cv2.waitKey()
