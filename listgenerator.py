def CreateRandomList(howlong:int = 1000):
    """  This function creates and returns a list of random tuples (x, y) where x is the category name, color, fruit or number and y is the value. Since
    it's a randomlist, there are repeats many times. E.g. [("name", "Rag"), ("color", "red")]"""
    import random
    random_list = []
    names = ['Steve', 'Bob', 'David', 'Rachana', 'Zach', 'Mike', 'Josh', 'Scott', 'Jenn', 'Cathy', 'Sharon', 'Zack', 'Carol', 'Olive', 'Violet']
    colors = ["red", "blue", "orange", "yellow", "green", "light blue", "white", "black", "pink", "purple", "cyan", "magenta", "indigo", "olive", "violet"]
    fruits = ["orange","olive","strawberry","apricot","watermelon","banana","grapes","avocado","blueberries","blackberries","cherries","cranberries","figs","guava","grapefruit","lemon"]
    numbers = [5, 26, 19, 85, 18, 20, 78, 64, 33, 1, 35, 52, 4, 75, 94, 77, 38, 34, 87, 55]
    for i in range(0,howlong):
        catagory = random.randint(1,4)
        if catagory == 1:
            index_names = random.randint(0,(len(names)-1))
            random_list.append(("name",names[index_names]))
        elif catagory == 2:
            index_colors = random.randint(0,(len(colors)-1))
            random_list.append(("color",colors[index_colors]))
        elif catagory == 3:
            index_fruits = random.randint(0,(len(fruits)-1))
            random_list.append(("fruit",fruits[index_fruits]))
        elif catagory == 4:
            index_numbers = random.randint(0,(len(numbers)-1))
            random_list.append(("number",numbers[index_numbers]))
#    print(random_list)
    return random_list
