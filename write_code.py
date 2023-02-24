import pyautogui
from tkinter import Tk
import pyperclip

class Write:

    screen_width, screen_height = pyautogui.size()
    locked = False
    a,b=None,None
    scanned = False
    var1,var2 = None,None
    loop = False
    if_ = False
    tabulated = False
    returning_ = False
    created_HT = False
    val_ = True
    def write(self,x,y,action):

        if self.locked:
            return
        self.locked = True
        if action == "var":
            if x<0.25 and y < 0.25:
                print("scanning")
                self.scan()
            elif x<0.25 and y >= 0.25:
                print("hashmap")
                self.createHT()
            elif x>=0.25 and y < 0.25:
                print("variable a")
                self.var(self.a)
            elif x>= 0.25 and y >= 0.25:
                print("variable b")
                self.var(self.b)
                self.val_=True
        elif action == "func":
            if x < 0.25 and y < 0.25:
                print("for loop")
                self.forloop()
            elif x < 0.25 and y>=0.25:
                print("if")
                self.ifcondition()
            elif x >= 0.25 and y < 0.25:
                if self.if_:
                    print("val")
                    pyautogui.write("val in ")
                elif self.val_:
                    print("val")
                    pyautogui.write("val")
                    pyautogui.hotkey('right')
                else:
                    print("pos")
                    pyautogui.write("pos")
                    pyautogui.hotkey('right')
                    pyautogui.hotkey('right')
                    pyautogui.write("\n")
            elif x>= 0.25 and y>=0.25:
                print("return")
                self.returning()
        elif action == "spec":
            if x < 0.25 and y < 0.25:
                print("[]")
                self.bracket()
            elif x < 0.25 and y>=0.25:
                self.comma()
            elif x >= 0.25 and y < 0.25:
                if self.returning_:
                    print("=")
                    self.val_ = None
                    pyautogui.write(" = ")
                else:
                    print("left")
                    self.left()
            elif x>= 0.25 and y>=0.25:
                print("Control Z")
                pyautogui.hotkey('ctrl', 'z')
        elif action == "send":
            pyautogui.moveTo(1300, 1000, duration = 0)
            pyautogui.click()

        self.locked = False
    def scan(self):
        if not self.scanned:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.press('right')
            pyautogui.sleep(0.1)
            parameters = Tk().clipboard_get()
            parameters = parameters.split(',')
            a = parameters[1].split(':')[0][1:]
            if len(parameters) > 2:
                b = parameters[2].split(':')[0][1:]
            self.a = a
            self.b = b            
            pyperclip.copy("#")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.write(f" Scanning the parameters\n")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.write(f" In variable a is saved '{a}' in variable b '{b}'\n")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.write(f" To stop press 'q'\n")

            self.scanned = True

    def createHT(self):
        
        if not self.created_HT:
            pyperclip.copy("{")
            pyautogui.write("hashmap = ")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.sleep(0.1)
            pyperclip.copy("}")
            pyautogui.hotkey("ctrl", "v")
            pyautogui.write("\n")
            self.created_HT = True
        else:
            # if self.returning_:
            #     pyautogui.write("\n")
            #     pyautogui.hotkey('left')
            #     pyautogui.sleep(0.1)
            #     pyautogui.hotkey('left')
            #     pyautogui.sleep(0.1)
            #     pyautogui.hotkey('left')
            #     pyautogui.sleep(0.1)
            #     pyautogui.hotkey('left')
            #     pyautogui.sleep(0.1)
            pyautogui.write("hashmap")
            if self.if_:
                pyautogui.write(":\n")
                self.if_ = False
    
    def var(self, var):
        if self.loop:
            pyautogui.write(str(var))
            pyautogui.write("):\n")
            self.loop = False
        else:
            pyautogui.write(str(var))


    def forloop(self):
        pyautogui.write("for pos,val in enumerate(")
        self.loop = True
    def ifcondition(self):
        pyautogui.write("if ")
        self.if_ = True
    def returning(self):
        pyautogui.write("return ")
        self.returning_ = True
    def bracket(self):
        pyautogui.write("[")
    def comma(self):
        if self.returning_:
            print("comma")
            pyautogui.write(",")
            self.val_ = False
            self.returning_=None
        else:
            print(" substract")
            pyautogui.write(" - ")
            self.val_=True
            self.returning_ = True
    def left(self):
        pyautogui.hotkey('left')
        pyautogui.hotkey('left')
        pyautogui.hotkey('left')
        pyautogui.hotkey('left')
        self.returning_ = None