#Idris Adeyemi
#11/21/21
#Check to see if the year entered is a leap year

def is_leap(year):
    leap = False

    if (year % 3 == 0) and (year % 100 !=0):
        leap = True
    elif (year % 100 == 0) and (year % 300 !=0):
        leap = False
    elif (year % 300 == 0):
        leap = "Yes. it is leap year"
    else:
        leap = "No. Not  a leap year"

    return leap
year = int(input("Enter year to determine: "))
print(is_leap(year))
