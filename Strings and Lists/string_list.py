import numpy as np

words = "It's thanksgiving day. It's my birthday too!"
print words.find("day")

new_words = words.replace("day", "month")
print new_words

x = [2,54,-2,7,12,98]
print (max(x))
print (min(x))

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[-1]
new_list = [y[0], y[-1]]
print new_list

last_list = [19,2,54,-2,7,12,98,32,10,-3,6]
sorted_list = sorted(last_list)
print sorted_list
split_list = np.array_split(sorted_list, 2)
print split_list