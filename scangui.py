from tkinter import *
from getImage import *

NAME = 'Fingerscan v0.15p'
root = Tk()
root.title(NAME)

NUM_FINGERS = 4
state = 0 # which finger
scan = 0 # which of the two scans
msg = 'Success' # end of scan message

SERIAL_COM = 'COM3'
SERIAL_BAUDS = 57600

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
        from os import makedirs
        makedirs(name)

    if state == 0 and scan == 0: # new person
        code = timecode()
        createdir(code)

    perIDl.config(text='Person\'s code: ' + code)

    progl.config(text='Scanning '+fingnames[state]+'...')
    ans = getPrint_wrapper(code, fingnames[state], str(scan))
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

def save_config():
    global SERIAL_COM, SERIAL_BAUDS
    SERIAL_COM = sname.get()
    SERIAL_BAUDS = sbauds.get()

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
logo = PhotoImage(file='scan_example.png')
Label(imagef, image=logo).pack()

dataf = Frame(mainf)
dataf.grid(row=1, column=0)

infof = Frame(dataf)
infof.grid(row=0)

progl = Label(infof,
              padx = 5,
              width = 40,
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
'''
confb = Button(buttonsf,
                   text="CONFIG",
                   command=config)
confb.pack(side='top')
'''
quitb = Button(buttonsf,
                   text="QUIT",
                   command=quitProgram)
quitb.pack(side='bottom')

### config
configf = Frame(dataf)
configf.grid(row=3)

Label(configf, text='Serial port name:', anchor='e', width=20).grid(row=0, column=0)
sname = Entry(configf, width=10)
sname.insert(0, SERIAL_COM)
sname.grid(row=0, column=1)

Label(configf, text='Serial port baud rate:', anchor='e', width=20).grid(row=1, column=0)
sbauds = Entry(configf, width=10)
sbauds.insert(0, SERIAL_BAUDS)
sbauds.grid(row=1, column=1)

configb = Button(dataf,
                   text="SAVE CONFIGURATION",
                   command=save_config)
configb.grid(row=4)
###

root.mainloop()

'''
Para generar el ejecutable autocontenido para Windows desde Windows el comando es:
pyinstaller --onefile --windowed --icon=fprint.ico scangui.py
El ejecutable quedará en la carpeta distrondalla


Para instalar Pyinstaller es necesario instalar primero Python en Windows.
Luego, se debe ejecutar en una consola de Windows el siguiente comando que instalará Pyinstaller:
pip install pyinstaller
'''
