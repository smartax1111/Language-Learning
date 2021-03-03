def sleep_in(weekday, vacation):
  if(weekday == 'Y'):
    if(vacation == 'N'):
      print("We do not sleep in :(")
    if(vacation == 'Y'):
      print("You can't be on vacation on weekdays")
  if(weekday == 'N'):
    if(vacation == 'Y' or vacation == 'N'):
      print("We sleep in!")

sleep_in(input("Is it a weekday? Y/N: "), input("Are you on vacation? Y/N: "))