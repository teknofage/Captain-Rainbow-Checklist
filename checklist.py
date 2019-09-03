# print('Hello World')
checklist = list()

checklist.append('Blue')
print(checklist)

checklist.append('Orange')
print(checklist)
print(checklist)

checklist = ['Blue', 'Cats']
checklist.pop(1)
print(checklist)


def my_fun_function(say_this):
	print(say_this)
	my_fun_function('Hello World')


def create(item):
	checklist.append(item)
	checklist[0]


def read(index):
	print(checklist[index])
	return checklist[index]


def update(index, item):
	checklist[index] = item


def destroy(index):
	checklist.pop(index)


def list_all_items():
	index = 0
	for list_item in checklist:
		print("{} {}".format(index, list_item))
		index += 1


def select(function_code):
   	# Create item
	if function_code == "C":
		input_item = user_input("Input item:")
		create(input_item)

   	# Read item
	elif function_code == "R":
		item_index = int(user_input("Index Number?"))

		# Remember that item_index must actually exist or our program will crash.
		read(item_index)

   	# Print all items
	elif function_code == "P":
		list_all_items()
  
	elif function_code == "Q":
		return False

	# Catch all
	else: 
	 	print("Unknown Option")
   
	return True  

	 
	
	
def user_input(prompt):
	user_input = input(prompt)
	return user_input


def test():
	create("purple sox")
	create("red cloak")
	print(read(0))
	print(read(1))
	update(0, "purple socks")
	destroy(1)
	print(read(0))
	print(read(1))
	list_all_items()
	select("C")
	list_all_items()
	select("R")
	list_all_items()
	user_value = user_input("Please Enter a value:")
	print(user_value)
 
test()

running = True
while running:
	selection = user_input("Press C to add to list, R to Read from list and P to display list")
	running = select(selection)
