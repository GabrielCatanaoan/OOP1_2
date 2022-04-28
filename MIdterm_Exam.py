from tkinter import *

window=Tk()
window.title('Special Midterm Exam in OOP')
window.geometry('500x400')

button=Button(window,text='Click to Change Color',activebackground='yellow')
button.place(relx=.5,rely=.5,anchor='center')

window.mainloop()


def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32
 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15
 class FarenheitToCelsius(TemperatureConversion):
     def conversion(self):
         return (self._temp - 32)*(5/9)
 class KelvinToCelsius(TemperatureConversion):
     def conversion(self):
         return (self._temp - 273.15)


 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")
 tempInFarenheit = float(input("Enter the temperature in Farenheit: "))
 convert = FarenheitToCelsius(tempInFarenheit)
 print(str(convert.conversion()) + " Celsius")
 tempInKelvin= float(input("Enter the Temperature in Kelvin: "))
 convert = KelvinToCelsius(tempInKelvin)
 print(str(convert.conversion()) + " Celsius")

main()




