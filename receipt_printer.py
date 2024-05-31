#! /home/frijol/Desktop/no_recollection/venv/bin python

import serial
import adafruit_thermal_printer

uart = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.16)
printer = ThermalPrinter(uart)
printer._set_charset(1)

# execute au lancement
def test_print():
    printer.flush()
    printer.feed(2) # lignes vides
    printer.print("HELLO WORLD")
    printer.feed(2)

# imprime la reponse. tu peux ajouter du style ici
def print_answer(gpt_answer):
    printer.flush()
    printer.feed(3)
    printer.print(gpt_answer, encoding="cp437")
    printer.feed(3)