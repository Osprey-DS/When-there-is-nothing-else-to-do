import tkinter as tk
from tkinter.constants import END, GROOVE
root = tk.Tk()
from tkinter import messagebox
#--------------------------------------------------------------BackEnd Part-------------------------------------------------------#

import random
from random import randint


def shuffle(s):
    n = len(s) #n stores the length of the string 
    li = list(s) #since string is immutable, 
                 #we make a list of the characters of the string 

    for i in range(0,n-1): #i is iterated from 0 to n-2
        pos = randint(i+1,n-1) #this function randint will produce a 
                               #random number ranging between i+1 and n-1
        li[pos],li[i] = li[i],li[pos] #exchanging li[pos] and li[i]
    
    res = "" 
    for i in range(n):
        res = res + li[i] #sequentially add the charters of the list 
                          #to the string
    return res


file = open('C:\VS Code FOlder\Tkinter_prj1\Jumble_wordGame\words.txt', 'r')
file = file.read()

answers = file.split('\n')  #list of original words

words = []   #it's a list of shuffle words

for i in answers:                 #shuffling the words
    suf_word = shuffle(i)
    words.append(suf_word)


num = random.randrange(0, len(words),1)

##-------------------------------------------------------------------------------------------------------------------------------------##
def reset():
    global num, words, answers
    num = random.randrange(0,len(words),1)
    lbl_word.config(text=words[num])
    e1.delete(0, END)

def default():
    global words                    # or global words, answers, num
    global answers
    global num
    lbl_word.config(text=words[num])


#check answer function
def check_ans():
    global words, answers, num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo('  Success  ', 'You guess it right ')
        reset()
    else:
        messagebox.showerror('  Fail   ', 'Not Right \n Try again')
        e1.delete(0, END)
        


#------------------------------------------------------------------------FrontEnd Part--------------------------------------------------#
root.geometry('375x500')
root.title('!!    Jumbbled Game    !!')
root.configure(background='#a396e0') #all window will be in black color


lbl = tk.Label(root, text='Welcome in Jumbbled Word \n Guess The Word', font=('Comic sans ms', 20), bg='#a396e0', fg='#ffffff')
lbl.pack(pady=30, ipady=10, ipadx=10)  #this will leave some space from upper section

lbl_word = tk.Label(root, text='Word',font=('Comic sans ms', 20), bg='#a396e0', fg='#ffffff')
lbl_word.pack(pady=10)
 
########################################
ans = tk.StringVar()
e1= tk.Entry(root, font=('Verdana', 16), textvariable=ans)
e1.pack(ipadx=5,ipady=5)

##########################################
btn_check = tk.Button(root, text='Check', font=('Comic sans ms', 16), width= 10,
                            bg='#CAD5E2', fg='#6EC72D', relief=GROOVE, command=check_ans)
btn_check.pack(pady=40)  #dont't confues with ipady or pady

##########################################
btn_reset = tk.Button(root, text='Reset', font=('Comic sans ms', 16), width= 10,
                            bg='#BF3325', fg='#6EC72D', relief=GROOVE, command=reset)
btn_reset.pack()
############################################


default()  #calling the function for getting word in start of the game
root.mainloop()