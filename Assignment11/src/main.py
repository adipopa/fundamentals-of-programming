# 3) The sequence a = 𝑎1, …, 𝑎𝑛 with integer elements is given. Determine all strictly increasing
# subsequences of sequence a (conserve the order of elements in the original sequence).


def solution(sequence, result, position):
    if position == 0:
        return True
    return sequence[result[position - 1]] < sequence[result[position]]


def print_sequence(sequence, result, position):
    sequence_to_print = []
    for index in range(0, position + 1):
        sequence_to_print.append(sequence[result[index]])
    print(sequence_to_print)


def backtracking_iterative(sequence, result):
    position = 0
    if len(sequence_of_integers) == 1:
        print_sequence(sequence, result, position)
        return
    while position >= 0:
        result[position] += 1
        if result[position] < len(sequence):
            if solution(sequence, result, position):
                print_sequence(sequence, result, position)
                position += 1
                result[position] = result[position-1]
        else:
            position -= 1


def backtracking_recursive(sequence, result, position):
    for next_value in range(result[position - 1] + 1, len(sequence)):
        result[position] = next_value
        if solution(sequence, result, position):
            print_sequence(sequence, result, position)
            backtracking_recursive(sequence, result, position + 1)


try:
    sequence_of_integers = list(input("The sequence of integers: ").strip().split())
    if len(sequence_of_integers) == 0:
        raise ValueError()
    result = [-1] * len(sequence_of_integers)
    while True:
        user_input = input("Choose which backtracking strategy to use (iterative / recursive): ").strip().lower()
        if user_input == "iterative":
            print("The strictly increasing subsequences of the sequence " + str(sequence_of_integers) + ":")
            backtracking_iterative(sequence_of_integers, result)
            break
        elif user_input == "recursive":
            print("The strictly increasing subsequences of the sequence " + str(sequence_of_integers) + ":")
            backtracking_recursive(sequence_of_integers, result, 0)
            break
        else:
            print("Not a valid option.")
            continue
except ValueError:
    print("Invalid sequence of integers.")
