year=int(input("input:"))
#year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{ yes")
       else:
           print(" not")
   else:
       print("yes")
else:
   print("not")
   
