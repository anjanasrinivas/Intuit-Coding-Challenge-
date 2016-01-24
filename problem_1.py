

lst = [1,10,5,63,29,71,10,12,44,29,10,-1]


def sorted_list(lst): 
	for i in range (len(lst)): 
		for j in range (len(lst)-1-i): 
			if lst[j] > lst[j+1]: 
				lst [j], lst[j+1] = lst[j+1], lst[j]
sorted_list(lst)
print(lst)

#Using python built in feature to sort
def sort(lst): 
	lst.sort() 


