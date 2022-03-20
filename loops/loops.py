# returns the number of lowercase words in a list of strings
def count_lowercase_words(words):
    count = 0
    for word in words:
        if(word.islower()):
            count += 1
    return count

# returns the number of uppercase words in a list of strings
def count_uppercase_words(words):
    raise NotImplementedError("No implementation provided for count_uppercase_words")

# makes every person in a list of names a doctor
# e.g.
#   make_them_doctors(["Watson", "Einstein"]) = ["Dr. Watson", "Dr. Einstein"]
def make_them_doctors(names):
    raise NotImplementedError("No implementation provided for make_them_doctors")

# returns true if the list is sorted from smallest to largest, false otherwise
def is_sorted_list(list):
    raise NotImplementedError("No implementation provided for is_sorted_list")

# returns the number of times that 'item' occurs in 'list'
def count_occurrences(item, list):
    raise NotImplementedError("No implementation provided for count_occurences")

def reverse_list(list):
    raise NotImplementedError("No implementation provided for reverse_list")

# form pairs from two lists 
# e.g.
#   zip_two_lists([1,2,3], [4,5]) = [(1,4), (2,5)]
#   zip_two_lists(["abc", "def"], ["ghi", "jkl"]) = [("abc", "ghi"), ("def", "jkl")]
def zip_two_lists(list_one, list_two):
    raise NotImplementedError("No implementation provided for zip_two_lists")

# returns true if 'item' is in 'list'
def search(item, list):
    raise NotImplementedError("No implementation provided for search")

# returns the biggest number in a list of numbers. If the list is empty, returns None
def find_biggest_number(numbers):
    raise NotImplementedError("No implementation provided for find_biggest_number")

# computes the factorial of a number. Assume n >= 0.
# e.g. factorial_recursive(5) = 5 * 4 * 3 * 2 * 1 = 120
def factorial_recursive(n):
    if(n == 0):
        return 1
    else:
        return n * factorial_recursive(n-1)

# as above, but with a loop
def factorial_loop(n):
    raise NotImplementedError("No implementation provided for factorial_loop")

# e.g. interleave_lists([1,2,3,4], ["abc", "def"]) = [1, "abc", 2, "def", 3, 4]
def interleave_lists(list_one, list_two):
    raise NotImplementedError("No implementation provided for interleave_lists")

# returns true if there are two numbers in list that sum to n
def two_numbers_in_list_that_sum_to(n, list):
    raise NotImplementedError("No implementation provided for two_numbers_in_list_that_sum_to")