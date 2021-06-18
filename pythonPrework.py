# Question 1

def hello_name(user_name):
    print(f"hello_{user_name}")

hello_name("user_name")

# Question 2

start, end = 0, 100

# iterating each number in list
for num in range(start, end + 1):
	
	# checking condition
	if num % 2 != 0:
		print(num, end = "100 ")

# first_odd_numbers(100)

# Question 3
def max_num_in_list(a_list):
    return(max(a_list))

l1 = [1, 2, 77, 5, 12]
m1 = max_num_in_list(l1)
print(m1)

#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# print(is_leap_year(2000))

# Question 5
# with integers within given range

def checkConsecutive(l):
	return sorted(l) == list(range(min(l), max(l)+1))
	
# Driver Code
lst = [2, 3, 1, 4, 5]
print(checkConsecutive(lst))



print(is_consecutive(l1))
