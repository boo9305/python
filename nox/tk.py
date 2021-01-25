import tkinter
import m1
import time

class MyTk():
    def __init__(self):
        
        self.count = 0 
        #self.loop = m1.Loop()

        w1 = m1.WindowMacro('NoxPlayer1', isShow=True)
        w2 = m1.WindowMacro('NoxPlayer2')
        w3 = m1.WindowMacro('NoxPlayer3')
        w4 = m1.WindowMacro('NoxPlayer4')
        
        self.wl = [w1, w2, w3, w4]

        self.window = tkinter.Tk()
        self.window.geometry("640x400+100+100")
        self.label=tkinter.Label(self.window, text="0", fg="black")
        
        self.button1 = tkinter.Button(self.window, overrelief="solid", text="Exit", width=15, command=self.btnExit, repeatdelay=1000)
        self.button2 = tkinter.Button(self.window, overrelief="solid", text="Recovery", width=15, command=self.btn_recovery, repeatdelay=1000)
        self.button3 = tkinter.Button(self.window, overrelief="solid", text="SellExpr", width=15, command=self.btn_sell_expr, repeatdelay=1000)
        self.button4 = tkinter.Button(self.window, overrelief="solid", text="MoveDoin", width=15, command=self.btn_move_doin, repeatdelay=1000)
        self.button5 = tkinter.Button(self.window, overrelief="solid", text="MoveWeapon", width=15, command=self.btn_move_weapon, repeatdelay=1000)
        self.button6 = tkinter.Button(self.window, overrelief="solid", text="Stop", width=15, command=self.btn_stop, repeatdelay=1000)
        
        self.entry = tkinter.Entry(self.window)
        self.entry.bind("<Return>", self.calc);
        
        self.listbox = tkinter.Listbox(self.window, selectmode='extended', width=50, height=20)


        self.label.place(x=10, y=10)
        self.listbox.place(x=250, y=10)
        self.entry.place(x=10, y=50)

        self.button1.place(x=10, y=90)
        self.button2.place(x=10, y=120)
        self.button3.place(x=10, y=160)
        self.button4.place(x=10, y=200)
        
        self.button5.place(x=10, y=240)
        self.button6.place(x=10, y=280)
        self.update()    
        self.window.mainloop()
    	
    def update(self):
        #print(str(self.count))
        #r = self.loop.run()
        [w.run() for w in self.wl]
        #rr = self.wl[0].get_normal()
        #r = self.wl[0].get_text()
        #print(rr)
        #self.label.config(text=rr + " : "+ r + "%")
        self.window.after(1000, self.update)

    def btn_stop(self):
        self.log("click stop!");
        [ w.stop() for w in self.wl]
    def btn_recovery(self):
        #print("click recovery!!")  
        self.log("click recovery!");
        #self.loop.set_action('recovery', {'delay' : 1 , 'timer' : time.time() , 'm' : [] , 'repeat' : 1})
        [ w.set_action('recovery', {'delay' : 5 , 'timer' : time.time() , 'm' : None , 'repeat' : 5}) for w in self.wl ]
         
    def btn_move_doin(self):
        self.log("click move doin");
        [ w.set_action('move_doin', {'delay' : 1 , 'timer' : time.time() , 'm' : None, 'repeat' : 1}) for w in self.wl ]
    def btn_sell_expr(self):
        self.log("click sell expr!");

        self.wl[0].set_action('sell_expr1', {'delay' : 1 , 'timer' : time.time() , 'm' : None , 'repeat' : 1})
        self.wl[1].set_action('sell_expr2', {'delay' : 1 , 'timer' : time.time() , 'm' : None , 'repeat' : 1})
        self.wl[2].set_action('sell_expr3', {'delay' : 1 , 'timer' : time.time() , 'm' : None , 'repeat' : 1})
        self.wl[3].set_action('sell_expr4', {'delay' : 1 , 'timer' : time.time() , 'm' : None , 'repeat' : 1})
    
    def btn_move_weapon(self):
        self.log("click move weapon!"); 
        [ w.set_action('move_weapon', {'delay' : 1 , 'timer' : time.time() , 'm' : None , 'repeat' : 1}) for w in self.wl ]
    
    def btnExit(self):
        self.log("click exit!");
        self.wl[0].exit()
        #self.count += 1
        #self.label.config(text=str(self.count))
    
    def log(self, msg):
        self.listbox.insert(self.listbox.size(), msg);
    def calc(self, event):
        self.label.config(text="result=" + str(self.entry.get()))
    

if __name__ == "__main__":
    tk = MyTk()
