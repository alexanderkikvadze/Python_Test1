import datetime

if __name__ == '__main__':
    nnn = range(3, 7, 2)
    for n in nnn:
        print(n)

    for n in range(20, 31, 2):
        print(n)

    exit()

    x = 10
    print(x / 3)
    print(x // 3)
    print(x % 3)
    print(x ** 3)

    x += 3
    print(x)
#    i = int(input("i = "))
#    n = int(input("n = "))
    i = 1
    n = 5
    while i <= n:
        print(i * " " + "aaa")
        i += + 2

    names = ['aaa', 'sss', 'ddd']
    i = 0
    n = len(names)
    print(" ----  printed by while")
    while i <= n:
        if i == 2:
            names.append("fff")
        print(names[i:i + 2])
        i += 1
    print(" ----  printed by for")
    for item in names:
        print(item)
    str1 = "qwert"
    print(str1)
    str1 = str1[:2] + "7" + str1[3:]
    print(str1)

#first_name = input("please insert the first name - ")
#last_name = input("please insert the last name - ")
#birth_year = int(input("Please enter the your birth year - "))
#is_patient_new = bool(input("Are you new patient? - "))
#if __name__ == '__main__':
#    current_year = date.today()
#age = current_year.year - birth_year

#print(first_name + " " + last_name + " age = " + str(age) + " is new patient = " + str(is_patient_new))