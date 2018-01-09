# Odd / Even
def odd_even():
    for number in range(1, 2001):
        if number % 2 == 0:
            print "Number is {}. This is an even number".format(number)
        elif number % 2 != 0:
            print "Number is {}. This is an odd number".format(number)

# Multiply
a = [2,3,10,16]
def multiply(list, multi):
    for number in range(len(list)):
        list[number] = list[number] * multi
    print list
