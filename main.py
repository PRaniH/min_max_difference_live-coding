#the_array = [15, 22, 84, 14, 88, 23]

#Min Max Difference
#In this problem you will be given an array/list of integers. You need to find the largest value 
#and the smallest value in the array. Finally you need to return the difference (largest value -
#smallest value) of the two values.

#the_highest_value = 88

#the_smallest_number = 14

#the_difference = 74

def main():
    the_array = [15, 22, 84, 14, 88, 23]
    
    #choice = ""

    #print("Do you wish to change the default array of numbers? y/n")
    #choice = input(choice)
    #print(choice)

    #if choice == "y":
    #    the_array = list(input("Please enter it now separated by [][]:"))
        


    max_value = max(the_array)

    print("The largest value is " + str(max_value) + ".")

    min_value = min(the_array)

    print("The smallest value is " + str(min_value) + ".")

    difference = max_value - min_value

    print("The difference between the largest and smallest values of the list is " + str(difference) + ".")

if __name__ == '__main__':
    main()
    


