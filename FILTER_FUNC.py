# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Input list
numbers2 = [1,2,3,4,5,6,7,8,9,10,11]
#numbers = [1, 2, 3, 4, 5, 6]
#even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)  # Output: [2, 4, 6]

en1 = filter(is_even,numbers2)
print(list(en1))
en2 = filter(lambda x : x%2 != 0,numbers2)
print(list(en2))