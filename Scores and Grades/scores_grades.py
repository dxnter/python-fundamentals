import random

def scores_and_grades():
    for test in range(10):
        random_num = random.randint(60, 100)
        if random_num >= 90:
            print 'Score:',random_num,'; Your grade is A'
        elif random_num <= 89 and random_num >= 80:
            print 'Score:',random_num,'; Your grade is B'
        elif random_num <= 79 and random_num >= 70:
            print 'Score:',random_num,'; Your grade is C'
        elif random_num <= 69 and random_num >= 60:
            print 'Score:',random_num,'; Your grade is D'
            
scores_and_grades()