#fizzbuzz
# Write a short program that prints each number from 1 to 100 on a new line. 
# For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

# for [Temporary variable] in [sequence]:
#      [do something]
# range() function used to generate a sequence between the given values.
for i in range(1, 101): #for loop
    
    if i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    #if i is divisble by 3 and 5, print FizzBuzz
    elif i%3==0:
        print('Fizz')
    #if i is divisble by 3 print Fizz
    elif i%5==0:
        print('Buzz')
    #if i is divisble by 5 print Buzz
    else:
        print(i)