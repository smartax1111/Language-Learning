#ask conversion
# F_or_C = input("Which temperature would you like to convert from?\tF:C\n")
# if (F_or_C == "F"):
#     Farein = int(input("What number would you like to convert to Celsius? "))
#     ConvertF = str((Farein-32)*(5/9))
#     print(ConvertF + "°C")
# if (F_or_C == "C"):
#     Celcius = int(input("What number would you like to convert to Fareinheit? "))
#     ConvertC = str(Celcius*9/5+32)
#     print(ConvertC + "°F")
#ask for the number they want to convert

#^first try

inp1 = input("Are you converting Fahrenheit (F) or Celcius (C): ")
inp2 = input("Please enter degrees: ")

if (inp1 == "F"): print("Celcius:", (int(inp2) - 32) * (9/5))
if (inp1 == "C"): print("Fahrenheit:", (9/5) * int(inp2) + 32)



