from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk
import os

#================
#GLOBAL VARIABLES
#================

#auto-hat matrix
a0,a1,a2,a3,a4,a5,a6,a7 = ('0','0','0','0','0','0','0','0')
b0,b1,b2,b3,b4,b5,b6,b7 = ('0','0','0','0','0','0','0','0')
c0,c1,c2,c3,c4,c5,c6,c7 = ('0','0','0','0','0','0','0','0')
d0,d1,d2,d3,d4,d5,d6,d7 = ('0','0','0','0','0','0','0','0')

#auto_hat volume
get_hatvolume = ''

#auto_hat pitch
get_hatpitch = ''

#auto_hat wait
get_wait = ''

#tempo scale
get_tempo = '0'


class tortia(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()


    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False


    def setWait(self, str, *args):

        global get_wait
        get_wait = self.varwait
        print get_wait.get()

    def setTempo(self, str, *args):

        global get_tempo
        get_tempo = self.vartempo
        print get_tempo.get()


    def setHatpitch(self, val):
        global get_hatpitch
        get_hatpitch = int(float(val))
        x = get_hatpitch
        if get_hatpitch == x:
            get_hatpitch = 32-x
        print get_hatpitch

    def setHatvolume(self, val):
        global get_hatvolume
        get_hatvolume = int(float(val))
        print get_hatvolume

    def setHatstart(self, val):
        global get_hatstart
        get_hatstart = int(float(val))
        print get_hatstart



    def initUI(self):

        self.parent.title()
        self.pack(fill=BOTH, expand=1)


        #vv-boxbutton vars-vv#
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var11 = IntVar()
        self.var22 = IntVar()
        self.var33 = IntVar()
        self.var44 = IntVar()
        self.var55 = IntVar()
        self.var66 = IntVar()
        self.var77 = IntVar()
        self.var88 = IntVar()
        self.var111 = IntVar()
        self.var222 = IntVar()
        self.var333 = IntVar()
        self.var444 = IntVar()
        self.var555 = IntVar()
        self.var666 = IntVar()
        self.var777 = IntVar()
        self.var888 = IntVar()
        self.var1111 = IntVar()
        self.var2222 = IntVar()
        self.var3333 = IntVar()
        self.var4444 = IntVar()
        self.var5555 = IntVar()
        self.var6666 = IntVar()
        self.var7777 = IntVar()
        self.var8888 = IntVar()
        #^^-boxbutton vars-^^#


        label_hatsection = Frame(self,bd = 2,
                                relief = 'raised', height = 127, width = 240, )
        label_hatsection.place(x = 5, y = 5)
        label_hatsection.grid_propagate(0)




        self.varhatpitch = IntVar()
        c2 = Scale(self, from_=32, to=1,orient=VERTICAL, font = ('arial', 8)
                    ,variable=self.varhatpitch,command=self.setHatpitch)
        c2.pack(pady=0, padx=0)
        c2.place(x = 195, y = 10)
        c2.set(32)


        self.varhatvolume = IntVar()
        c3 = Scale(self, from_=15, to=0,orient=VERTICAL, font = ('arial', 8)
                    ,variable=self.varhatvolume,command=self.setHatvolume)
        c3.pack(pady=0, padx=0)
        c3.place(x = 160, y = 10)
        c3.set(7)


        label_autohat = Frame(self,bd = 2,
                                relief = 'sunken', height = 85, width = 153)
        label_autohat.place(x = 10, y = 10)
        label_autohat.grid_propagate(0)


        vol_label = Label(self, text = 'Vol', font = ('calibri', 8),
                            padx = 0, pady = 0)
        vol_label.place(x=176, y=111)


        pitch_label = Label(self, text = 'Pitch', font = ('calibri', 8),
                            padx = 0, pady = 0)
        pitch_label.place(x=213, y=111)



        vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        tick_label = Label(self, text = 'Ticks/row:', font = ('calibri', 10),
                            padx = 0, pady = 0)
        tick_label.place(x=297, y=85)

        self.vartempo = StringVar()
        c1 = Spinbox(self, from_=1, to=99, font = ('arial', 8), textvariable = self.vartempo,
                                    width = 2, validate = 'key', validatecommand = vcmd,
                                    cursor = 'arrow', insertontime = 0)
        c1.pack(pady=0, padx=0)
        c1.place(x = 362, y = 85)
        self.vartempo.trace( 'w', self.setTempo)
        self.vartempo.set(3)




      #----------#
        xx = 17  #   matrix-
        yy = 17 #  position
      #----------#
        yyy = yy+17
        yyyy = yyy+17
        yyyyy = yyyy+17

        cb1 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var1, command=self.onClick)
        cb1.place(x= xx, y= yy)

        cb2 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var2, command=self.onClick)
        cb2.place(x= xx+17, y= yy)

        cb3 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var3, command=self.onClick)
        cb3.place(x= xx+34, y= yy)

        cb4 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var4, command=self.onClick)
        cb4.place(x= xx+51, y= yy)

        cb5 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var5, command=self.onClick)
        cb5.place(x= xx+68, y= yy)

        cb6 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var6, command=self.onClick)
        cb6.place(x= xx+85, y= yy)

        cb7 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var7, command=self.onClick)
        cb7.place(x= xx+102, y= yy)

        cb8 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var8, command=self.onClick)
        cb8.place(x= xx+119, y= yy)

        #------------------------row 2



        cb11 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var11, command=self.onClick)
        cb11.place(x= xx, y= yyy)

        cb22 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var22, command=self.onClick)
        cb22.place(x= xx+17, y= yyy)

        cb33 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var33, command=self.onClick)
        cb33.place(x= xx+34, y= yyy)

        cb44 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var44, command=self.onClick)
        cb44.place(x= xx+51, y= yyy)

        cb55 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var55, command=self.onClick)
        cb55.place(x= xx+68, y= yyy)

        cb66 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var66, command=self.onClick)
        cb66.place(x= xx+85, y= yyy)

        cb77 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var77, command=self.onClick)
        cb77.place(x= xx+102, y= yyy)

        cb88 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var88, command=self.onClick)
        cb88.place(x= xx+119, y= yyy)

         #------------------------row 3



        cb111 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var111, command=self.onClick)
        cb111.place(x= xx, y= yyyy)

        cb222 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var222, command=self.onClick)
        cb222.place(x= xx+17, y= yyyy)

        cb333 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var333, command=self.onClick)
        cb333.place(x= xx+34, y= yyyy)

        cb444 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var444, command=self.onClick)
        cb444.place(x= xx+51, y= yyyy)

        cb555 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var555, command=self.onClick)
        cb555.place(x= xx+68, y= yyyy)

        cb666 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var666, command=self.onClick)
        cb666.place(x= xx+85, y= yyyy)

        cb777 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var777, command=self.onClick)
        cb777.place(x= xx+102, y= yyyy)

        cb888 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var888, command=self.onClick)
        cb888.place(x= xx+119, y= yyyy)

        #------------------------row 4



        cb1111 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var1111, command=self.onClick)
        cb1111.place(x= xx, y= yyyyy)

        cb2222 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var2222, command=self.onClick)
        cb2222.place(x= xx+17, y= yyyyy)

        cb3333 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var3333, command=self.onClick)
        cb3333.place(x= xx+34, y= yyyyy)

        cb4444 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var4444, command=self.onClick)
        cb4444.place(x= xx+51, y= yyyyy)

        cb5555 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var5555, command=self.onClick)
        cb5555.place(x= xx+68, y= yyyyy)

        cb6666 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var6666, command=self.onClick)
        cb6666.place(x= xx+85, y= yyyyy)

        cb7777 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var7777, command=self.onClick)
        cb7777.place(x= xx+102, y= yyyyy)

        cb8888 = Checkbutton(self, text="", padx=0, pady=0,
            variable=self.var8888, command=self.onClick)
        cb8888.place(x= xx+119, y= yyyyy)


        self.varwait = StringVar()
        c2 = Spinbox(self, from_=0, to=999, font = ('arial', 8), textvariable = self.varwait,
                                    width = 2, validate = 'key', validatecommand = vcmd,
                                        cursor = 'arrow', insertontime = 0)
        c2.pack(pady=0, padx=0)
        c2.place(x = 89, y = 104)
        self.varwait.trace( 'w', self.setWait)
        self.varwait.set(0)


        wait_label = Label(self, text = 'Wait:', font = ('calibri', 8),
                            padx = 0, pady = 0)
        wait_label.place(x=52, y=105)


        self.iconPath = 'docs/image/text.pbm'
        self.icon = ImageTk.PhotoImage(Image.open(self.iconPath))
        self.icon_place = Button(self, image = self.icon, relief = 'flat',
                                    command=self.Convert)
        self.icon_place.place(x=262, y=18)


    #===================================#
    #= I N S T R U M E N T  V A L U E S=#
    #===================================#

    def Convert(self):

        inst_value = {

            'C-101' : 'byte %00111110',#---------->FULL RANGE
            'C#101' : 'byte %00111100',
            'D-101' : 'byte %00111011',
            'D#101' : 'byte %00111001',
            'E-101' : 'byte %00111000',
            'F-101' : 'byte %00110110',
            'F#101' : 'byte %00110101',
            'G-101' : 'byte %00110100',
            'G#101' : 'byte %00110011',
            'A-101' : 'byte %00110001',
            'A#101' : 'byte %00110000',
            'B-101' : 'byte %00101111',
            'C-201' : 'byte %11011111',
            'C#201' : 'byte %11011101',
            'D-201' : 'byte %11011100',
            'D#201' : 'byte %11011010',
            'E-201' : 'byte %11011000',
            'F-201' : 'byte %11010111',
            'F#201' : 'byte %11010110',
            'G-201' : 'byte %11010100',
            'G#201' : 'byte %11010011',
            'A-201' : 'byte %11010010',
            'A#201' : 'byte %11010001',
            'B-201' : 'byte %11010000',
            'C-301' : 'byte %11001111',
            'C#301' : 'byte %11001110',
            'D-301' : 'byte %11001101',
            'D#301' : 'byte %11001100',
            'E-301' : 'byte %10111111',
            'F-301' : 'byte %10111101',
            'F#301' : 'byte %10111011',
            'G-301' : 'byte %10111010',
            'G#301' : 'byte %10111000',
            'A-301' : 'byte %10110111',
            'A#301' : 'byte %10110101',
            'B-301' : 'byte %10110100',
            'C-401' : 'byte %10110011',
            'C#401' : 'byte %10110010',
            'D-401' : 'byte %10110001',
            'D#401' : 'byte %10110000',
            'E-401' : 'byte %10101111',
            'F-401' : 'byte %10101110',
            'F#401' : 'byte %10101101',
            'G-401' : 'byte %10101100',
            'G#401' : 'byte %11000100',
            'A-401' : 'byte %10101011',
            'A#401' : 'byte %10101010',
            'B-401' : 'byte %00011111',
            'C-501' : 'byte %00011101',
            'C#501' : 'byte %00011011',
            'D-501' : 'byte %00011010',
            'D#501' : 'byte %00011000',
            'E-501' : 'byte %00010111',
            'F-501' : 'byte %00010101',
            'F#501' : 'byte %00010100',
            'G-501' : 'byte %00010011',
            'G#501' : 'byte %00010010',
            'A-501' : 'byte %00010001',
            'A#501' : 'byte %00010000',
            'B-501' : 'byte %00001111',
            'C-601' : 'byte %00001110',
            'C#601' : 'byte %00001101',
            'D-601' : 'byte %00001100',
            'E-601' : 'byte %00001011',
            'F-601' : 'byte %00001010',
            'G-601' : 'byte %00001001',
            'A-601' : 'byte %00001000',
            'B-601' : 'byte %00000111',
            'C#701' : 'byte %00000110',
            'E-701' : 'byte %00000101',
            'G-701' : 'byte %00000100',
            'B-701' : 'byte %00000011',

            'C-102' : 'byte %01111111',#---------->NOISE
            'C#102' : 'byte %01111110',
            'D-102' : 'byte %01111101',
            'D#102' : 'byte %01111100',
            'E-102' : 'byte %01111011',
            'F-102' : 'byte %01111010',
            'F#102' : 'byte %01111001',
            'G-102' : 'byte %01111000',
            'G#102' : 'byte %01110111',
            'A-102' : 'byte %01110110',
            'A#102' : 'byte %01110101',
            'B-102' : 'byte %01110100',
            'C-202' : 'byte %01110011',
            'C#202' : 'byte %01110010',
            'D-202' : 'byte %01110001',
            'D#202' : 'byte %01110000',
            'E-202' : 'byte %01101111',
            'F-202' : 'byte %01101110',
            'F#202' : 'byte %01101101',
            'G-202' : 'byte %01101100',
            'G#202' : 'byte %01101011',
            'A-202' : 'byte %01101010',
            'A#202' : 'byte %01101001',
            'B-202' : 'byte %01101000',
            'C-302' : 'byte %01100111',
            'C#302' : 'byte %01100110',
            'D-302' : 'byte %01100101',
            'D#302' : 'byte %01100100',
            'E-302' : 'byte %01100011',
            'F-302' : 'byte %01100010',
            'F#302' : 'byte %01100001',
            'G-302' : 'byte %01100000',
            'G#302' : 'byte %01111111',
            'A-302' : 'byte %01111110',
            'A#302' : 'byte %01111101',
            'B-302' : 'byte %01111100',
            'C-402' : 'byte %01111011',
            'C#402' : 'byte %01111010',
            'D-402' : 'byte %01111001',
            'D#402' : 'byte %01111000',
            'E-402' : 'byte %01110111',
            'F-402' : 'byte %01110110',
            'F#402' : 'byte %01110101',
            'G-402' : 'byte %01110100',
            'G#402' : 'byte %01110011',
            'A-402' : 'byte %01110010',
            'A#402' : 'byte %01110001',
            'B-402' : 'byte %01110000',
            'C-502' : 'byte %01101111',
            'C#502' : 'byte %01101110',
            'D-502' : 'byte %01101101',
            'D#502' : 'byte %01101100',
            'E-502' : 'byte %01101011',
            'F-502' : 'byte %01101010',
            'F#502' : 'byte %01101001',
            'G-502' : 'byte %01101000',
            'G#502' : 'byte %01100111',
            'A-502' : 'byte %01100110',
            'A#502' : 'byte %01100101',
            'B-502' : 'byte %01100100',
            'C-602' : 'byte %01100011',

            'C-103' : 'byte %10011111',#---------->BUZZ
            'C#103' : 'byte %10011100',
            'D-103' : 'byte %10011001',
            'D#103' : 'byte %10010111',
            'E-103' : 'byte %10010100',
            'F-103' : 'byte %10010001',
            'F#103' : 'byte %10001110',
            'G-103' : 'byte %10001011',
            'G#103' : 'byte %10001000',
            'A-103' : 'byte %10000101',
            'A#103' : 'byte %10000011',
            'B-103' : 'byte %10000000',
            'C-203' : 'byte %10011111',
            'C#203' : 'byte %10011100',
            'D-203' : 'byte %10011001',
            'D#203' : 'byte %10010111',
            'E-203' : 'byte %10010100',
            'F-203' : 'byte %10010001',
            'F#203' : 'byte %10001110',
            'G-203' : 'byte %10001011',
            'G#203' : 'byte %10001000',
            'A-203' : 'byte %10000101',
            'A#203' : 'byte %10000011',
            'B-203' : 'byte %10000000',
            'C-303' : 'byte %10011111',
            'C#303' : 'byte %10011100',
            'D-303' : 'byte %10011001',
            'D#303' : 'byte %10010111',
            'E-303' : 'byte %10010100',
            'F-303' : 'byte %10010001',
            'F#303' : 'byte %10001110',
            'G-303' : 'byte %10001011',
            'G#303' : 'byte %10001000',
            'A-303' : 'byte %10000101',
            'A#303' : 'byte %10000011',
            'B-303' : 'byte %10000000',
            'C-403' : 'byte %10011111',
            'C#403' : 'byte %10011100',
            'D-403' : 'byte %10011001',
            'D#403' : 'byte %10010111',
            'E-403' : 'byte %10010100',
            'F-403' : 'byte %10010001',
            'F#403' : 'byte %10001110',
            'G-403' : 'byte %10001011',
            'G#403' : 'byte %10001000',
            'A-403' : 'byte %10000101',
            'A#403' : 'byte %10000011',
            'B-403' : 'byte %10000000',
            'C-503' : 'byte %10011111',
            'C#503' : 'byte %10011100',
            'D-503' : 'byte %10011001',
            'D#503' : 'byte %10010111',
            'E-503' : 'byte %10010100',
            'F-503' : 'byte %10010001',
            'F#503' : 'byte %10001110',
            'G-503' : 'byte %10001011',
            'G#503' : 'byte %10001000',
            'A-503' : 'byte %10000101',
            'A#503' : 'byte %10000011',
            'B-503' : 'byte %10000000',
            'C-603' : 'byte %10011111',

            'C-104' : 'byte %11111110',#---------->ENGINE
            'C#104' : 'byte %11111110',
            'D-104' : 'byte %11111101',
            'D#104' : 'byte %11111100',
            'E-104' : 'byte %11111011',
            'F-104' : 'byte %11111010',
            'F#104' : 'byte %11111001',
            'G-104' : 'byte %11111000',
            'G#104' : 'byte %11110111',
            'A-104' : 'byte %11110110',
            'A#104' : 'byte %11110101',
            'B-104' : 'byte %11110100',
            'C-204' : 'byte %11110011',
            'C#204' : 'byte %11110010',
            'D-204' : 'byte %11110001',
            'D#204' : 'byte %11110000',
            'E-204' : 'byte %11101111',
            'F-204' : 'byte %11101110',
            'F#204' : 'byte %11101101',
            'G-204' : 'byte %11101100',
            'G#204' : 'byte %11101011',
            'A-204' : 'byte %11101010',
            'A#204' : 'byte %11101001',
            'B-204' : 'byte %11101000',
            'C-304' : 'byte %11100111',
            'C#304' : 'byte %11100110',
            'D-304' : 'byte %11100101',
            'D#304' : 'byte %11100100',
            'E-304' : 'byte %11100011',
            'F-304' : 'byte %11100010',
            'F#304' : 'byte %11100001',
            'G-304' : 'byte %11100000',
            'G#304' : 'byte %11111110',
            'A-304' : 'byte %11111110',
            'A#304' : 'byte %11111101',
            'B-304' : 'byte %11111100',
            'C-404' : 'byte %11111011',
            'C#404' : 'byte %11111010',
            'D-404' : 'byte %11111001',
            'D#404' : 'byte %11111000',
            'E-404' : 'byte %11110111',
            'F-404' : 'byte %11110110',
            'F#404' : 'byte %11110101',
            'G-404' : 'byte %11110100',
            'G#404' : 'byte %11110011',
            'A-404' : 'byte %11110010',
            'A#404' : 'byte %11110001',
            'B-404' : 'byte %11110000',
            'C-504' : 'byte %11101111',
            'C#504' : 'byte %11101110',
            'D-504' : 'byte %11101101',
            'D#504' : 'byte %11101100',
            'E-504' : 'byte %11101011',
            'F-504' : 'byte %11101010',
            'F#504' : 'byte %11101001',
            'G-504' : 'byte %11101000',
            'G#504' : 'byte %11100111',
            'A-504' : 'byte %11100110',
            'A#504' : 'byte %11100101',
            'B-504' : 'byte %11100100',
            'C-604' : 'byte %11100011',

            'C-105' : 'byte %00011111',#---------->SQUARE
            'C#105' : 'byte %00011110',
            'D-105' : 'byte %00011101',
            'D#105' : 'byte %00011100',
            'E-105' : 'byte %00011011',
            'F-105' : 'byte %00011010',
            'F#105' : 'byte %00011001',
            'G-105' : 'byte %00011000',
            'G#105' : 'byte %00010111',
            'A-105' : 'byte %00010110',
            'A#105' : 'byte %00010101',
            'B-105' : 'byte %00010100',
            'C-205' : 'byte %00010011',
            'C#205' : 'byte %00010010',
            'D-205' : 'byte %00010001',
            'D#205' : 'byte %00010000',
            'E-205' : 'byte %00001111',
            'F-205' : 'byte %00001110',
            'F#205' : 'byte %00001101',
            'G-205' : 'byte %00001100',
            'G#205' : 'byte %00001011',
            'A-205' : 'byte %00001010',
            'A#205' : 'byte %00001001',
            'B-205' : 'byte %00001000',
            'C-305' : 'byte %00000111',
            'C#305' : 'byte %00000110',
            'D-305' : 'byte %00000101',
            'D#305' : 'byte %00000100',
            'E-305' : 'byte %00000011',
            'F-305' : 'byte %00000010',
            'F#305' : 'byte %00000001',
            'G-305' : 'byte %00000000',
            'G#305' : 'byte %00011111',
            'A-305' : 'byte %00011110',
            'A#305' : 'byte %00011101',
            'B-305' : 'byte %00011100',
            'C-405' : 'byte %00011011',
            'C#405' : 'byte %00011010',
            'D-405' : 'byte %00011001',
            'D#405' : 'byte %00011000',
            'E-405' : 'byte %00010111',
            'F-405' : 'byte %00010110',
            'F#405' : 'byte %00010101',
            'G-405' : 'byte %00010100',
            'G#405' : 'byte %00010011',
            'A-405' : 'byte %00010010',
            'A#405' : 'byte %00010001',
            'B-405' : 'byte %00010000',
            'C-505' : 'byte %00001111',
            'C#505' : 'byte %00001110',
            'D-505' : 'byte %00001101',
            'D#505' : 'byte %00001100',
            'E-505' : 'byte %00001011',
            'F-505' : 'byte %00001010',
            'F#505' : 'byte %00001001',
            'G-505' : 'byte %00001000',
            'G#505' : 'byte %00000111',
            'A-505' : 'byte %00000110',
            'A#505' : 'byte %00000101',
            'B-505' : 'byte %00000100',
            'C-605' : 'byte %00000011',

            'C-106' : 'byte %11011111',#---------->SAW
            'C#106' : 'byte %11011110',
            'D-106' : 'byte %11011101',
            'D#106' : 'byte %11011100',
            'E-106' : 'byte %11011011',
            'F-106' : 'byte %11011010',
            'F#106' : 'byte %11011001',
            'G-106' : 'byte %11011000',
            'G#106' : 'byte %11010111',
            'A-106' : 'byte %11010110',
            'A#106' : 'byte %11010101',
            'B-106' : 'byte %11010100',
            'C-206' : 'byte %11010011',
            'C#206' : 'byte %11010010',
            'D-206' : 'byte %11010001',
            'D#206' : 'byte %11010000',
            'E-206' : 'byte %11001111',
            'F-206' : 'byte %11001110',
            'F#206' : 'byte %11001101',
            'G-206' : 'byte %11001100',
            'G#206' : 'byte %11001011',
            'A-206' : 'byte %11001010',
            'A#206' : 'byte %11001001',
            'B-206' : 'byte %11001000',
            'C-306' : 'byte %11000111',
            'C#306' : 'byte %11000110',
            'D-306' : 'byte %11000101',
            'D#306' : 'byte %11000100',
            'E-306' : 'byte %11000011',
            'F-306' : 'byte %11000010',
            'F#306' : 'byte %11000001',
            'G-306' : 'byte %11000000',
            'G#306' : 'byte %11011111',
            'A-306' : 'byte %11011110',
            'A#306' : 'byte %11011101',
            'B-306' : 'byte %11011100',
            'C-406' : 'byte %11011011',
            'C#406' : 'byte %11011010',
            'D-406' : 'byte %11011001',
            'D#406' : 'byte %11011000',
            'E-406' : 'byte %11010111',
            'F-406' : 'byte %11010110',
            'F#406' : 'byte %11010101',
            'G-406' : 'byte %11010100',
            'G#406' : 'byte %11010011',
            'A-406' : 'byte %11010010',
            'A#406' : 'byte %11010001',
            'B-406' : 'byte %11010000',
            'C-506' : 'byte %11001111',
            'C#506' : 'byte %11001110',
            'D-506' : 'byte %11001101',
            'D#506' : 'byte %11001100',
            'E-506' : 'byte %11001011',
            'F-506' : 'byte %11001010',
            'F#506' : 'byte %11001001',
            'G-506' : 'byte %11001000',
            'G#506' : 'byte %11000111',
            'A-506' : 'byte %11000110',
            'A#506' : 'byte %11000101',
            'B-506' : 'byte %11000100',
            'C-606' : 'byte %11000011',

            'C-107' : 'byte %01011111',#---------->PITFALL
            'C#107' : 'byte %01011110',
            'D-107' : 'byte %01011101',
            'D#107' : 'byte %01011100',
            'E-107' : 'byte %01011011',
            'F-107' : 'byte %01011010',
            'F#107' : 'byte %01011001',
            'G-107' : 'byte %01011000',
            'G#107' : 'byte %01010111',
            'A-107' : 'byte %01010110',
            'A#107' : 'byte %01010101',
            'B-107' : 'byte %01010100',
            'C-207' : 'byte %01010011',
            'C#207' : 'byte %01010010',
            'D-207' : 'byte %01010001',
            'D#207' : 'byte %01010000',
            'E-207' : 'byte %01001111',
            'F-207' : 'byte %01001110',
            'F#207' : 'byte %01001101',
            'G-207' : 'byte %01001100',
            'G#207' : 'byte %01001011',
            'A-207' : 'byte %01001010',
            'A#207' : 'byte %01001001',
            'B-207' : 'byte %01001000',
            'C-307' : 'byte %01000111',
            'C#307' : 'byte %01000110',
            'D-307' : 'byte %01000101',
            'D#307' : 'byte %01000100',
            'E-307' : 'byte %01000011',
            'F-307' : 'byte %01000010',
            'F#307' : 'byte %01000001',
            'G-307' : 'byte %01000000',
            'G#307' : 'byte %01011111',
            'A-307' : 'byte %01011110',
            'A#307' : 'byte %01011101',
            'B-307' : 'byte %01011100',
            'C-407' : 'byte %01011011',
            'C#407' : 'byte %01011010',
            'D-407' : 'byte %01011001',
            'D#407' : 'byte %01011000',
            'E-407' : 'byte %01010111',
            'F-407' : 'byte %01010110',
            'F#407' : 'byte %01010101',
            'G-407' : 'byte %01010100',
            'G#407' : 'byte %01010011',
            'A-407' : 'byte %01010010',
            'A#407' : 'byte %01010001',
            'B-407' : 'byte %01010000',
            'C-507' : 'byte %01001111',
            'C#507' : 'byte %01001110',
            'D-507' : 'byte %01001101',
            'D#507' : 'byte %01001100',
            'E-507' : 'byte %01001011',
            'F-507' : 'byte %01001010',
            'F#507' : 'byte %01001001',
            'G-507' : 'byte %01001000',
            'G#507' : 'byte %01000111',
            'A-507' : 'byte %01000110',
            'A#507' : 'byte %01000101',
            'B-507' : 'byte %01000100',
            'C-607' : 'byte %01000011',

            'C-108' : 'byte %00111111',#---------->BASS
            'C#108' : 'byte %00111110',
            'D-108' : 'byte %00111101',
            'D#108' : 'byte %00111100',
            'E-108' : 'byte %00111011',
            'F-108' : 'byte %00111010',
            'F#108' : 'byte %00111001',
            'G-108' : 'byte %00111000',
            'G#108' : 'byte %00110111',
            'A-108' : 'byte %00110110',
            'A#108' : 'byte %00110101',
            'B-108' : 'byte %00110100',
            'C-208' : 'byte %00110011',
            'C#208' : 'byte %00110010',
            'D-208' : 'byte %00110001',
            'D#208' : 'byte %00110000',
            'E-208' : 'byte %00101111',
            'F-208' : 'byte %00101110',
            'F#208' : 'byte %00101101',
            'G-208' : 'byte %00101100',
            'G#208' : 'byte %00101011',
            'A-208' : 'byte %00101010',
            'A#208' : 'byte %00101001',
            'B-208' : 'byte %00101000',
            'C-308' : 'byte %00100111',
            'C#308' : 'byte %00100110',
            'D-308' : 'byte %00100101',
            'D#308' : 'byte %00100100',
            'E-308' : 'byte %00100011',
            'F-308' : 'byte %00100010',
            'F#308' : 'byte %00100001',
            'G-308' : 'byte %00100000',
            'G#308' : 'byte %00111111',
            'A-308' : 'byte %00111110',
            'A#308' : 'byte %00111101',
            'B-308' : 'byte %00111100',
            'C-408' : 'byte %00111011',
            'C#408' : 'byte %00111010',
            'D-408' : 'byte %00111001',
            'D#408' : 'byte %00111000',
            'E-408' : 'byte %00110111',
            'F-408' : 'byte %00110110',
            'F#408' : 'byte %00110101',
            'G-408' : 'byte %00110100',
            'G#408' : 'byte %00110011',
            'A-408' : 'byte %00110010',
            'A#408' : 'byte %00110001',
            'B-408' : 'byte %00110000',
            'C-508' : 'byte %00101111',
            'C#508' : 'byte %00101110',
            'D-508' : 'byte %00101101',
            'D#508' : 'byte %00101100',
            'E-508' : 'byte %00101011',
            'F-508' : 'byte %00101010',
            'F#508' : 'byte %00101001',
            'G-508' : 'byte %00101000',
            'G#508' : 'byte %00100111',
            'A-508' : 'byte %00100110',
            'A#508' : 'byte %00100101',
            'B-508' : 'byte %00100100',
            'C-608' : 'byte %00100011',

            'C-109' : 'byte %10111111',#---------->LEAD
            'C#109' : 'byte %10111110',
            'D-109' : 'byte %10111101',
            'D#109' : 'byte %10111100',
            'E-109' : 'byte %10111011',
            'F-109' : 'byte %10111010',
            'F#109' : 'byte %10111001',
            'G-109' : 'byte %10111000',
            'G#109' : 'byte %10110111',
            'A-109' : 'byte %10110110',
            'A#109' : 'byte %10110101',
            'B-109' : 'byte %10110100',
            'C-209' : 'byte %10110011',
            'C#209' : 'byte %10110010',
            'D-209' : 'byte %10110001',
            'D#209' : 'byte %10110000',
            'E-209' : 'byte %10101111',
            'F-209' : 'byte %10101110',
            'F#209' : 'byte %10101101',
            'G-209' : 'byte %10101100',
            'G#209' : 'byte %10101011',
            'A-209' : 'byte %10101010',
            'A#209' : 'byte %10101001',
            'B-209' : 'byte %10101000',
            'C-309' : 'byte %10100111',
            'C#309' : 'byte %10100110',
            'D-309' : 'byte %10100101',
            'D#309' : 'byte %10100100',
            'E-309' : 'byte %10100011',
            'F-309' : 'byte %10100010',
            'F#309' : 'byte %10100001',
            'G-309' : 'byte %10100000',
            'G#309' : 'byte %10111111',
            'A-309' : 'byte %10111110',
            'A#309' : 'byte %10111101',
            'B-309' : 'byte %10111100',
            'C-409' : 'byte %10111011',
            'C#409' : 'byte %10111010',
            'D-409' : 'byte %10111001',
            'D#409' : 'byte %10111000',
            'E-409' : 'byte %10110111',
            'F-409' : 'byte %10110110',
            'F#409' : 'byte %10110101',
            'G-409' : 'byte %10110100',
            'G#409' : 'byte %10110011',
            'A-409' : 'byte %10110010',
            'A#409' : 'byte %10110001',
            'B-409' : 'byte %10110000',
            'C-509' : 'byte %10101111',
            'C#509' : 'byte %10101110',
            'D-509' : 'byte %10101101',
            'D#509' : 'byte %10101100',
            'E-509' : 'byte %10101011',
            'F-509' : 'byte %10101010',
            'F#509' : 'byte %10101001',
            'G-509' : 'byte %10101000',
            'G#509' : 'byte %10100111',
            'A-509' : 'byte %10100110',
            'A#509' : 'byte %10100101',
            'B-509' : 'byte %10100100',
            'C-609' : 'byte %10100011',

            '===..' : 'byte 255',
                'S' : '0' }



        #-------------------------
        #ch1 patterns and volume

        blank1 = ("byte 255")
        ch1note_values = 'CI0\n'
        ch1volu_values = '\tbyte %'
        a = 0
        g = 0
        q = 0

        #-------------------
        #ch1 pattern array

        pattern_values = ''
        ch1_pattern_array = ''
        c = 0
        e = 0
        m = 0
        m2 = 0
        m_count = 0

        #--------
        #song 1

        ch1_song_values = ''
        k = 0
        k_count = 0



        #-------------------------
        #ch2 patterns and volume

        blank2 = ("byte 255")
        ch2note_values = 'CII1\n'
        ch2volu_values = '\tbyte %'
        b = 1
        f = 0
        h = 0
        r = 0

        #-------------------
        #ch2 pattern array

        ch2_pattern_array = ''
        d = 0
        n = 1
        n2 = 1
        n_count = 0

        #--------
        #song 2

        ch2_song_values = ''
        l = 1
        l_count = 0




        infile = open("tortia.txt", "r")
        for line in infile:


            #ch1 patterns

            ch1note = line[1:6]


            if q == 1:
                ch1note_values += '\nCI%s\n' % a
                q = 0
            if ch1note in inst_value:
                blank1 = inst_value[ch1note]
                ch1note_values+= '\t%s\n' % inst_value[ch1note]
                e += 1
            elif ch1note == ".....":
                ch1note_values+= "\t%s\n" % blank1
                e += 1
            elif ch1note != '.....':
                if ch1note != 'odPlu':
                    ch1note_values+= "\tbyte 255\n"
                    e += 1

            #ch1 volume

            ch1volu = line[9:10]
            ch1volu_list = []


            if ch1volu in inst_value:
                ch1volu_values+= inst_value[ch1volu]
                g += 1
            elif ch1volu == '.':
                ch1volu_values+= '1'
                g += 1
            elif ch1volu != '.':
                if ch1volu != 'r':
                    ch1volu_values+= '1\n'
                    g += 1
            if g == 8:
                a += 2
                ch1volu_list.append(ch1volu_values)
                ch1note_values += '\n'
                ch1note_values += ch1volu_list[0]
                ch1note_values += '\n'
                ch1volu_values = '\tbyte %'
                g = 0
                q = 1


            #ch2 patterns

            ch2note = line[13:18]

            if r == 1:
                ch2note_values += '\nCII%s\n' % b
                r = 0
            if ch2note in inst_value:
                blank2 = inst_value[ch2note]
                ch2note_values+= '\t%s\n' % inst_value[ch2note]
                f += 1
            elif ch2note == ".....":
                ch2note_values+= "\t%s\n" % blank2
                f += 1
            elif ch2note != '.....':
                if ch2note != 'er  I':
                    ch2note_values+= "\tbyte 255\n"
                    f += 1


            #ch2 volume

            ch2volu = line[21:22]
            ch2volu_list = []

            if ch2volu in inst_value:
                ch2volu_values+= inst_value[ch2volu]
                h += 1
            elif ch2volu == '.':
                ch2volu_values+= '1'
                h += 1
            elif ch2volu != '.':
                if ch2volu != '':
                    ch2volu_values+= '1'
                    h += 1
            if h == 8:
                b += 2
                ch2volu_list.append(ch2volu_values)
                ch2note_values += '\n'
                ch2note_values += ch2volu_list[0]
                ch2note_values += '\n'
                ch2volu_values = '\tbyte %'
                h = 0
                r = 1


            #ch1 pattern array

            pattern_list1 = []
            if e == 8:
                if m_count == 0:
                    ch1_pattern_array += '\tword CI%s, ' % m
                    m_count += 1
                    m += 2
                    c += 1
                    e = 0
                elif m_count == 1:
                    ch1_pattern_array += 'CI%s, ' % m
                    m_count += 1
                    m += 2
                    c += 1
                    e = 0
                elif m_count == 2:
                    ch1_pattern_array += 'CI%s, ' % m
                    m_count += 1
                    m += 2
                    c += 1
                    e = 0
                elif m_count == 3:
                    ch1_pattern_array += 'CI%s ;%s\n' % (m, m2)
                    pattern_list1.append(ch1_pattern_array)
                    pattern_values += pattern_list1[0]
                    ch1_pattern_array = ''
                    m_count = 0
                    m += 2
                    m2 += 2
                    c += 1
                    e = 0


            #ch2 pattern array

            pattern_list2 = []
            if f == 8:
                if n_count == 0:
                    ch2_pattern_array += '\tword CII%s, ' % n
                    n_count += 1
                    n += 2
                    d += 1
                    f = 0
                elif n_count == 1:
                    ch2_pattern_array += 'CII%s, ' % n
                    n_count += 1
                    n += 2
                    d += 1
                    f = 0
                elif n_count == 2:
                    ch2_pattern_array += 'CII%s, ' % n
                    n_count += 1
                    n += 2
                    d += 1
                    f = 0
                elif n_count == 3:
                    ch2_pattern_array += 'CII%s ;%s\n' % (n, n2)
                    pattern_list2.append(ch2_pattern_array)
                    pattern_values += pattern_list2[0]
                    ch2_pattern_array = ''
                    n_count = 0
                    n += 2
                    n2 += 2
                    d += 1
                    f = 0


            #song1

            if c == 4:
                if k_count == 0:
                    ch1_song_values += '\tbyte %s, ' % k
                    k_count += 1
                    k += 2
                    c = 0
                elif k_count == 1:
                    ch1_song_values += '%s\n' % k
                    k_count = 0
                    k += 2
                    c = 0


            #song2

            if d == 4:
                if l_count == 0:
                    ch2_song_values += '\tbyte %s, ' % l
                    l_count += 1
                    l += 2
                    d = 0
                elif l_count == 1:
                    ch2_song_values += '%s\n' % l
                    l_count = 0
                    l += 2
                    d = 0


        infile.close()


        outfile = open('kit/song.h','w') #---------->overwrites "song.h"
        outfile.write


        print 'TEMPODELAY equ',get_tempo.get(),'\n\n'
        outfile.write('TEMPODELAY equ %s\n\n\n' % get_tempo.get())


        outfile = open('kit/song.h','a')


        print 'soundTurnArray'
        outfile.write('soundTurnArray\n')

        print '\tbyte 8, 0, 5, 9'
        outfile.write('\tbyte 8, 0, 5, 9\n')

        print '\tbyte 0, 6, 4, 0\n'
        outfile.write('\tbyte 0, 6, 4, 0\n\n')


        print 'soundTypeArray'
        outfile.write('soundTypeArray\n')

        print '\tbyte 4,6,7,8'
        outfile.write('\tbyte 4,6,7,8\n')

        print '\tbyte 15,12,1,14\n\n'
        outfile.write('\tbyte 15,12,1,14\n\n\n')


        printbyte = 'byte %'

        print 'hatPattern'
        outfile.write('hatPattern\n')

        print '\t%s%s%s%s%s%s%s%s%s' % (printbyte,a0,a1,a2,a3,a4,a5,a6,a7)
        outfile.write('\t%s%s%s%s%s%s%s%s%s\n' % (printbyte,a0,a1,a2,a3,a4,a5,
                                                a6,a7))

        print '\t%s%s%s%s%s%s%s%s%s' % (printbyte,b0,b1,b2,b3,b4,b5,b6,b7)
        outfile.write('\t%s%s%s%s%s%s%s%s%s\n' % (printbyte,b0,b1,b2,b3,b4,b5,
                                                b6,b7))

        print '\t%s%s%s%s%s%s%s%s%s' % (printbyte,c0,c1,c2,c3,c4,c5,c6,c7)
        outfile.write('\t%s%s%s%s%s%s%s%s%s\n' % (printbyte,c0,c1,c2,c3,c4,c5,
                                                c6,c7))

        print '\t%s%s%s%s%s%s%s%s%s\n\n' % (printbyte,d0,d1,d2,d3,d4,d5,d6,d7)
        outfile.write('\t%s%s%s%s%s%s%s%s%s\n\n' % (printbyte,d0,d1,d2,d3,d4,
                                                    d5,d6,d7))


        print 'HATSTART equ ', get_wait.get()
        outfile.write('HATSTART equ %s\n' % get_wait.get())

        print 'HATVOLUME equ', get_hatvolume
        outfile.write('HATVOLUME equ %s\n' % get_hatvolume)

        print 'HATPITCH equ', get_hatpitch
        outfile.write('HATPITCH equ %s\n' % get_hatpitch)

        print 'HATSOUND equ 8'
        outfile.write('HATSOUND equ 8\n\n\n')


        print 'song1\n\n', ch1_song_values
        outfile.write('song1\n\n%s\n' % ch1_song_values)

        print '\tbyte 255\n'
        outfile.write('\tbyte 255\n')

        print 'song2\n\n', ch2_song_values
        outfile.write('song2\n\n%s\n' % ch2_song_values)

        print '\tbyte 255\n\n\n\n'
        outfile.write('\tbyte 255\n\n\n\n')


        print 'patternArrayH\n\n'
        outfile.write('patternArrayH\n\n')

        print pattern_values, '\n\n'
        outfile.write('%s\n\n' % pattern_values)

        print 'patternArrayL\n\n\n\n'
        outfile.write('patternArrayL\n\n\n\n')


        print ch1note_values
        outfile.write('%s' % ch1note_values)

        print ch2note_values
        outfile.write('%s' % ch2note_values)


        outfile.close()


        os.chdir('kit')
        os.startfile('asm.bat')
        os.chdir(os.pardir)



    def onClick(self):
        global a0,a1,a2,a3,a4,a5,a6,a7
        global b0,b1,b2,b3,b4,b5,b6,b7
        global c0,c1,c2,c3,c4,c5,c6,c7
        global d0,d1,d2,d3,d4,d5,d6,d7

        if self.var1.get() == 1:  #start row 1
            a0 = '1'
        else:
            a0 = '0'
        if self.var2.get() == 1:
			a1 = '1'
        else:
			a1 = '0'
        if self.var3.get() == 1:
			a2 = '1'
        else:
			a2 = '0'
        if self.var4.get() == 1:
			a3 = '1'
        else:
			a3 = '0'
        if self.var5.get() == 1:
			a4 = '1'
        else:
			a4 = '0'
        if self.var6.get() == 1:
			a5 = '1'
        else:
			a5 = '0'
        if self.var7.get() == 1:
			a6 = '1'
        else:
			a6 = '0'
        if self.var8.get() == 1:
			a7 = '1'
        else:
			a7 = '0'
        if self.var11.get() == 1:  #start row 2
			b0 = '1'
        else:
			b0 = '0'
        if self.var22.get() == 1:
			b1 = '1'
        else:
			b1 = '0'
        if self.var33.get() == 1:
			b2 = '1'
        else:
			b2 = '0'
        if self.var44.get() == 1:
			b3 = '1'
        else:
			b3 = '0'
        if self.var55.get() == 1:
			b4 = '1'
        else:
			b4 = '0'
        if self.var66.get() == 1:
			b5 = '1'
        else:
			b5 = '0'
        if self.var77.get() == 1:
			b6 = '1'
        else:
			b6 = '0'
        if self.var88.get() == 1:
			b7 = '1'
        else:
			b7 = '0'
        if self.var111.get() == 1:  #start row 3
			c0 = '1'
        else:
			c0 = '0'
        if self.var222.get() == 1:
			c1 = '1'
        else:
			c1 = '0'
        if self.var333.get() == 1:
			c2 = '1'
        else:
			c2 = '0'
        if self.var444.get() == 1:
			c3 = '1'
        else:
			c3 = '0'
        if self.var555.get() == 1:
			c4 = '1'
        else:
			c4 = '0'
        if self.var666.get() == 1:
			c5 = '1'
        else:
			c5 = '0'
        if self.var777.get() == 1:
			c6 = '1'
        else:
			c6 = '0'
        if self.var888.get() == 1:
			c7 = '1'
        else:
			c7 = '0'
        if self.var1111.get() == 1: #start row 4
			d0 = '1'
        else:
			d0 = '0'
        if self.var2222.get() == 1:
			d1 = '1'
        else:
			d1 = '0'
        if self.var3333.get() == 1:
			d2 = '1'
        else:
			d2 = '0'
        if self.var4444.get() == 1:
			d3 = '1'
        else:
			d3 = '0'
        if self.var5555.get() == 1:
			d4 = '1'
        else:
			d4 = '0'
        if self.var6666.get() == 1:
			d5 = '1'
        else:
			d5 = '0'
        if self.var7777.get() == 1:
			d6 = '1'
        else:
			d6 = '0'
        if self.var8888.get() == 1:
			d7 = '1'
        else:
			d7 = '0'


def main():


    root = Tk()
    root.title("")
    app = tortia(root)
    app.parent.resizable(0,0)
    app.parent.geometry("450x137+300+300")
    app.mainloop()


if __name__ == '__main__':
    main()