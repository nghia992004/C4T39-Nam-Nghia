yob = int(input("Nam sinh:"))
age = 2019 - yob
print(age)


if age<10:
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Adult")