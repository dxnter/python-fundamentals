danny = {'name' : 'Danny', 'age' : 20, 'country' : 'The United States', 'language' : 'Python'}
def user_info(x):
    print 'My name is',x['name']
    print 'My age is',x['age']
    print 'My country of birth is',x['country']
    print 'My favorite language is',x['language']

user_info(danny)