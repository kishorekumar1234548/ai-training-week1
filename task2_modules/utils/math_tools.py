def add(a, b):
    return a + b

def average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("Addition:", add(10, 20))

    marks = [80, 90, 70, 60, 100,]

    print("Average:", average(marks))
    