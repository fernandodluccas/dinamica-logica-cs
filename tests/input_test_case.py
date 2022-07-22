def problem1_format_input(path):
    with open(path) as file:
        lines = file.read().splitlines()
        test_cases = int(lines[0])
        test_array = []
        for index in range(1,test_cases+1):
            threshold = int(lines[2*index-1].split(' ')[1])
            student_array = [int(number) for number in lines[2*index].split(' ')]
            answer = lines[2*index-1].split(' ')[2]
            test_array.append((student_array, threshold, answer))

        return test_array


def problem2_format_input(path):
    with open(path) as file:
        lines = file.read().splitlines()
        test_cases = int(lines[0])
        test_array = []
        for index in range(1,test_cases+1):
            answer = int(lines[2*index-1])
            socks_array = [int(number) for number in lines[2*index].split(', ')]
            test_array.append((socks_array, answer))

        return test_array


def problem3_format_input(path):
    with open(path) as file:
        lines = file.read().splitlines()
        test_cases = int(lines[0])
        test_array = []
        for index in range(1,test_cases+1):
            year = int(lines[index].split(' ')[0])
            leap = bool(int(lines[index].split(' ')[1]))
            test_array.append((year, leap))

        return test_array