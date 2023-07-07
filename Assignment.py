#1. Write a Python program to reverse a string without using any built-in string reversal functions.
def reverse(str):   
    str = str[::-1]   
    return str   
    
st = "Animesh"  
print ("The original string  is : ",st)   
print ("The reversed string  is : ",reverse(st))


# 2. Implement a function to check if a given string is a palindrome.
def isPalindrome(s):
    return s == s[::-1]
 
s = "naman"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# 3.Write a program to find the largest element in a given list.
list1 = [10,1,34,25,22]
 
list1.sort()
 
print("Largest element is:", list1[-1])

#4. Implement a function to count the occurrence of each element in a list
def countX(lst, x):
    return lst.count(x)

lst = [8, 6, 8, 10, 9, 20, 10, 9, 9]
x = 9
print( x," occurred " ,countX(lst, x)," times")


#5. Write a Python program to find the second largest number in a list.
def secondmax(arr):
  sublist = [x for x in arr if x < max(arr)]
  return max(sublist)
 
if __name__ == '__main__':
  arr = [10,20,4,40,32]
  print(secondmax(arr))


#6. Implement a function to remove duplicate elements from a list.
def RemoveDuplicate(duplicate):
    set_list = []
    for num in duplicate:
        if num not in set_list:
            set_list.append(num)
    return set_list

duplicatedArray = [2, 4, 10, 5, 2, 20, 4]
print(RemoveDuplicate(duplicatedArray))

# 7. Write a program to calculate the factorial of a given number.
def factorial(n):
       
    if n == 0:
        return 1
      
    return n * factorial(n-1)

num = 8;
print("Factorial of", num, "is",
factorial(num))


# 8. Implement a function to check if a given number is prime
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
print(isprime(7))
print(isprime(8))


# 9. Write a Python program to sort a list of integers in ascending order.
nums = [1, 5, 3, 4, 2, 10, 9]
nums.sort()
print('List in Ascending Order: ', nums)

# 10. Implement a function to find the sum of all numbers in a list.
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum([1,2,3,4,5,6,7,8]))



#11. Write a program to find the common elements between two lists.

def common_element(a, b):   
    a_set = set(a)
    b_set = set(b)

    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set)) 
    else:
        return("no common elements")
    
#12. Implement a function to check if a given string is an anagram of another string.

def isAnagram(self, a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

#  13. Write a Python program to generate all permutations of a given string.
def permute(s, answer):
    if (len(s) == 0):
        print(answer, end = "  ")
        return
     
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)
 
answer = ""
s = input("Enter the string : ")
print("All possible strings are : ")
permute(s, answer)

#14. Implement a function to calculate the Fibonacci sequence up to a given number of terms.
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("please enter correct number")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b
print(fibonacci(5))


# 15. Write a program to find the median of a list of numbers.
def findMedian(a, n):
 
   
    sorted(a)
 
    
    if n % 2 != 0:
        return float(a[int(n/2)])
 
    return float((a[int((n-1)/2)] +
                  a[int(n/2)])/2.0)

def findMean(a, n):
 
    sum = 0
    for i in range(0, n):
        sum += a[i]
 
    return float(sum/n)

# 16. Implement a function to check if a given list is sorted in non-decreasing order.
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


list1 = [1, 2, 3, 4, 5]
print(is_sorted(list1)) 

list2 = [5, 3, 2, 1]
print(is_sorted(list2)) 

list3 = [1, 1, 2, 3, 3, 4]
print(is_sorted(list3)) 



# 17. Write a Python program to find the intersection of two lists.
def find_intersection(list1, list2):
    intersection = []
    for element in list1:
        if element in list2 and element not in intersection:
            intersection.append(element)
    return intersection
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_intersection(list1, list2)
print("Intersection:", result)


#18. Implement a function to find the maximum subarray sum in a given list.
def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

list1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(list1)
print("Maximum Subarray Sum:", result)

#19. Write a program to remove all vowels from a given string.
def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string
input_string = input("Enter a string: ")
result = remove_vowels(input_string)
print("String without vowels:", result)

#20. Implement a function to reverse the order of words in a given sentence.

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence
input_sentence = input("Enter a sentence: ")
reversed_sentence = reverse_words(input_sentence)
print("Reversed sentence:", reversed_sentence)


#21. Write a Python program to check if two strings are anagrams of each other.
def isAnagram(self, a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False
    
#22. Implement a function to find the first non-repeating character in a string.
def find_first_non_repeating_char(string):
    char_count = {}
    
    
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    
    for char in string:
        if char_count[char] == 1:
            return char
    
    
    return None

input_string = input("Enter a string: ")
result = find_first_non_repeating_char(input_string)
if result is None:
    print("No non-repeating character found")
else:
    print("First non-repeating character:", result)


#23. Write a program to find the prime factors of a given number.
def find_prime_factors(number):
    prime_factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return prime_factors
input_number = int(input("Enter a number: "))
result = find_prime_factors(input_number)
print("Prime factors:", result)


# 24. Implement a function to check if a given number is a power of two.
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
 
    return True
 

# 25. Write a Python program to merge two sorted lists into a single sorted list.

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1


    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

list1 = [1, 4, 7, 9]
list2 = [2, 3, 5, 6, 8]
result = merge_sorted_lists(list1, list2)
print("Merged and sorted list:", result)

# 26. Implement a function to find the mode of a list of numbers.

def find_mode(numbers):
    
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    
    max_count = max(counts.values())
    
    
    mode = [num for num, count in counts.items() if count == max_count]
    
    return mode


#27. Write a program to find the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


num1 = 48
num2 = 18
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)



#28. Implement a function to calculate the square root of a given number.

import math

def square_root(number):
    if number < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    
    result = math.sqrt(number)
    return result



#29. Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.
def isPalindrome(s):
    return s == s[::-1]


#30. Implement a function to find the minimum element in a rotated sorted list.
def find_min(rotated_list):
    left = 0
    right = len(rotated_list) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if rotated_list[mid] > rotated_list[right]:
            left = mid + 1
        else:
            right = mid
    
    return rotated_list[left]

numbers = [4, 5, 6, 7, 0, 1, 2]
result = find_min(numbers)
print("The minimum element in the rotated sorted list is:", result)



# 31. Write a program to find the sum of all even numbers in a list.

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(number_list)
print("The sum of all even numbers in the list is:", result)


#32. Implement a function to calculate the power of a number using recursion.
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / power(base, -exponent)

base = 2
exponent = 5
result = power(base, exponent)
print(base, "raised to the power of", exponent, "is:", result)



# 33. Write a Python program to remove duplicates from a list while preserving the order.

def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

my_list = [1, 3, 2, 4, 2, 3, 1, 5, 4]
result = remove_duplicates_preserve_order(my_list)
print("List after removing duplicates:", result)


#34. Implement a function to find the longest common prefix among a list of strings.

def longest_common_prefix(strs):
    if not strs:
        return ""

   
    sorted_strs = sorted(strs)

    
    for i in range(len(sorted_strs[0])):
        if sorted_strs[0][i] != sorted_strs[-1][i]:
            return sorted_strs[0][:i]

   
    return sorted_strs[0]


string_list = ["flower", "flow", "flight"]
result = longest_common_prefix(string_list)
print("The longest common prefix is:", result)


#35. Write a program to check if a given number is a perfect square.
def is_perfect_square(number):
    if number < 0:
        return False
    sqrt = int(number ** 0.5)

    return sqrt * sqrt == number

num = 25
result = is_perfect_square(num)
if result:
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")


#36. Implement a function to calculate the product of all elements in a list.

def calculate_product(numbers):
    if not numbers:
        return 1

    product = 1
    for num in numbers:
        product *= num
    return product

number_list = [1, 2, 3, 4, 5]
result = calculate_product(number_list)
print("The product of all elements in the list is:", result)


#37. Write a Python program to reverse the order of words in a sentence while preserving the word order.

def reverse_words(sentence):
 
    words = sentence.split()

    reversed_words = words[::-1]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

input_sentence = "Hello, how are you?"
result = reverse_words(input_sentence)
print("Reversed sentence:", result)



#38. Implement a function to find the missing number in a given list of consecutive numbers.


def find_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number
number_list = [1, 2, 3, 5, 6, 7, 8]
result = find_missing_number(number_list)
print("The missing number is:", result)



#39. Write a program to find the sum of digits of a given number.
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

# Example usage
num = 12345
result = sum_of_digits(num)
print("The sum of digits of the number is:", result)


#40. Implement a function to check if a given string is a valid palindrome considering case sensitivity.

def is_palindrome(string):
    
    clean_string = ''.join(c for c in string if c.isalnum())
    return clean_string == clean_string[::-1]
input_string = "Able was I saw eLba"
result = is_palindrome(input_string)
if result:
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")


#41. Write a Python program to find the smallest missing positive integer in a list.

def find_smallest_missing_positive(nums):
    n = len(nums)

   
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1

number_list = [3, 4, -1, 1]
result = find_smallest_missing_positive(number_list)
print("The smallest missing positive integer is:", result)



#42. Implement a function to find the longest palindrome substring in a given string.
def longest_palindrome(string):
    longest = ''
    for i in range(len(string)):
        
        odd_palindrome = expand_around_center(string, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        
        even_palindrome = expand_around_center(string, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest


def expand_around_center(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left + 1: right]

input_string = "babad"
result = longest_palindrome(input_string)
print("Longest palindrome substring:", result)


# 43. Write a program to find the number of occurrences of a given element in a list.

def countX(lst, x):
    return lst.count(x)

lst = [8, 6, 8, 10, 9, 20, 10, 9, 9]
x = 9
print( x," occurred " ,countX(lst, x)," times")


# 44. Implement a function to check if a given number is a perfect number.
def is_perfect_number(number):
    if number <= 0:
        return False
    
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    
    return divisor_sum == number
num = 28
result = is_perfect_number(num)
if result:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")


#45. Write a Python program to remove all duplicates from a string.
def remove_duplicates(string):

    unique_chars = set(string)

    result = ''.join(unique_chars)

    return result


input_string = "Hello, World!"
result = remove_duplicates(input_string)
print("String after removing duplicates:", result)


#46. Implement a function to find the first missing positive
def find_first_missing_positive(nums):
    
    nums = [num for num in nums if num > 0]

   
    num_set = set(nums)

    
    i = 1
    while i in num_set:
        i += 1

    return i


number_list = [3, 4, -1, 1]
result = find_first_missing_positive(number_list)
print("The first missing positive integer is:", result)
