year=int(input("input:"))
#year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} yes".format(year))
       else:
           print("{0} not".format(year))
   else:
       print("{0} yes".format(year))
else:
   print("{0} not".format(year))
