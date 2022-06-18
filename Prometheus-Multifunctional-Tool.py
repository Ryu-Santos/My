from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from fractions import Fraction
from sympy import *
from sympy.physics.units import *
from math import pi, e, log, sin, cos, tan, asin, acos, atan
import sympy.physics.units as unit
import re


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Prometheus")
        self.geometry("400x400")

        self.__frame = HomePage(self)
        self.__frame.pack()

    def switch_frame(self, FRAME):
        self.__frame.destroy()
        self.__frame = FRAME(self)
        self.__frame.pack()


class HomePage(Frame):
    def __init__(self, MASTER):  # parameter master is where the frame will be place, also, frames are stackable
        super().__init__(master=MASTER)

        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        title = f"{'Les anges'}\n{'de Freddie'}"

        self.__my_canvas.create_text(200, 75, text=title, fill='#d3fff3', justify="center", font=('LL Karatula', 35))

        btn_con = Button(self, text="Converter", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(ConverterPage))
        btn_cal = Button(self, text="Calculator", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(CalculatorPage))
        btn_todo = Button(self, text="To-do Work", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                          bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                          command=lambda: MASTER.switch_frame(WorkPage))

        self.__my_canvas.create_window(200, 250, anchor="center", window=btn_con)
        self.__my_canvas.create_window(200, 300, anchor="center", window=btn_cal)
        self.__my_canvas.create_window(200, 350, anchor="center", window=btn_todo)


"--------------------------------------------------------------------"


class CalculatorPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Calculator", fill='#d3fff3',
                                     justify="center", font=('LL Karatula', 24))

        ##-----------------Input and Output-----------------##
        display_input = Entry(self, font=("Aileron SemiBold", 12), background="#6A94B5", foreground="#D3FFF3",
                              insertwidth=1, width=30, justify="left")
        display_output = Entry(self, font=("Aileron SemiBold", 12), background="#6A94B5", foreground="#D3FFF3",
                               insertwidth=1, width=30, justify="right")

        self.__my_canvas.create_text(200, 80, text="=", fill="#D3FFF3", justify="center", font=('Aileron SemiBold', 20))

        self.__my_canvas.create_window(200, 55, anchor="center", window=display_input)
        self.__my_canvas.create_window(200, 105, anchor="center", window=display_output)

        ##-----------------Calculator Functions-----------------##
        def click(char):
            display_input.insert(END, str(char))

        def equal():
            result_str = display_input.get().replace("π", "pi").replace("^", "**")
            display_output.delete(0, END)

            try:
                result = eval(result_str)

            except:
                if result_str == "":
                    result = ""
                else:
                    result = "Syntax Error"

            display_output.insert(0, result)

        def delete():
            display_input.delete(len(display_input.get()) - 1)

        def clear():
            display_input.delete(0, END)
            display_output.delete(0, END)

        ##-----------------Calculator Buttons-----------------##
        wid = 6
        padx = 10
        pady = 5
        bgc = "#3D617D"
        fgc = "#D3FFF3"
        actbcol = "#6A94B5"
        actfcol = "#D3FFF3"
        font = ('Montserrat SemiBold', 8)

        btn_1 = Button(self, text="1", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(1))
        btn_2 = Button(self, text="2", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(2))
        btn_3 = Button(self, text="3", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(3))
        btn_4 = Button(self, text="4", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(4))
        btn_5 = Button(self, text="5", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(5))
        btn_6 = Button(self, text="6", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(6))
        btn_7 = Button(self, text="7", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(7))
        btn_8 = Button(self, text="8", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(8))
        btn_9 = Button(self, text="9", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click(9))
        btn_zero = Button(self, text="0", activeforeground=actfcol, activebackground=actbcol,
                          padx=padx, pady=pady, width=wid, font=font,
                          bg=bgc, fg=fgc, command=lambda: click(0))
        btn_power = Button(self, text="^", activeforeground=actfcol, activebackground=actbcol,
                           padx=padx, pady=pady, width=wid, font=font,
                           bg=bgc, fg=fgc, command=lambda: click("^"))
        btn_e = Button(self, text="e", activeforeground=actfcol, activebackground=actbcol,
                       padx=padx, pady=pady, width=wid, font=font,
                       bg=bgc, fg=fgc, command=lambda: click("e"))
        btn_dot = Button(self, text=".", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=lambda: click("."))
        btn_comma = Button(self, text=",", activeforeground=actfcol, activebackground=actbcol,
                           padx=padx, pady=pady, width=wid, font=font,
                           bg=bgc, fg=fgc, command=lambda: click(","))
        btn_add = Button(self, text="+", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=lambda: click("+"))
        btn_subt = Button(self, text="-", activeforeground=actfcol, activebackground=actbcol,
                          padx=padx, pady=pady, width=wid, font=font,
                          bg=bgc, fg=fgc, command=lambda: click("-"))
        btn_mult = Button(self, text="*", activeforeground=actfcol, activebackground=actbcol,
                          padx=padx, pady=pady, width=wid, font=font,
                          bg=bgc, fg=fgc, command=lambda: click("*"))
        btn_div = Button(self, text="/", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=lambda: click("/"))
        btn_pi = Button(self, text="π", activeforeground=actfcol, activebackground=actbcol,
                        padx=padx, pady=pady, width=wid, font=font,
                        bg=bgc, fg=fgc, command=lambda: click("π"))
        btn_leftP = Button(self, text="(", activeforeground=actfcol, activebackground=actbcol,
                           padx=padx, pady=pady, width=wid, font=font,
                           bg=bgc, fg=fgc, command=lambda: click("("))
        btn_rightP = Button(self, text=")", activeforeground=actfcol, activebackground=actbcol,
                            padx=padx, pady=pady, width=wid, font=font,
                            bg=bgc, fg=fgc, command=lambda: click(")"))
        btn_log = Button(self, text="log", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=lambda: click("log("))
        btn_sin = Button(self, text="sin", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=lambda: click("sin("))
        btn_cos = Button(self, text="cos", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=lambda: click("cos("))
        btn_tan = Button(self, text="tan", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=lambda: click("tan("))
        btn_shift = Button(self, text="SHIFT", activeforeground=actfcol, activebackground=actbcol,
                           padx=padx, pady=pady, width=wid, font=font,
                           bg=bgc, fg=fgc, command=lambda: click("a"))

        ##-----------------Special Buttons-----------------##
        btn_equal = Button(self, text="=", activeforeground=actfcol, activebackground=actbcol,
                           padx=padx, pady=pady, width=16, font=font,
                           bg="#6A94B5", fg=fgc, command=equal)
        btn_del = Button(self, text="DEL", activeforeground=actfcol, activebackground=actbcol,
                         padx=padx, pady=pady, width=wid, font=font,
                         bg=bgc, fg=fgc, command=delete)
        btn_clear = Button(self, text="AC", activeforeground=actfcol, activebackground=actbcol,
                           padx=padx, pady=pady, width=wid, font=font,
                           bg=bgc, fg=fgc, command=clear)

        ##-----------------1st Row-----------------##
        self.__my_canvas.create_window(60, 150, anchor="center", window=btn_shift)
        self.__my_canvas.create_window(130, 150, anchor="center", window=btn_sin)
        self.__my_canvas.create_window(200, 150, anchor="center", window=btn_cos)
        self.__my_canvas.create_window(270, 150, anchor="center", window=btn_tan)
        self.__my_canvas.create_window(340, 150, anchor="center", window=btn_log)
        ##-----------------2nd Row-----------------##
        self.__my_canvas.create_window(60, 185, anchor="center", window=btn_leftP)
        self.__my_canvas.create_window(130, 185, anchor="center", window=btn_rightP)
        self.__my_canvas.create_window(200, 185, anchor="center", window=btn_power)
        self.__my_canvas.create_window(270, 185, anchor="center", window=btn_comma)
        self.__my_canvas.create_window(340, 185, anchor="center", window=btn_e)
        ##-----------------3rd Row-----------------##
        self.__my_canvas.create_window(60, 220, anchor="center", window=btn_7)
        self.__my_canvas.create_window(130, 220, anchor="center", window=btn_8)
        self.__my_canvas.create_window(200, 220, anchor="center", window=btn_9)
        self.__my_canvas.create_window(270, 220, anchor="center", window=btn_del)
        self.__my_canvas.create_window(340, 220, anchor="center", window=btn_clear)
        ##-----------------4th Row-----------------##
        self.__my_canvas.create_window(60, 255, anchor="center", window=btn_4)
        self.__my_canvas.create_window(130, 255, anchor="center", window=btn_5)
        self.__my_canvas.create_window(200, 255, anchor="center", window=btn_6)
        self.__my_canvas.create_window(270, 255, anchor="center", window=btn_mult)
        self.__my_canvas.create_window(340, 255, anchor="center", window=btn_div)
        ##-----------------5th Row-----------------##
        self.__my_canvas.create_window(60, 290, anchor="center", window=btn_1)
        self.__my_canvas.create_window(130, 290, anchor="center", window=btn_2)
        self.__my_canvas.create_window(200, 290, anchor="center", window=btn_3)
        self.__my_canvas.create_window(270, 290, anchor="center", window=btn_add)
        self.__my_canvas.create_window(340, 290, anchor="center", window=btn_subt)
        ##-----------------6th Row-----------------##
        self.__my_canvas.create_window(60, 325, anchor="center", window=btn_zero)
        self.__my_canvas.create_window(130, 325, anchor="center", window=btn_dot)
        self.__my_canvas.create_window(200, 325, anchor="center", window=btn_pi)
        self.__my_canvas.create_window(305, 325, anchor="center", window=btn_equal)

        ##-----------------Back Button to Home Page-----------------##
        btn_back = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                          bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                          command=lambda: MASTER.switch_frame(HomePage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back)
class ConverterPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Converter", fill='#d3fff3',
                                     justify="center", font=('LL Karatula', 24))
        btn_len = Button(self, text="Length", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(LengthPage))
        btn_mass = Button(self, text="Mass", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                          bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                          command=lambda: MASTER.switch_frame(MassPage))
        btn_temp = Button(self, text="Temperature", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                          bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                          command=lambda: MASTER.switch_frame(TemperaturePage))
        btn_vol = Button(self, text="Volume", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(VolumePage))
        btn_ene = Button(self, text="Energy", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(EnergyPage))
        btn_pow = Button(self, text="Power", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(PowerPage))
        btn_cur = Button(self, text="Current", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(CurrentPage))
        btn_cha = Button(self, text="Charge", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(ChargePage))
        btn_tme = Button(self, text="Time", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(TimePage))
        btn_nuB = Button(self, text="Number Base", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(NumberBasePage))
        btn_mcd = Button(self, text="Morse Code", padx=5, pady=3, width=10, height=2, font=('Roboto Medium', 10),
                         bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                         command=lambda: MASTER.switch_frame(MorseCodePage))
        btn_dtf = Button(self, text=f"Decimal\nto Fraction", padx=5, pady=3, width=10, height=2,
                         font=('Roboto Medium', 10), bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86",
                         activeforeground="#D3FFF3", command=lambda: MASTER.switch_frame(DecimaltoFractionPage))

        ##~~~~~~~~~~~~~~~~~~~~Commonly Used Measurements Row~~~~~~~~~~~~~~~~~~~~##
        self.__my_canvas.create_window(65, 100, anchor="center", window=btn_len)
        self.__my_canvas.create_window(155, 100, anchor="center", window=btn_mass)
        self.__my_canvas.create_window(245, 100, anchor="center", window=btn_temp)
        self.__my_canvas.create_window(335, 100, anchor="center", window=btn_vol)

        ##~~~~~~~~~~~~~~~~~~~~Electricity Conversion Row~~~~~~~~~~~~~~~~~~~~##
        self.__my_canvas.create_window(65, 200, anchor="center", window=btn_ene)
        self.__my_canvas.create_window(155, 200, anchor="center", window=btn_pow)
        self.__my_canvas.create_window(245, 200, anchor="center", window=btn_cur)
        self.__my_canvas.create_window(335, 200, anchor="center", window=btn_cha)

        ##~~~~~~~~~~~~~~~~~~~~Others Conversion Row~~~~~~~~~~~~~~~~~~~~##
        self.__my_canvas.create_window(65, 300, anchor="center", window=btn_tme)
        self.__my_canvas.create_window(155, 300, anchor="center", window=btn_nuB)
        self.__my_canvas.create_window(245, 300, anchor="center", window=btn_mcd)
        self.__my_canvas.create_window(335, 300, anchor="center", window=btn_dtf)

        ##-----------------Back Button to Home Page-----------------##
        btn_back = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                          bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                          command=lambda: MASTER.switch_frame(HomePage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back)

    ##~~~~~~~~~~~~~~~~~~~~Length Page~~~~~~~~~~~~~~~~~~~~##
class LengthPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Length Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        length_units = ['Millimeter', 'Centimeter', 'Decimeter', 'Meter', 'Kilometer', 'Lightyear', 'Inch', 'Foot',
                        'Yard', 'Mile', 'Nautical Mile']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_length.get()
            outunit = output_length.get()

            #----inputs----#
            if inpunit == "Millimeter":
                inpunit = inp*unit.mm
            if inpunit == "Centimeter":
                inpunit = inp*unit.cm
            if inpunit == "Decimeter":
                inpunit = inp*unit.dm
            if inpunit == "Meter":
                inpunit = inp*unit.m
            if inpunit == "Kilometer":
                inpunit = inp*unit.km
            if inpunit == "Lightyear":
                inpunit = inp*unit.ly
            if inpunit == "Inch":
                inpunit = inp*unit.inch
            if inpunit == "Foot":
                inpunit = inp*unit.foot
            if inpunit == "Yard":
                inpunit = inp*unit.yd
            if inpunit == "Mile":
                inpunit = inp*unit.mile
            if inpunit == "Nautical Mile":
                inpunit = inp*unit.nautical_mile
            #----outputs----#
            if outunit == "Millimeter":
                outunit = unit.mm
            if outunit == "Centimeter":
                outunit = unit.cm
            if outunit == "Decimeter":
                outunit = unit.dm
            if outunit == "Meter":
                outunit = unit.m
            if outunit == "Kilometer":
                outunit = unit.km
            if outunit == "Lightyear":
                outunit = unit.ly
            if outunit == "Inch":
                outunit = unit.inch
            if outunit == "Foot":
                outunit = unit.foot
            if outunit == "Yard":
                outunit = unit.yd
            if outunit == "Mile":
                outunit = unit.mile
            if outunit == "Nautical Mile":
                outunit = unit.nautical_mile

            convert = str(unit.convert_to(inpunit, outunit).n())
            float_convert = re.sub('[*]' + str(outunit), "", convert)

            outputentry.delete(0, END)
            outputentry.insert(0, float_convert)

        input_length = StringVar()
        input_length.set(length_units[0])
        output_length = StringVar()
        output_length.set(length_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_length, state='readonly')
        inputbox['values'] = length_units
        outputbox = ttk.Combobox(self, textvariable=output_length, state='readonly')
        outputbox['values'] = length_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

        ##~~~~~~~~~~~~~~~~~~~~Mass Page~~~~~~~~~~~~~~~~~~~~##
class MassPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Mass Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        mass_units = ['Microgram', 'Milligram', 'Gram', 'Kilogram', 'Pound', 'Planck Mass', 'Atomic Mass Unit']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_mass.get()
            outunit = output_mass.get()

            #----inputs----#
            if inpunit == "Microgram":
                inpunit = inp*unit.microgram
            if inpunit == "Milligram":
                inpunit = inp*unit.milligram
            if inpunit == "Gram":
                inpunit = inp*unit.gram
            if inpunit == "Kilogram":
                inpunit = inp*unit.kilogram
            if inpunit == "Pound":
                inpunit = inp*unit.pound
            if inpunit == "Planck Mass":
                inpunit = inp*unit.planck_mass
            if inpunit == "Atomic Mass Unit":
                inpunit = inp*unit.atomic_mass_unit
            #----outputs----#
            if outunit == "Microgram":
                outunit = unit.microgram
            if outunit == "Milligram":
                outunit = unit.milligram
            if outunit == "Gram":
                outunit = unit.gram
            if outunit == "Kilogram":
                outunit = unit.kilogram
            if outunit == "Pound":
                outunit = unit.pound
            if outunit == "Planck Mass":
                outunit = unit.planck_mass
            if outunit == "Atomic Mass Unit":
                outunit = unit.atomic_mass_unit

            convert = str(unit.convert_to(inpunit, outunit).n())
            float_convert = re.sub('[*]' + str(outunit), "", convert)

            outputentry.delete(0, END)
            outputentry.insert(0, float_convert)

        input_mass = StringVar()
        input_mass.set(mass_units[0])
        output_mass = StringVar()
        output_mass.set(mass_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_mass, state='readonly')
        inputbox['values'] = mass_units
        outputbox = ttk.Combobox(self, textvariable=output_mass, state='readonly')
        outputbox['values'] = mass_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Temperature Page~~~~~~~~~~~~~~~~~~~~##
class TemperaturePage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Temperature Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_temp.get()
            outunit = output_temp.get()

            #----Celsius----#
            if inpunit == "Celsius" and outunit == "Fahrenheit":
                convert = (inp * 9/5) + 32
            elif inpunit == "Celsius" and outunit == "Kelvin":
                convert = (inp + 273.15)
            #----from Fahrenheit----#
            elif inpunit == "Fahrenheit" and outunit == "Celsius":
                convert = (inp - 32) * 5/9
            elif inpunit == "Fahrenheit" and outunit == "Kelvin":
                convert = (inp - 32) * 5/9 + 273.15
            #----From Kelvin----#
            elif inpunit == "Kelvin" and outunit == "Celsius":
                convert = (inp - 273.15)
            elif inpunit == "Kelvin" and outunit == "Fahrenheit":
                convert = (inp - 273.15) * 9/5 + 32

            outputentry.delete(0, END)
            outputentry.insert(0, convert)

        input_temp = StringVar()
        input_temp.set(temp_units[0])
        output_temp = StringVar()
        output_temp.set(temp_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_temp, state='readonly')
        inputbox['values'] = temp_units
        outputbox = ttk.Combobox(self, textvariable=output_temp, state='readonly')
        outputbox['values'] = temp_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Volume Page~~~~~~~~~~~~~~~~~~~~##
class VolumePage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Volume Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        volume_units = ['Milliliter', 'Centiliter', 'Deciliter', 'Liter', 'US Liquid Quart']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_volume.get()
            outunit = output_volume.get()

            # ----inputs----#
            if inpunit == "Milliliter":
                inpunit = inp * unit.milliliter
            if inpunit == "Centiliter":
                inpunit = inp * unit.centiliter
            if inpunit == "Deciliter":
                inpunit = inp * unit.deciliter
            if inpunit == "Liter":
                inpunit = inp * unit.liter
            if inpunit == "US Liquid Quart":
                inpunit = inp * unit.quart
            # ----outputs----#
            if outunit == "Milliliter":
                outunit = unit.milliliter
            if outunit == "Centiliter":
                outunit = unit.centiliter
            if outunit == "Deciliter":
                outunit = unit.deciliter
            if outunit == "Liter":
                outunit = unit.liter
            if outunit == "US Liquid Quart":
                outunit = unit.quart

            convert = str(unit.convert_to(inpunit, outunit).n())
            float_convert = re.sub('[*]' + str(outunit), "", convert)

            outputentry.delete(0, END)
            outputentry.insert(0, float_convert)

        input_volume = StringVar()
        input_volume.set(volume_units[0])
        output_volume = StringVar()
        output_volume.set(volume_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_volume, state='readonly')
        inputbox['values'] = volume_units
        outputbox = ttk.Combobox(self, textvariable=output_volume, state='readonly')
        outputbox['values'] = volume_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Energy Page~~~~~~~~~~~~~~~~~~~~##
class EnergyPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Energy Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        energy_units = ['Millijoule', 'Centijoule', 'Decijoule', 'Joule', 'Kilojoule', 'Megajoule',
                        'Electron Volt', 'Planck Energy']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_energy.get()
            outunit = output_energy.get()

            #------Introducing New Units------#
            millij = Quantity('milliJoule', abbrev='mj')
            millij.set_global_relative_scale_factor(milli, joule)
            millijoule = millij.convert_to(joule)
            centij = Quantity('centiJoule', abbrev='cj')
            centij.set_global_relative_scale_factor(centi, joule)
            centijoule = centij.convert_to(joule)
            decijo = Quantity('deciJoule', abbrev='dj')
            decijo.set_global_relative_scale_factor(deci, joule)
            decijoule = decijo.convert_to(joule)
            kiloj = Quantity('kiloJoule', abbrev='kj')
            kiloj.set_global_relative_scale_factor(kilo, joule)
            kilojoule = kiloj.convert_to(joule)
            megaj = Quantity('megaJoule', abbrev='mega j')
            megaj.set_global_relative_scale_factor(mega, joule)
            megajoule = megaj.convert_to(joule)

            # ----inputs----#
            if inpunit == "Joule":
                inpunit = inp * unit.joules
            if inpunit == "Electron Volt":
                inpunit = inp * unit.electronvolts
            if inpunit == "Planck Energy":
                inpunit = inp * unit.planck_energy
            if inpunit == "Kilojoule":
                inpunit = inp * kilojoule
            if inpunit == "Millijoule":
                inpunit = inp * millijoule
            if inpunit == "Centijoule":
                inpunit = inp * centijoule
            if inpunit == "Decijoule":
                inpunit = inp * decijoule
            if inpunit == "Megajoule":
                inpunit = inp * megajoule
            # ----outputs----#
            if outunit == "Joule":
                outunit = unit.joules
            if outunit == "Electron Volt":
                outunit = unit.electronvolts
            if outunit == "Planck Energy":
                outunit = unit.planck_energy
            if outunit == "Kilojoule":
                outunit = kilojoule
            if outunit == "Millijoule":
                outunit = millijoule
            if outunit == "Centijoule":
                outunit = centijoule
            if outunit == "Decijoule":
                outunit = decijoule
            if outunit == "Megajoule":
                outunit = megajoule

            convert = str((unit.convert_to(inpunit, outunit) / outunit).n())
            deci_float = float(convert)
            decimal = round(deci_float, 12)

            outputentry.delete(0, END)
            outputentry.insert(0, decimal)

        input_energy = StringVar()
        input_energy.set(energy_units[0])
        output_energy = StringVar()
        output_energy.set(energy_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_energy, state='readonly')
        inputbox['values'] = energy_units
        outputbox = ttk.Combobox(self, textvariable=output_energy, state='readonly')
        outputbox['values'] = energy_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Energy Page~~~~~~~~~~~~~~~~~~~~##
class PowerPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Power Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        power_units = ['Milliwatt', 'Centiwatt', 'Deciwatt', 'Watt', 'Kilowatt', 'Megawatt', 'Planck Power']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_power.get()
            outunit = output_power.get()

            #------Introducing New Units------#
            milliw = Quantity('milliWatt', abbrev='mw')
            milliw.set_global_relative_scale_factor(milli, watt)
            milliwatt = milliw.convert_to(watt)
            centiw = Quantity('centiWatt', abbrev='cw')
            centiw.set_global_relative_scale_factor(centi, watt)
            centiwatt = centiw.convert_to(watt)
            deciwa = Quantity('deciWatt', abbrev='dw')
            deciwa.set_global_relative_scale_factor(deci, watt)
            deciwatt = deciwa.convert_to(watt)
            kilow = Quantity('kiloWatt', abbrev='kw')
            kilow.set_global_relative_scale_factor(kilo, watt)
            kilowatt = kilow.convert_to(watt)
            megaw = Quantity('megaWatt', abbrev='mega w')
            megaw.set_global_relative_scale_factor(mega, watt)
            megawatt = megaw.convert_to(watt)

            # ----inputs----#
            if inpunit == "Watt":
                inpunit = inp * unit.watt
            if inpunit == "Planck Power":
                inpunit = inp * unit.planck_power
            if inpunit == "Kilowatt":
                inpunit = inp * kilowatt
            if inpunit == "Milliwatt":
                inpunit = inp * milliwatt
            if inpunit == "Centiwatt":
                inpunit = inp * centiwatt
            if inpunit == "Deciwatt":
                inpunit = inp * deciwatt
            if inpunit == "Megawatt":
                inpunit = inp * megawatt
            # ----outputs----#
            if outunit == "Watt":
                outunit = unit.watt
            if outunit == "Planck Power":
                outunit = unit.planck_power
            if outunit == "Kilowatt":
                outunit = kilowatt
            if outunit == "Milliwatt":
                outunit = milliwatt
            if outunit == "Centiwatt":
                outunit = centiwatt
            if outunit == "Deciwatt":
                outunit = deciwatt
            if outunit == "Megawatt":
                outunit = megawatt

            convert = str((unit.convert_to(inpunit, outunit) / outunit).n())
            deci_float = float(convert)
            decimal = round(deci_float, 12)

            outputentry.delete(0, END)
            outputentry.insert(0, decimal)

        input_power = StringVar()
        input_power.set(power_units[0])
        output_power = StringVar()
        output_power.set(power_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_power, state='readonly')
        inputbox['values'] = power_units
        outputbox = ttk.Combobox(self, textvariable=output_power, state='readonly')
        outputbox['values'] = power_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Current Page~~~~~~~~~~~~~~~~~~~~##
class CurrentPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Current Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        current_units = ['Milliampere', 'Centiampere', 'Deciampere', 'Ampere', 'Kiloampere', 'Megaampere',
                         'Planck Current']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_current.get()
            outunit = output_current.get()

            #------Introducing New Units------#
            millia = Quantity('milliAmpere', abbrev='ma')
            millia.set_global_relative_scale_factor(milli, ampere)
            milliampere = millia.convert_to(ampere)
            centia = Quantity('centiAmpere', abbrev='ca')
            centia.set_global_relative_scale_factor(centi, ampere)
            centiampere = centia.convert_to(ampere)
            decia = Quantity('deciAmpere', abbrev='da')
            decia.set_global_relative_scale_factor(deci, ampere)
            deciampere = decia.convert_to(ampere)
            kiloa = Quantity('kiloAmpere', abbrev='ka')
            kiloa.set_global_relative_scale_factor(kilo, ampere)
            kiloampere = kiloa.convert_to(ampere)
            megaa = Quantity('megaAmpere', abbrev='mega a')
            megaa.set_global_relative_scale_factor(mega, ampere)
            megaampere = megaa.convert_to(ampere)

            # ----inputs----#
            if inpunit == "Ampere":
                inpunit = inp * unit.ampere
            if inpunit == "Planck Current":
                inpunit = inp * unit.planck_current
            if inpunit == "Kiloampere":
                inpunit = inp * kiloampere
            if inpunit == "Milliampere":
                inpunit = inp * milliampere
            if inpunit == "Centiampere":
                inpunit = inp * centiampere
            if inpunit == "Deciampere":
                inpunit = inp * deciampere
            if inpunit == "Megaampere":
                inpunit = inp * megaampere
            # ----outputs----#
            if outunit == "Ampere":
                outunit = unit.ampere
            if outunit == "Planck Current":
                outunit = unit.planck_current
            if outunit == "Kiloampere":
                outunit = kiloampere
            if outunit == "Milliampere":
                outunit = milliampere
            if outunit == "Centiampere":
                outunit = centiampere
            if outunit == "Deciampere":
                outunit = deciampere
            if outunit == "Megaampere":
                outunit = megaampere

            convert = str((unit.convert_to(inpunit, outunit) / outunit).n())
            deci_float = float(convert)
            decimal = round(deci_float, 12)

            outputentry.delete(0, END)
            outputentry.insert(0, decimal)

        input_current = StringVar()
        input_current.set(current_units[0])
        output_current = StringVar()
        output_current.set(current_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_current, state='readonly')
        inputbox['values'] = current_units
        outputbox = ttk.Combobox(self, textvariable=output_current, state='readonly')
        outputbox['values'] = current_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Charge Page~~~~~~~~~~~~~~~~~~~~##
class ChargePage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Current Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        current_units = ['Millicoulomb', 'Centicoulomb', 'Decicoulomb', 'Coulomb', 'Kilocoulomb', 'Megacoulomb',
                         'Planck Charge', 'Elementary Charge']

        def convert():
            inp = float(inputentry.get())
            inpunit = input_current.get()
            outunit = output_current.get()

            # ------Introducing New Units------#
            millicb = Quantity('milliCoulomb', abbrev='mcb')
            millicb.set_global_relative_scale_factor(milli, coulomb)
            millicoulomb = millicb.convert_to(coulomb)
            centicb = Quantity('centiCoulomb', abbrev='ccb')
            centicb.set_global_relative_scale_factor(centi, coulomb)
            centicoulomb = centicb.convert_to(coulomb)
            decicb = Quantity('deciCoulomb', abbrev='dcb')
            decicb.set_global_relative_scale_factor(deci, coulomb)
            decicoulomb = decicb.convert_to(coulomb)
            kilocb = Quantity('kiloCoulomb', abbrev='kcb')
            kilocb.set_global_relative_scale_factor(kilo, coulomb)
            kilocoulomb = kilocb.convert_to(coulomb)
            megacb = Quantity('megaCoulomb', abbrev='mega cb')
            megacb.set_global_relative_scale_factor(mega, coulomb)
            megacoulomb = megacb.convert_to(coulomb)

            # ----inputs----#
            if inpunit == "Coulomb":
                inpunit = inp * unit.coulomb
            if inpunit == "Planck Charge":
                inpunit = inp * unit.planck_charge
            if inpunit == "Elementary Charge":
                inpunit = inp * unit.elementary_charge
            if inpunit == "Kilocoulomb":
                inpunit = inp * kilocoulomb
            if inpunit == "Millicoulomb":
                inpunit = inp * millicoulomb
            if inpunit == "Centicoulomb":
                inpunit = inp * centicoulomb
            if inpunit == "Decicoulomb":
                inpunit = inp * decicoulomb
            if inpunit == "Megacoulomb":
                inpunit = inp * megacoulomb
            # ----outputs----#
            if outunit == "Coulomb":
                outunit = unit.coulomb
            if outunit == "Planck Charge":
                outunit = unit.planck_charge
            if outunit == "Elementary Charge":
                outunit = unit.elementary_charge
            if outunit == "Kilocoulomb":
                outunit = kilocoulomb
            if outunit == "Millicoulomb":
                outunit = millicoulomb
            if outunit == "Centicoulomb":
                outunit = centicoulomb
            if outunit == "Decicoulomb":
                outunit = decicoulomb
            if outunit == "Megacoulomb":
                outunit = megacoulomb

            convert = str((unit.convert_to(inpunit, outunit) / outunit).n())
            deci_float = float(convert)
            decimal = round(deci_float, 12)

            outputentry.delete(0, END)
            outputentry.insert(0, decimal)

        input_current = StringVar()
        input_current.set(current_units[0])
        output_current = StringVar()
        output_current.set(current_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_current, state='readonly')
        inputbox['values'] = current_units
        outputbox = ttk.Combobox(self, textvariable=output_current, state='readonly')
        outputbox['values'] = current_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Time Page~~~~~~~~~~~~~~~~~~~~##
class TimePage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Time Converter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        time_units = ['Millisecond', 'Microsecond', 'Nanosecond', 'Picosecond', 'Second', 'Minute', 'Hour', 'Day',
                      'Common Year', 'Year', 'Tropical Year', 'Full Moon Cycle']

        def convert():
          inp = float(inputentry.get())
          inpunit = input_time.get()
          outunit = output_time.get()

           #----inputs----#
          if inpunit == "Millisecond":
              inpunit = inp*unit.millisecond
          if inpunit == "Microsecond":
              inpunit = inp*unit.microsecond
          if inpunit == "Nanosecond":
              inpunit = inp*unit.nanosecond
          if inpunit == "Picosecond":
              inpunit = inp*unit.picosecond
          if inpunit == "Second":
              inpunit = inp*unit.second
          if inpunit == "Minute":
              inpunit = inp*unit.minute
          if inpunit == "Hour":
              inpunit = inp*unit.hour
          if inpunit == "Day":
              inpunit = inp*unit.day
          if inpunit == "Common Year":
              inpunit = inp*unit.common_year
          if inpunit == "Year":
              inpunit = inp*unit.year
          if inpunit == "Tropical Year":
              inpunit = inp*unit.tropical_year
          if inpunit == "Full Moon Cycle":
              inpunit = inp*unit.full_moon_cycle

      #----outputs----#
          if outunit == "Millisecond":
              outunit = unit.millisecond
          if outunit == "Microsecond":
              outunit = unit.microsecond
          if outunit == "Nanosecond":
              outunit = unit.nanosecond
          if outunit == "Picosecond":
              outunit = unit.picosecond
          if outunit == "Second":
              outunit = unit.second
          if outunit == "Minute":
              outunit = unit.minute
          if outunit == "Hour":
              outunit = unit.hour
          if outunit == "Day":
              outunit = unit.day
          if outunit == "Common Year":
              outunit = unit.common_year
          if outunit == "Year":
              outunit = unit.year
          if outunit == "Tropical Year":
              outunit = unit.tropical_year
          if outunit == "Full Moon Cycle":
              outunit = unit.full_moon_cycle

          convert = str(unit.convert_to(inpunit, outunit).n())
          float_convert = re.sub('[*]' + str(outunit), "", convert)

          outputentry.delete(0, END)
          outputentry.insert(0, float_convert)

        input_time = StringVar()
        input_time.set(time_units[0])
        output_time = StringVar()
        output_time.set(time_units[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3")
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3")
        inputbox = ttk.Combobox(self, textvariable=input_time, state='readonly')
        inputbox['values'] = time_units
        outputbox = ttk.Combobox(self, textvariable=output_time, state='readonly')
        outputbox['values'] = time_units

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        ##-----------------Buttons and Entries-----------------##
        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

      ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

        ##~~~~~~~~~~~~~~~~~~~~Number Base Page~~~~~~~~~~~~~~~~~~~~##
class NumberBasePage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 25, text="Number Base", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        num = IntVar()
        lblbinary = StringVar()
        lbldecimal = StringVar()
        lblhexa = StringVar()
        lbloctal = StringVar()

        def convert():
            lblbinary.set(str(bin(num.get())))
            lbldecimal.set(str(num.get()))
            lblhexa.set(str(hex(num.get())))
            lbloctal.set(str(oct(num.get())))

        def clear():
            num.set(0)
            lblhexa.set('')
            lblbinary.set('')
            lbldecimal.set('')
            lbloctal.set('')

        self.__my_canvas.create_text(95, 90, text="Enter Number", fill='#d3fff3',
                                     justify="center", font=('LL Karatula', 15))
        self.__my_canvas.create_text(95, 140, text="Binary", fill='#d3fff3',
                                     justify="center", font=('LL Karatula', 15))
        self.__my_canvas.create_text(95, 190, text="Decimal", fill='#d3fff3',
                                     justify="center", font=('LL Karatula', 15))
        self.__my_canvas.create_text(95, 240, text="Hexa Decimal", fill='#d3fff3',
                                     justify="center", font=('LL Karatula', 15))
        self.__my_canvas.create_text(95, 290, text="Octal", fill='#d3fff3',
                                     justify="center", font=('LL Karatula', 15))

        display_input = Entry(self, font=("Aileron SemiBold", 12), background="#6A94B5", foreground="#D3FFF3",
                              insertwidth=1, width=15, justify="left",textvariable=num)
        display_output1 = Entry(self, font=("Aileron SemiBold", 12), background="#6A94B5", foreground="#D3FFF3",
                                insertwidth=1, width=15, justify="right",textvariable=lblbinary)
        display_output2 = Entry(self, font=("Aileron SemiBold", 12), background="#6A94B5", foreground="#D3FFF3",
                                insertwidth=1, width=15, justify="right",textvariable=lbldecimal)
        display_output3 = Entry(self, font=("Aileron SemiBold", 12), background="#6A94B5", foreground="#D3FFF3",
                                insertwidth=1, width=15, justify="right",textvariable=lblhexa)
        display_output4 = Entry(self, font=("Aileron SemiBold", 12), background="#6A94B5", foreground="#D3FFF3",
                                insertwidth=1, width=15, justify="right",textvariable=lbloctal)

        btn_convert = Button(self, text="Convert", padx=5, pady=3, width=20, height=1, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)
        btn_clear =  Button(self, text="Clear", padx=5, pady=3, width=20, height=1, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=clear)

        self.__my_canvas.create_window(300, 90, anchor="center", window=display_input)
        self.__my_canvas.create_window(300, 140, anchor="center", window=display_output1)
        self.__my_canvas.create_window(300, 190, anchor="center", window=display_output2)
        self.__my_canvas.create_window(300, 240, anchor="center", window=display_output3)
        self.__my_canvas.create_window(300, 290, anchor="center", window=display_output4)

        self.__my_canvas.create_window(110, 332, anchor="center", window=btn_convert)
        self.__my_canvas.create_window(300, 332, anchor="center", window=btn_clear)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Morse Code Page~~~~~~~~~~~~~~~~~~~~##
class MorseCodePage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 40, text=f"Morse Code\nEncrypter/Decrypter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        morse_code_dict = {'A': '.-', 'B': '-...',
                           'C': '-.-.', 'D': '-..', 'E': '.',
                           'F': '..-.', 'G': '--.', 'H': '....',
                           'I': '..', 'J': '.---', 'K': '-.-',
                           'L': '.-..', 'M': '--', 'N': '-.',
                           'O': '---', 'P': '.--.', 'Q': '--.-',
                           'R': '.-.', 'S': '...', 'T': '-',
                           'U': '..-', 'V': '...-', 'W': '.--',
                           'X': '-..-', 'Y': '-.--', 'Z': '--..',
                           '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....',
                           '7': '--...', '8': '---..', '9': '----.',
                           '0': '-----', ', ': '--..--', '.': '.-.-.-',
                           '?': '..--..', '/': '-..-.', '-': '-....-',
                           '(': '-.--.', ')': '-.--.-'}

        def encrypt():
            text = str(message.get()).upper()
            cipher = ''
            for letter in text:
                if letter != ' ':
                    cipher += morse_code_dict[letter] + ' '
                    outputentry.delete(0, END)
                    outputentry.insert(0, cipher)
                else:
                    cipher += ' '
                    outputentry.delete(0, END)
                    outputentry.insert(0, cipher)

        def decrypt():
            text = str(message.get())
            text += ' '
            decipher = ''
            citext = ''
            letter: object
            for letter in text:
                if letter != ' ':
                    i = 0
                    citext += letter
                else:
                    i += 1
                    if i == 2:
                        decipher += ' '
                    else:
                        decipher += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(citext)]
                        citext = ''
                        outputentry.delete(0, END)
                        outputentry.insert(0, decipher)

        message = StringVar()

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 10),
                           background="#6A94B5", foreground="#D3FFF3", textvariable=message)
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 10),
                            background="#6A94B5", foreground="#D3FFF3")

        btn_encrypt = Button(self,
                             text="Encrypt", padx=5, pady=3, width=20, height=1, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=encrypt)
        btn_decrypt = Button(self,
                             text="Decrypt", padx=5, pady=3, width=20, height=1, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=decrypt)

        self.__my_canvas.create_text(200, 120, text="Input", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 15))
        self.__my_canvas.create_text(200, 230, text="Output", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 15))
        self.__my_canvas.create_window(200, 150, width=350, height=25, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 260, width=350, height=25, anchor="center", window=outputentry)
        self.__my_canvas.create_window(300, 330, anchor="center", window=btn_encrypt)
        self.__my_canvas.create_window(100, 330, anchor="center", window=btn_decrypt)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~Decimal to Fraction Page~~~~~~~~~~~~~~~~~~~~##
class DecimaltoFractionPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)

        ##-----------------Background-----------------##
        self.__bg = (Image.open("whitelotus.png"))
        self.__my_canvas = Canvas(self, width=400, height=400)
        self.__my_canvas.pack(fill="both", expand=TRUE)

        self.__resized_image = self.__bg.resize((500, 800))
        self.__new_image = ImageTk.PhotoImage(self.__resized_image)
        self.__my_canvas.create_image(197, 55, image=self.__new_image)

        self.__my_canvas.create_text(200, 40, text=f"Decimal - Fraction\nConverter", fill='#d3fff3', justify="center",
                                     font=('LL Karatula', 24))

        ##-----------------Combobox and Conversion-----------------##
        number = ['Decimal', 'Fraction']

        def convert():
            inpunit = input_num.get()
            outunit = output_num.get()

            if inpunit == "Decimal" and outunit == "Fraction":
                inp = float(inputentry.get())
                converted = Fraction(inp).limit_denominator()
            elif inpunit == "Fraction" and outunit == "Decimal":
                inp = inputentry.get()
                fract = Fraction(inp).limit_denominator()
                deci_float = float(fract)
                decimal = round(deci_float, 12)
                converted = decimal
            else:
                converted = "Syntax Error"

            outputentry.delete(0, END)
            outputentry.insert(0, converted)

        input_num = StringVar()
        input_num.set(number[0])
        output_num = StringVar()
        output_num.set(number[0])

        self.__my_canvas.create_text(200, 160, text="=", fill='#d3fff3', justify="center",
                                     font=('Montserrat SemiBold', 30))

        inputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                           background="#6A94B5", foreground="#D3FFF3",)
        outputentry = Entry(self, justify="left", font=('Roboto Medium', 14),
                            background="#6A94B5", foreground="#D3FFF3",)
        inputbox = ttk.Combobox(self, textvariable=input_num, state='readonly')
        inputbox['values'] = number
        outputbox = ttk.Combobox(self, textvariable=output_num, state='readonly')
        outputbox['values'] = number

        btn_convert = Button(self,
                             text="Convert", padx=5, pady=3, width=20, height=2, font=('Roboto Medium', 9),
                             bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                             command=convert)

        self.__my_canvas.create_window(200, 130, anchor="center", window=inputbox)
        self.__my_canvas.create_window(200, 106, anchor="center", window=inputentry)
        self.__my_canvas.create_window(200, 220, anchor="center", window=outputbox)
        self.__my_canvas.create_window(200, 196, anchor="center", window=outputentry)
        self.__my_canvas.create_window(200, 330, anchor="center", window=btn_convert)

        ##-----------------Back Button to Converter Main Page-----------------##
        btn_back2 = Button(self, text="Back", padx=5, pady=3, width=20, font=('Roboto Medium', 9),
                           bg="#6A94B5", fg="#D3FFF3", activebackground="#466D86", activeforeground="#D3FFF3",
                           command=lambda: MASTER.switch_frame(ConverterPage))

        self.__my_canvas.create_window(200, 375, anchor="center", window=btn_back2)

    ##~~~~~~~~~~~~~~~~~~~~To-do Work Page~~~~~~~~~~~~~~~~~~~~##
class WorkPage(Frame):
    def __init__(self, MASTER):
        super().__init__(MASTER)


"--------------------------------------------------------------------"

Window().mainloop()