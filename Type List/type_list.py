def type_list(x):
    total_sum = 0
    final_string = ''
    for value in range(len(x)):
        if type(x[value]) is int or type(x[value]) is float:
            total_sum += x[value]
        if type(x[value]) is str:
            final_string += x[value] + ' '
    if len(final_string) > 0 and total_sum > 0:
        print "The list you entered is of mixed type"
    elif len(final_string) > 0 and total_sum == 0:
        print "The list you entered is of string type"
    elif len(final_string) == 0 and total_sum > 0:
        print "The list you entered is of integer type"
    if len(final_string) > 0:
        print "String:",final_string
    if total_sum > 0:
        print "Sum:",total_sum

type_list([1,44,3.5,"string"])