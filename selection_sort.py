numbers = [10, 15, 3, 6, 7, 1, 3, 9, 10]

def max(numbers):
    max = numbers[0]
    for number in numbers:
        if max < number:
            max = number
    return max

def move(numbers, idx):
    return [numbers[idx]] + numbers[:idx] + numbers[idx + 1:]

def reverse_sort(numbers):
    for i in range(len(numbers)):
        sorted_numbers = numbers[:i]
        unsorted_numbers = numbers[i:]
        max_number = max(unsorted_numbers)
        numbers = sorted_numbers + move(unsorted_numbers, unsorted_numbers.index(max_number))
    return numbers

assert reverse_sort([10, 15, 3, 6, 7, 1, 3, 9, 10]) == [15, 10, 10, 9, 7, 6, 3, 3, 1]
assert reverse_sort([10, 15, 3, 6, 7, 3, 9, 10]) == [15, 10, 10, 9, 7, 6, 3, 3]
assert reverse_sort([10, 15, 6, 7, 3, 9, 10]) == [15, 10, 10, 9, 7, 6, 3]
assert reverse_sort([10, 15, 9, 10]) == [15, 10, 10, 9]
assert reverse_sort([10]) == [10]

assert reverse_sort([10, 15, 6, 7, 3, 10]) == [15, 10, 10, 7, 6, 3]
assert reverse_sort([10, 15, 7, 9, 10]) == [15, 10, 10, 9, 7]
assert reverse_sort([10, 15, 9]) == [15, 10, 9]


print(reverse_sort(numbers))