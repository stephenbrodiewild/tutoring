# A whole bunch of loopy exercises.

A bunch of theory stuff (skip if bored and come back before exams):

- when you write a program, you'll want some code to be executed multiple times
- different ways of doing **iteration** or **repetition**:

    1. jumps (and GOTO) in assembly languages (and C)
        - all iteration, at the end of the day, is just doing this (i.e. when your code is compiled/interpreted)
        - e.g. 'JUMP 10' to start executing code at line 10
        - e.g. 'GOTO end' which executes code at a section of your code labelled 'end'
        - this tends to make code harder to read/debug, so new 'control structures' like while/for loops were created
            and these almost always make code easier to read/write/debug
        
    2. while loops
        - used for potentially **unbounded repetition**
        - e.g.
            ```
            # keep asking for number until user enters 10
            while(int(input("Guess a number: ")) != 10):
                print("Wrong number!")
            ```
    3. for loops
        - used for **bounded repetition**, or iterating over a **collection**
        - e.g.
            ```
            # prints each fruit on a new line
            for fruit in ["apple", "banana", "mango"]:
                print(fruit)
            ```
    4. recursion
        - used when a **problem is naturally divided into similar and smaller sub-problems**, and those are
            naturally divided into similar and smaller sub-problems, and so on and so forth until you hit
            a 'base' case
        - e.g.
            ```
            # calculate the greatest common divisor of two numbers
            def gcd(x,y):
                if(y == 0):
                    return x
                else:
                    return gcd(y, x % y)
            ```
- in python, you'll generally be writing for-loops, sometimes while loops, and very ocassionally recursive functions
    - recursive functions aren't always efficient in Python because it lacks 'tail-call optimisation'
    - pretty easy to get 'stack-overflow errors'
    - e.g. 
            ```
            def crash_python():
                print("I'm going to crash lol")
                crash_python()
            ```
- while-loops and recursive functions are equivalent (apart from efficiency considerations, and the whole tail-call thing)
    - e.g.

        ```
        def guessing_game(n):
            while(int(input("Guess a number: ")) != n):
                    print("Wrong number!")
        ```
        can be rewritten to 
        ```
        def guessing_game(n):
            if(int(input("Guess a number: ")) != n):
                print("Wrong number!)
                guessing_game(n)
        ```
- every for-loop can be rewritten to be recursive or use a while-loop, but not vice-versa
    - e.g.

        ```
        x = 0
        while(x >= 0):
            print(f"Looped {x} times...")
            x += 1
        ```
        can't be rewritten into a for-loop. If you could, it'd look something like:
        ```
        for x in infinite_list:
            print(f"Looped {x} times...") 
        ```
        But infinite lists in Python don't exist. [^1]

- it takes a bit of practise to know when while loops, for loops, recursion, or GOTO is better
- rules of thumb:
    - while loops are for when you don't know how many times the code should run, but you know when it should stop
    - for loops are useful when you know how many times the code should be run
    - recursion comes in handy if operating on a recursive data-structure
    - GOTO is bad; avoid GOTO. [^2]


[^1]: Except they do, kind of, with generators.
[^2]: If you disagree because XYZ then you know too much programming for this tutorial to help you :) 