# leap year program
# leap year if it is divisible by 4 AND not divisible by 100
# OR divisible by 400
year = int(input( "What year? "))
isLeap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print ("Is it a leap year?", isLeap)