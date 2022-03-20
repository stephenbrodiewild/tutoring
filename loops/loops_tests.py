from loops import *

"""
Usage:
    python loops_tests.py 

This file is for testing the 'loops.py' file.

There are lots of ways to test code. This style is called 'unit-testing',
where you test the smallest 'units' (usually functions) of your program
separately, so that when you combine these small 'units' into a larger
program, you have some confidence that it will work properly.

You can read more about it here: https://en.wikipedia.org/wiki/Unit_testing

What does 'assert' do? Try running:

        assert(5 == 5)
        assert(5 * 2 == 10)
        assert(len("abc") == 3)
        assert("abc"[0] == "b")

Gemerally it's considered good programming to write your tests before you write your code.
More info here: https://en.wikipedia.org/wiki/Test-driven_development


"""

def test_count_lowercase_words():
    test_words = ["THIS", "list", "HAS", "FOUR", "uppercase", "words", "AND", "seven", "lowercase", "words"]
    assert(count_lowercase_words(test_words) == 6)

def test_count_uppercase_words():
    test_words = ["THIS", "has", "THREE", "uppercase", "WORDS"]
    assert(count_uppercase_words(test_words) == 3)

def test_make_them_doctors():
    names = ["Dre", "Seuss", "Phil"]
    doctorised = make_them_doctors(names)
    assert(doctorised[0] == "Dr. Dre")
    assert(doctorised[1] == "Dr. Seuss")
    assert(doctorised[1] == "Dr. Phil") 

def test_is_sorted_list():
    sorted_list = [1,1,2,6,24,120]
    unsorted_list = [1,2,1,6,3,6]
    assert(is_sorted_list(sorted_list))
    assert(is_sorted_list(unsorted_list) == False)

def test_count_occurences():
    raise NotImplementedError()

def test_reverse_list():
    raise NotImplementedError()

def test_zip_two_lists():
    raise NotImplementedError()

def test_search():
    raise NotImplementedError()

def test_find_biggest_number():
    raise NotImplementedError()

def test_factorial_recursive():
    raise NotImplementedError("No implementation provided for test_factorial_recursive")

def test_factorial_loop():
    assert(factorial_loop(0) == 1)
    assert(factorial_loop(1) == 1)
    assert(factorial_loop(2) == 2)
    assert(factorial_loop(3) == 6)
    assert(factorial_loop(4) == 24)
    assert(factorial_loop(5) == 120)

def test_factorial_loop_equivalent_to_factorial_recursive():
    for x in range(10):
        assert(factorial_loop(x) == factorial_recursive(x))

def test_interleave_lists():
    raise NotImplementedError("No implementation provided for test_interleave_lists")

def test_two_numbers_in_list_that_sum_to():
    raise NotImplementedError("No implementation provided for test_two_numbers_in_list_that_sum_to")

# Don't worry about understanding this
def test_all(tests):
    def print_green_text(s):
        print(f"\033[1;32;40m{s}\033[0;37;40m")
    def print_red_text(s):
        print(f"\033[1;31;40m{s}\033[0;37;40m")
    def print_blue_text(s):
        print(f"\033[1;34;40m{s}\033[0;37;40m")

    num_tests = len(tests)
    num_succeeded = 0
    num_failed = 0
    num_unimplemented = 0
    for test in tests:
        print_blue_text(f"Testing {test.__name__} ...")
        try:
            test()
            print_green_text("\tTest passed!")
            num_succeeded += 1
        except AssertionError:
            print_red_text("\tTest failed due to failed assertion!")
            num_failed += 1
        except NotImplementedError:
            print_red_text("\tTest failed due to unimplemented test/code!")
            num_unimplemented += 1

    print("-"*64)
    print_blue_text(f"Total number of tests: {num_tests}")
    print_green_text(f"Total number of succeeded tests: {num_succeeded}")
    print_green_text(f"Success rate: {num_succeeded / num_tests * 100}%")
    print_green_text(f"Implementation rate: {(num_succeeded + num_failed)/num_tests * 100}%")
    print_red_text(f"Total number of failed tests: {num_failed}")
    print_red_text(f"Total number of missing implementations: {num_unimplemented}")
    print_red_text(f"Failure rate: {num_failed / num_tests * 100}%")

if __name__ == "__main__":

    # put the name of the test in here:
    tests = [
        test_count_lowercase_words,
        test_count_uppercase_words,
        test_make_them_doctors,
        test_is_sorted_list,
        test_count_occurences,
        test_reverse_list,
        test_zip_two_lists,
        test_search,
        test_find_biggest_number,
        test_factorial_recursive,
        test_factorial_loop,
        test_factorial_loop_equivalent_to_factorial_recursive,
        test_interleave_lists,
        test_two_numbers_in_list_that_sum_to
    ]

    # magic to run your tests
    test_all(tests)