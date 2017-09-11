list = ["one", "two", "three", "four"]

my_iterator = iter(list)

for element in range(len(list)):
    next_item = next(my_iterator)
    print(next_item)
