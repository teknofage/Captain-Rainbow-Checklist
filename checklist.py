checklist = list()

def create(item): #creates item 
	checklist.append(item) #adds it to the checklist
	
def read(index): #reads the items at each index
	item = checklist[index]
	return item

def update(index,item): #replaces index with item
	checklist[index] = item
	
def destroy(index): #destroys whatever is at this index
	checklist.pop(index)
	
def list_all_items():
	for list_item in checklist:
		print(list_item)
    

def test():
	create("purple sox")
	create("red cloak")

	print(read(0))
	print(read(1))

	update(0, "purple socks")
	destroy(1)

	print(read(0))
	# print(read(1))

test()
