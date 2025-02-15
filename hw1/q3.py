# Question 3 = Return Array with only odd elements
# Chose to use Python instead of Java
# See test print statements

def SpOdd(array):
  odd_only = []
  for i in array:
    if i % 2 != 0:
      odd_only.append(i)
  return odd_only


print("Test 1 - Should return [1, 3, 5, 7, 9]:", SpOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Test 2 - Should return [1, 3, 5, 7, 9]:", SpOdd([1, 3, 5, 7, 9]))
print("Test 3 - Should return []:", SpOdd([2, 4, 6, 8, 10]))