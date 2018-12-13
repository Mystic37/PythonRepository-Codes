#Hello the secret word is unicorn
import time
from tkinter import *
window = Tk()
window.title('Secrets')
idea = 'asd'
#print("DEV MODE: what is the next user's deepest secret?")
#secret = input()
#input()
#print('...')
#time.sleep(2)
#print('Hello Shrey...')
#input()
#print('I know your deepst secrets...')
#print('press anything to go on...')
#input()
#print("You're secret is...")
#print(secret)
def cad():
	global idea
	msg.delete(0.0, END)
	msg.insert(END, idea)
	input()
msg = Text(window, width = 30, height = 2, wrap = WORD, background = 'white')
msg.grid(row = '0', column = '1', sticky = 'W')
idea = "DEV MODE: what is the next user's deepest secret?"
cad()
idea = '...'
cad()
idea = 'Hello User...'
cad()
idea = 'I know your deepst secrets...'
cad()
idea = "You're secret is..."
cad()
idea = secret
cad()
idea ="Cya!"
cad()

window.mainloop()