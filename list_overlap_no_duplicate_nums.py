import random
import os
play = True

while play == True:


	list_one_size = random.randint(10,20)
	list_two_size = random.randint(10,20)
	list_one = []
	list_two = []
	common_list = []
	x = range(1,list_one_size)
	for elem in x:
		
		num = random.randint(1,20)

		list_one.append(num)


	y = range(1,list_two_size)
	for elem in y:
		
		num_2 = random.randint(1,20)

		list_two.append(num_2)

	list_one_length = len(list_one)
	list_two_length = len(list_two)

	if list_one_length > list_two_length:
		for item in list_one:

			if item in list_two and item not in common_list:
				common_list.append(item)

	if list_two_length > list_one_length:
		for item in list_two:

			if item in list_one and item not in common_list:
				common_list.append(item)



	list_one_p = "List 1: "+ str(list_one)
	list_two_p = "List 2: "+ str(list_two)
	common_list_p = "Overlapping Numbers: " + str(common_list)


	print("")
	print(list_one_p)
	print("")
	print(list_two_p)
	print("")

	print(common_list_p)


	print("")
	play_again = input('Do you want to play again? "Yes" or "No": ')

	if play_again == "yes":
		play = True
		os.system('clear')
	else:
		print("Thanks for playing!")
		play = False