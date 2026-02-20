# both julian and gregorian calendars hav programmers day on 13 september if not in leapyear else on 12 september
def programmer(year):
    if year == 1918:
        return "26.09.1918"
    elif year < 1918:
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"       
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
                
year = 2017
print(programmer(year))

