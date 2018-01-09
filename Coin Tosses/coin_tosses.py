import random

def coin_toss():
    head_count = 0
    tail_count = 0
    for attempt in range(1,5001):
        random_int = round(random.uniform(0,1))
        if random_int > 0:
            head_count += 1
            print "Attempt #",attempt,': Throwing a coin... It\'s a head! ... Got',head_count,'head(s) so far and',tail_count,'tail(s) so far'
        if random_int <= 0:
            tail_count += 1
            print "Attempt #",attempt,': Throwing a coin... It\'s a tail! ... Got',head_count,'tail(s) so far and',tail_count,'tail(s) so far'
    print 'Ending the program, thank you!'
    
coin_toss()