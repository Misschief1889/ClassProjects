from datetime import datetime
from dateutil.parser import parse
from dateutil import parser as date_parser
from bs4 import BeautifulSoup
import requests

#Get Month and date
def GetDate(M, D):
  DateExists = False
  while DateExists == False:
    BirthDate = input("Please give your date of birth in YY-MM-DD format:\n")
    if validate(BirthDate) == False:
      print('Date Format Incorrect. Please Re-Enter.')
      continue
    else:
      ParsedDate = parse(BirthDate)
      M = ParsedDate.month
      D = ParsedDate.day
      print('Thank you for that!')
      DateExists = True
      return M, D
    
#Check Formatting and validity of date
def validate(date_str):
    try:
        return bool(date_parser.parse(date_str))
    except ValueError:
        return False
    try:
        return bool(datetime.strptime(date_str, '%Y-%m-%d'))
    except ValueError:
        return False


#Iterate though month and date combos to determine star sign and assign to the appropriate number
def CheckSign(MonthOfBirth, DayOfBirth):
  Starsign = 0
  SignIs = 0
  while Starsign == 0:
    if MonthOfBirth == 1:
      if DayOfBirth >= 1 and DayOfBirth <= 19 :
        Starsign += 10
        SignIs = "Capricorn"
        return Starsign, SignIs
      if DayOfBirth >= 20 and DayOfBirth <= 31:
        Starsign += 11
        SignIs = "Aquarius"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 2:
      if DayOfBirth >= 1 and DayOfBirth <= 18 :
        Starsign += 11
        SignIs = "Aquarius"
        return Starsign, SignIs
      if DayOfBirth >= 19 and DayOfBirth <= 29:
        Starsign += 12
        SignIs = "Pisces"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 3:
      if DayOfBirth >= 1 and DayOfBirth <= 20 :
        Starsign += 12
        SignIs = "Pisces"
        return Starsign, SignIs
      if DayOfBirth >= 21 and DayOfBirth <= 30:
        Starsign += 1
        SignIs = "Aires"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 4:
      if DayOfBirth >= 1 and DayOfBirth <= 19 :
        Starsign += 1
        SignIs = "Aires"
        return Starsign, SignIs
      if DayOfBirth >= 20 and DayOfBirth <= 30:
        Starsign += 2
        SignIs = "Taurus"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 5:
      if DayOfBirth >= 1 and DayOfBirth <= 20 :
        Starsign += 2
        SignIs = "Taurus"
        return Starsign, SignIs
      if DayOfBirth >= 21 and DayOfBirth <= 31:
        Starsign += 3
        SignIs = "Gemini"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 6:
      if DayOfBirth >= 1 and DayOfBirth <= 21 :
        Starsign += 3
        SignIs = "Gemini"
        return Starsign, SignIs
      if DayOfBirth >= 21 and DayOfBirth <= 30:
        Starsign += 4
        SignIs = "Cancer"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 7:
      if DayOfBirth >= 1 and DayOfBirth <= 22 :
        Starsign += 4
        SignIs = "Cancer"
        return Starsign, SignIs
      if DayOfBirth >= 23 and DayOfBirth <= 31:
        Starsign += 5
        SignIs = "Leo"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 8:
      if DayOfBirth >= 1 and DayOfBirth <= 23 :
        Starsign += 5
        SignIs = "Leo"
        return Starsign, SignIs
      if DayOfBirth >= 24 and DayOfBirth <= 31:
        Starsign += 6
        SignIs = "Virgo"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 9:
      if DayOfBirth >= 1 and DayOfBirth <= 22 :
        Starsign += 6
        SignIs = "Virgo"
        return Starsign, SignIs
      if DayOfBirth >= 23 and DayOfBirth <= 30:
        Starsign += 7
        SignIs = "Libra"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 10:
      if DayOfBirth >= 1 and DayOfBirth <= 23 :
        Starsign += 7
        SignIs = "Libra"
        return Starsign, SignIs
      if DayOfBirth >= 24 and DayOfBirth <= 31:
        Starsign += 8
        SignIs = "Scorpio"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 11:
      if DayOfBirth >= 1 and DayOfBirth <= 21 :
        Starsign += 8
        SignIs = "Scorpio"
        return Starsign, SignIs
      if DayOfBirth >= 21 and DayOfBirth <= 30:
        Starsign += 9
        SignIs = "Sagittarius"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    if MonthOfBirth == 12:
      if DayOfBirth >= 1 and DayOfBirth <= 21 :
        Starsign += 9
        SignIs = "Sagittarius"
        return Starsign, SignIs
      if DayOfBirth >= 22 and DayOfBirth <= 30:
        Starsign += 10
        SignIs = "Capricorn"
        return Starsign, SignIs
      else:
        DayOfBirth = int(input("Please enter a valid date of birth:\n"))
        continue
    else: 
      MonthOfBirth = int(input("Please enter a valid month of birth:\n"))
      continue


#uses starsign number to find horoscope, print.
def GetHoroscope(sign):
  url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + sign
  html_content = requests.get(url).text
  soup = BeautifulSoup(html_content, "html.parser")
  print(soup.find('p').text)

#Uses starsign number to find yesterday's horoscope and print.
def GetYesterday(sign):
  url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-yesterday.aspx?sign=" + sign
  html_content = requests.get(url).text
  soup = BeautifulSoup(html_content, "html.parser")
  print(soup.find('p').text)

#Uses starsign number to find tomorrow's horoscope and print.
def GetTomorrow(sign):
  url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-tomorrow.aspx?sign=" + sign
  html_content = requests.get(url).text
  soup = BeautifulSoup(html_content, "html.parser")
  print(soup.find('p').text)