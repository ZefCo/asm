def squares(numbers):
    for i in numbers:
        yield (i * i), i


def main():
    numbers = [1, 2, 3, 4, 5]

    square_numbers = squares(numbers)

    for square in square_numbers:
        print(square, type(square))


if __name__ in '__main__':
    main()