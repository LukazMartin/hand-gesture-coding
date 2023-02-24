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
    def write(self,x,y,action):

        if self.locked:
            return
        self.locked = True
        if action == "var":
            if x<0.25 and y < 0.25:
                self.scan()
            elif x<0.25 and y >= 0.25:
                self.createHT()
            elif x>=0.25 and y < 0.25:
                self.var(self.a)
            elif x>= 0.25 and y >= 0.25:
                self.var(self.b)
        elif action == "func":
            if x < 0.25 and y < 0.25:
                self.loop()
            elif x < 0.25 and y>=0.25:
                self.ifcondition()
            elif x >= 0.25 and y < 0.25:
                if self.if_:
                    pyautogui.write("val in ")
                else:
                    pyautogui.write("pos")
            elif x>= 0.25 and y>=0.25:
                self.returning()
        elif action == "spec":
            if x < 0.25 and y < 0.25:
                self.bracket()
            elif x < 0.25 and y>=0.25:
                self.comma()
            elif x >= 0.25 and y < 0.25:
                if self.returning_:
                    pyautogui.write(" = ")
                else:
                    self.left()
            elif x>= 0.25 and y>=0.25:
                pyautogui.hotkey('ctrl', 'z')

        self.locked = False
    def scan(self):
        if not self.scanned:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.press('right')
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
            pyautogui.write(f" To delete press at the bottom right.To quit press 'q'\n")

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
            if self.returning:
                pyautogui.write("\n")
                pyautogui.hotkey('left')
                pyautogui.sleep(0.1)
                pyautogui.hotkey('left')
                pyautogui.sleep(0.1)
                pyautogui.hotkey('left')
                pyautogui.sleep(0.1)
                pyautogui.hotkey('left')
                pyautogui.sleep(0.1)
            pyautogui.write("hashmap")
            if self.if_:
                pyautogui.write(":\n")
                self.if_ = False
    
    def var(self, var):
        pyautogui.write(var)
        if self.loop:
            pyautogui.write(":\n")
            self.loop = False

    def forloop(self):
        pyautogui.write("for pos,val in enumerate(")
        self.loop = True
    def ifcondition(self):
        pyautogui.write("if ")
        self.if_ = True
    def returning(self):
        pyperclip.copy("return ")
        self.returning_ = True
    def bracket(self):
        pyautogui.write("[]")
    def comma(self):
        if self.returning_:
            pyautogui.write(" - ")
        else:
            pyautogui.write(",")
    def left(self):
        pyautogui.hotkey('left')