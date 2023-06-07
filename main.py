#Import needed modules
import datetime
from CheckSign import *


#Global variables for later
M = 0
D = 0
ReadingHoroscope = 1

#Start a while loop, ask for dob and validate, call check for starsign, return a starsign number. Then ask if they want to read tomorrow's horoscope, yesterday's, or start over.
while ReadingHoroscope == 1:
  MonthOfBirth, DayOfBirth = GetDate(M, D)
  StarNum, SignIs = CheckSign(MonthOfBirth, DayOfBirth)
  print("Your star sign is " + SignIs + ". Here is today's horoscope!\n")
  GetHoroscope(str(StarNum))
  while ReadingHoroscope == 1:
    WhichScope = input("\nWould you like to read another horoscope?\nY=Yesterday's\nT=Tomorrow's\nN=Enter a new birthdate\nE=End the program\n")
    if WhichScope == "Y":
      GetYesterday(str(StarNum))
      continue
    if WhichScope == 'T':
      GetTomorrow(str(StarNum))
      continue
    if WhichScope == "N":
      break
    if WhichScope == "E":
      print("Thank you for playing! ^.^")
      ReadingHoroscope = 0
      break
    else:
      print("Please enter a valid response.")