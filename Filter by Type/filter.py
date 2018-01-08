def filter_type(x):
    if type(x) is int:
        if x >= 100:
            print "That's a big number!"
        elif x < 100:
            print "That's a small number"
    if type(x) is str:
        if len(x) >= 50:
            print "Long sentence"
        elif len(x) < 50:
            print "Short sentence"
    if type(x) is list:
        if len(x) >= 10:
            print "Big list"
        if len(x) < 10:
            print "Short list"

filter_type(['name','address','phone number','social security number'])