"""Grade Calculator - calculates the average of scores and a letter grade."""


def calculate_average(scores):
    return sum(scores) / len(scores)


def letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main():
    raw = input("Enter scores separated by spaces: ").split()
    scores = [float(s) for s in raw]
    average = calculate_average(scores)
    print(f"Average: {average:.2f}  Grade: {letter_grade(average)}")


if __name__ == "__main__":
    main()
