
# range of [0, 10)
for x in range(10):
    print(x)

# range of [5, 10) 
for y in range(5, 10):
    print(y)

# stepped range
for z in range(0,10,2):
    print(z)

# simply iterating over a list
list_of_words = ["this", "is", "a", "list", "of", "words"]
for word in list_of_words:
    print(list_of_words)

# enumerating
names = ["Alonzo", "Alan", "Stephen", "John"]
for n, name in enumerate(names):
    print(f"{n} {name}")

# 'switching' on elements in a list/range
for n in range(100):
    if(n % 15 == 0):
        print("FizzBuzz")
    elif(n % 5 == 0):
        print("Buzz")
    elif(n % 3 == 0):
        print("Fizz")
    else:
        print(n)

# accumulating elements in a list/range
sum = 0
for number in range(100):
    sum += number
print(sum)

# nested loops
for x in range(0,10):
    for y in range(0, x):
        print("*",end='')
    print("")

# looping to get some input from the user
def login():
    login_details = [("leetc00der", "password123"), ("hackermann","opEn_sEsamE")]
    username = input("Username: ")
    password = input("Password: ")
    while((username, password) not in login_details):
        username = input("Enter username: ")
        password = input("Enter password: ")
    print("You're in")
login()

# collecting elements that satisfy a predicate
def collect_uppercase_words(sentence):
    uppercase_words = []
    words = sentence.split(' ')

    for word in words:
        if(word.isupper()):
            uppercase_words.append(word)

    return uppercase_words
print(collect_uppercase_words("THIS SENTENCE has some UPPER and LOWERCASE words"))

# checking if an element in one list is in another list
list_of_trading_partners = ["China", "Japan", "USA", "Russia", "New Zealand", "Myanmar", "South Africa"]
list_of_sanctioned_countries = ["Russia", "DPRK", "Iran", "Myanmar"]
for trading_partner in list_of_trading_partners:
    if(trading_partner in list_of_sanctioned_countries):
        print(f"Uh oh looks like we've got to cut ties with {trading_partner}")

