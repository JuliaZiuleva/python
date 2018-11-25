'''#words = ['hello', 'daddy', 'hello', 'mum']
#print(tuple(words)) ('hello', 'daddy', 'hello', 'mum')
#print(list(words)) ('hello', 'daddy', 'hello', 'mum')
#print(set(words)) ('hello', 'daddy', 'hello', 'mum')

def safe_pawns(pawns: set) -> int:
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
    print(pawns_indexes)
    count = 0
    for row, col in pawns_indexes:
        is_safe = ((row - 1),(col + 1)) in pawns_indexes or ((row - 1),(col - 1)) in pawns_indexes
        if is_safe:
            count += 1
    return count
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    
    
    
    def sun_angle(time):
    time_list = get_time_list()
    angels_list = get_angels_list()
    if time in time_list[360:1081]:
        return angels_list[time_list[360:1081].index(time)]
    else:
        return "I don't see the sun!"

def get_angels_list():
    def frange(start, stop, step):
        i = 0
        while start + i * step < stop:
            yield start + i * step
            i += 1
    return [x for x in frange(0,180.25 ,0.25)]


def get_time_list():
    hours, minutes, time_list = [], [], []
    for i in range(24):
        if i <= 9:
            hours.append("0%d:" % (i))
        else:
            hours.append("%d:" % (i))
    for j in range(60):
        if j <=9:
           minutes.append("0%d" % (j))
        else:
          minutes.append("%d" % (j))
    for a in hours:
        for b in range(len(minutes)):
            time_list.append(a + minutes[b])
    return time_list
    
    
    
    from itertools import groupby

def long_repeat(line):
    my_list = list(line)
    answer = [] 
    if len(line) > 0:   
        for key, iter in groupby(my_list): 
            answer.append((len(list(iter))))
        print(max(answer))
    else:
        return 0

if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    #assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    #assert long_repeat('abababaab') == 2, "Third"
    #assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
    
    
def checkio(text: str) -> str:
  count = 1
from collections import Counter

def checkio(text):
    new_text = ''
    new_text = [(i + new_text) for i in text.lower() if i.isalpha() == True]
    new_text = sorted(new_text)
    print(max((Counter(new_text)), key=(Counter(new_text)).get))
if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")



import re
import string

def checkio(data: str) -> bool:
    if len(data) >= 10: 
        if any(i.isdigit() for i in data) == True:
            if re.match("^[A-Za-z0-9]*$", data):
                if (i.isupper() for i in data) == True:
                    if (i.islower() for i in data)== True:
                        return True
    else:
        return False
    #replace this for solution
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print(censor("this hack is wack hack", "hack"))

import time
time.sleep(5)
(print("Hello World!"))

a = "Word"
b = 3.7
print("Hello " + a + "!Version Python'a = " + str(b)+ "!")

a = "Word"
b = 3
c = 7
print("Hello %s! Version Python's = %d.%d" % ("World!", b, c))

print("Hello {name}! Version Python's = {version}".format(name = "World", version = 3.7))

print("Hello {0}! Version Python's = {1}".format("World", 3.7))

print("{0} {1} {0}".format('hello', 'world'))

fruits = ['Lemons', 'bananas', 'oranges', 'apples']
print(",".join(fruits) + '.')

print("Hello World!".replace("World", "766"))

a = 'Hello'
b = ' World!'
print((a + b).replace(a,b))
---------------
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests


def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
    return average(results)
    
get_class_average([lloyd, alice, tyler])
'''