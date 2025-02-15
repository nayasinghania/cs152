# Question 1 - Phone Number Regex
# See test print statements

import re

def isPhoneNumber(number):
  if re.search(r'\d{3}-\d{3}-\d{4}', number) != None:
    return True
  else:
    return False

print("Test 1 - Should return True:", isPhoneNumber('123-456-7890'))
print("Test 2; Should return False:", isPhoneNumber('123/456/7890'))