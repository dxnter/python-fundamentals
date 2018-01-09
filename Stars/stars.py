# Part I
def draw_stars(x):
    for number in range(len(x)):
        print '*' * x[number]

draw_stars([4, 6, 1, 3, 5, 7, 25])

# Part II
def draw(x):
    for number in range(len(x)):
        if type(x[number]) is str:
            print (x[number][0].lower()) * len(x[number])
        elif type(x[number]) is int:
            print '*' * x[number]

draw([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])