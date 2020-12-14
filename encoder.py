#import tkinter module 
from tkinter import *

#import other necessery modules 
import random 
import time 
import datetime 

# creating root object 
root = Tk() 

# defining size of window 
root.geometry("1200x6000")

# setting up the title of window 
root.title("Message Encoder and Decoder")


TopF = Frame(root, width = 1600, relief = RAISED) 
TopF.pack(side = TOP) 

f1 = Frame(root, width = 800, height = 700, 
                            relief = RAISED) 
f1.pack(side = LEFT) 

# showing time
localtime = time.asctime(time.localtime(time.time())) 

lbInfo = Label(TopF, font = ('helvetica', 50, 'bold'), 
        text = "SECRET MESSAGING \n vignere cipher", 
                    fg = "Black", bd = 10, anchor='w') 
                    
lbInfo.grid(row = 0, column = 0) 

lbInfo = Label(TopF, font=('chaucer', 20, 'bold'), 
            text = localtime , fg = "red", 
                        bd = 10, anchor = 'w') 
                        
lbInfo.grid(row = 1, column = 0) 

rand = StringVar() 
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar()

#exit function 
def qExit(): 
    root.destroy() 

#Function to reset the window 
def Reset(): 
    rand.set("") 
    Msg.set("") 
    key.set("") 
    mode.set("") 
    Result.set("") 


#making necessary labels
#1
lblName = Label(f1, font = ('arial', 16, 'bold'), 
                text = "NAME:-", bd = 16, anchor = "w") 
                
lblName.grid(row = 0, column = 0) 

txtName = Entry(f1, font = ('arial', 16, 'bold'), 
            textvariable = rand, bd = 10, insertwidth = 4, 
                        bg = "light steel blue", justify = 'center') 
                        
txtName.grid(row = 0, column = 1) 
#2
lblMsg = Label(f1, font = ('arial', 16, 'bold'), 
        text = "MESSAGE:-", bd = 16, anchor = "w") 
        
lblMsg.grid(row = 1, column = 0) 

txtMsg = Entry(f1, font = ('arial', 16, 'bold'), 
        textvariable = Msg, bd = 10, insertwidth = 4, 
                bg = "light steel blue", justify = 'center') 
                
txtMsg.grid(row = 1, column = 1) 
#3
lblkey = Label(f1, font = ('arial', 16, 'bold'), 
            text = "KEY:-", bd = 16, anchor = "w") 
            
lblkey.grid(row = 2, column = 0) 

txtkey = Entry(f1, font = ('arial', 16, 'bold'), 
        textvariable = key, bd = 10, insertwidth = 4, 
                bg = "light steel blue", justify = 'center') 
                
txtkey.grid(row = 2, column = 1) 
#4
lblmode = Label(f1, font = ('arial', 16, 'bold'), 
        text = "MODE(e for encrypt, d for decrypt)", 
                                bd = 16, anchor = "w") 
                                
lblmode.grid(row = 3, column = 0) 

txtmode = Entry(f1, font = ('arial', 16, 'bold'), 
        textvariable = mode, bd = 10, insertwidth = 4, 
                bg = "light steel blue", justify = 'center') 
                    
txtmode.grid(row = 3, column = 1) 
#5
lblresult = Label(f1, font = ('arial', 18, 'bold'), 
            text = "THE RESULT:-", bd =16, anchor = "w") 
            
lblresult.grid(row = 2, column = 2) 

txtresult = Entry(f1, font = ('arial', 16, 'bold'), 
            textvariable = Result, bd = 14, insertwidth = 4, 
                    bg = "light steel blue", justify = 'right') 
                        
txtresult.grid(row = 2, column = 3) 

#importing Vigenere cipher module
import base64 

#Function to encode 
def encode(key, message): 
    enc = [] 
    
    for i in range(len(message)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(message[i]) +
                    ord(key_c)) % 256) 
                    
        enc.append(enc_c) 
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode() 

# Function to decode 
def decode(key, enc): 
    dec = [] 
    
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) -
                        ord(key_c)) % 256) 
                            
        dec.append(dec_c) 
    return "".join(dec) 

#function for getting message and mode and showing corresponding output
def Output(): 
    print("Message = ", (Msg.get())) 
    print("key = ", (key.get()))
    message = Msg.get() 
    k = key.get() 
    m = mode.get() 

    if (m == 'e'): 
        Result.set(encode(k, message)) 
    elif (m == 'd'):
        Result.set(decode(k, message))
    else:
        Result.set("Invalid")

print("Result is", Result)
#message button 
btnMessage = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                    text = "Show Message", bg = "gold", relief=GROOVE, 
                        command = Output).grid(row = 7, column = 1) 

#Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
                fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "Reset", bg = "green yellow",relief=GROOVE, 
                command = Reset).grid(row = 7, column = 2) 

#Exit button 
btnExit = Button(f1, padx = 16, pady = 8, bd = 16, 
                fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "Exit", bg = "firebrick2",relief=GROOVE, 
                command = qExit).grid(row = 7, column = 3) 

# keeps window alive 
root.mainloop() 
