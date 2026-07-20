def pair_product(numbers, target_product):
    mapped_numbers = {}

    for index, value in enumerate(numbers):
        print(f"index: {index}")
        print(mapped_numbers)
        complement = target_product / value

        if complement in mapped_numbers:
            return (mapped_numbers[complement], index)

        mapped_numbers[complement] = index


print(pair_product([3, 2, 5, 4, 1], 8))
