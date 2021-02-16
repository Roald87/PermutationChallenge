"""
Count from 1 to 30, replacing any number divisible by three with the word "Fizz", and any number
divisible by five with the word "Buzz". If is divisible by three _and_ five replace the number by
FizzBuzz.
"""


def roald1():
    answer = ""
    for i in range(1, 31):
        if i % 3 == 0:
            answer += "Fizz"
        if i % 5 == 0:
            answer += "Buzz"

        if not (i % 3 == 0) and not (i % 5 == 0):
            answer += str(i)

        answer += " "

    return answer.strip()


def tom1():
    answer = ""
    for i in range(1, 31):
        if i % 15 == 0:
            update = "FizzBuzz"
        elif i % 3 == 0:
            update = "Fizz"
        elif i % 5 == 0:
            update = "Buzz"
        else:
            update = str(i)

        answer += " " + update

    return answer.strip()


def roald2():
    answer = " ".join(str(i) for i in range(1, 31))

    answer = answer.replace("30", "FizzBuzz")
    answer = answer.replace("27", "Fizz")
    answer = answer.replace("25", "Buzz")
    answer = answer.replace("24", "Fizz")
    answer = answer.replace("21", "Fizz")
    answer = answer.replace("20", "Buzz")
    answer = answer.replace("18", "Fizz")
    answer = answer.replace("15", "FizzBuzz")
    answer = answer.replace("12", "Fizz")
    answer = answer.replace("10", "Buzz")
    answer = answer.replace(" 9 ", " Fizz ")
    answer = answer.replace(" 6 ", " Fizz ")
    answer = answer.replace(" 5 ", " Buzz ")
    answer = answer.replace(" 3 ", " Fizz ")

    return answer

def tom2():
    def fizzbuzz(i):
        if i % 15 == 0:
            update = "FizzBuzz"
        elif i % 3 == 0:
            update = "Fizz"
        elif i % 5 == 0:
            update = "Buzz"
        else:
            update = str(i)
        return update
    str_list = [fizzbuzz(i) for i in range(1,31)]
    return " ".join(str_list)

def roald3():
    def digit_sum(number: int):
        return sum(int(digit) for digit in str(number))

    answer = ""
    for i in range(1, 31):
        div_by_three = digit_sum(i) in [3, 6, 9]
        if div_by_three:
            answer += "Fizz"

        div_by_five = "0" in str(i) or "5" in str(i)
        if div_by_five:
            answer += "Buzz"

        if not (div_by_three or div_by_five):
            answer += str(i)

        answer += " "

    return answer.strip()

def tom3():
    def is_prime(i: int):
        mod_sum = [i % j for j in range(1,i-1)] #prime nr will never get a zero except for 1
        zero_mod_sum = len([el for el in mod_sum if el == 0])
        if zero_mod_sum > 1:
            return False
        else:
            return True

    def is_even_not_mult_3_5(i: int):
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
            return True
        else:
            return False

    fizzbuzz_list = ['Fizz', 'Buzz', 'Fizz','Fizz', 'Buzz','Fizz','FizzBuzz']

    answer = ""
    fizzbuzz_ind = 0
    for i in range(1, 31):
        if (is_prime(i) and i not in [3,5]) or is_even_not_mult_3_5(i):
            update = str(i)
        else:
            update = fizzbuzz_list[fizzbuzz_ind]
            fizzbuzz_ind = (fizzbuzz_ind + 1) % len(fizzbuzz_list)
        answer += " " + update
    return answer.strip()