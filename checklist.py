import sys
sys.stdout.write("\033[0;95m")

checklist = list()  # creates Checklist

#define functions


def create(item):  # creates item
    checklist.append(item)  # adds it to the checklist


def read(index):  # reads the items at each index
    item = checklist[index]
    return item


def update(index, item):  # replaces index with item
    checklist[index] = item


def destroy(index):  # destroys whatever is at this index
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# def mark_completed(index): # Add code here that marks an item as completed


def select(function_code):
    #create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
    
    #read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        
        #remember thet the item_index must actually exist or program will crash
        read(item_index)
        
    #print all items
    elif function_code == "P":
        list_all_items()
        
    elif function_code == "Q":
        #this is where we want to stop our loop
        return False

    #catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    #the input function will display a message in the terminal
    #and wait for user input
    user_input = input(prompt)
    return user_input
    user_value = user_input("Please enter a value:")
    print(user_value)

#test functions
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))
    list_all_items()

#runs tests
test()

running = True
while running: #conditional that keeps it running while True or until False
    selection = user_input(
        "Press C to add to list, R to read from list, P to display list, and Q to quit ")
    running = select(selection)
