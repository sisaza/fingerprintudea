from tkinter import *
from getImage import *

NAME = 'Fingerscan v0.1'
root = Tk()
root.title(NAME)

NUM_FINGERS = 4
state = 0 # which finger
scan = 0 # which of the two scans
msg = 'Success' # end of scan message

def fakescan():
    global state, scan, code, msg
    fingnames = ['index','middle','ring','pinky','thumb']
    again = ['',' again']
    def timecode():
        from datetime import datetime
        t = str(datetime.now())
        t = list(t)
        e = t.index(' ')
        p = t.index('.')
        t.remove(' ')
        t = ''.join(t[:p - 1])
        t = list(t)

        t.remove('-')
        t.remove('-')
        t.remove(':')
        t.remove(':')
        t = ''.join(t)

        return t

    def createdir(name):
        '''Ejecuta tsunami para generar el sitio web a partir de un archivo .lis'''
        from os import path, makedirs
        makedirs(name)

    if state == 0 and scan == 0: # new person
        code = timecode()
        createdir(code)

    perIDl.config(text='Person\'s code: ' + code)

    progl.config(text='Scanning '+fingnames[state]+'...')
    ans = getPrint_f(code, fingnames[state], str(scan)) #port to windows
    if ans != 'Error':
        logo.config(file=ans)
        if scan==0:
            scan = 1
        else:
            scan = 0
            state = state + 1
            if state == NUM_FINGERS:
                state = 0
                msg = 'Successfuly scanned all required fingers'

        placefinl.config(text='Place your ' + fingnames[state] + ' finger' + again[scan])
        progl.config(text=msg)
        msg = 'Success'
    else:
        progl.config(text='Error')

def config():
    pass

def quitProgram():
    global root
    root.destroy()

mainf = Frame(root)
mainf.pack()

Label(mainf,
              #align='center',
              padx = 10,
              font='Verdana 12 bold',
              text=NAME).grid(row=0)

imagef = Frame(mainf)
imagef.grid(column=1)
logo = PhotoImage(file='finger.png')
Label(imagef, image=logo).pack()

dataf = Frame(mainf)
dataf.grid(row=1, column=0)

infof = Frame(dataf)
infof.grid(row=0)

progl = Label(infof,
              padx = 10,
              font='Verdana 10')
progl.pack(side='top')

perIDl = Label(infof,
              padx = 10,
              font='Verdana 10')
perIDl.pack(side='top')

placefinl = Label(infof,
              padx = 10,
              font='Verdana 10',
              text='Place your index finger')
placefinl.pack(side='top')

buttonsf = Frame(dataf)
buttonsf.grid(row=1)

scanb = Button(buttonsf,
                   text="SCAN",
                   command=fakescan)
scanb.pack(side='top')

confb = Button(buttonsf,
                   text="CONFIG",
                   command=config)
confb.pack(side='top')

quitb = Button(buttonsf,
                   text="QUIT",
                   command=quitProgram)
quitb.pack(side='bottom')

root.mainloop()

'''
Para generar el ejecutable autocontenido para Windows desde Windows el comando es:
pyinstaller --onefile --windowed --icon=fprint.ico scangui.py
El ejecutable quedará en la carpeta distrondalla


Para instalar Pyinstaller es necesario instalar primero Python en Windows.
Luego, se debe ejecutar en una consola de Windows el siguiente comando que instalará Pyinstaller:
pip install pyinstaller
'''
