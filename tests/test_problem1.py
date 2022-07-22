from problems.problem1 import solve
from input_test_case import problem1_format_input

def test_case_one():
    assert solve([-1, -3, 4, 2], 3) == 'NÃO'
    assert solve([0, -1, 2, 1], 2) == 'SIM'


def test_case_two():
    assert solve([-93, -86, 49, -62, -90, -63, 40, 72, 11, 67], 4) == "SIM"
    assert solve([23, -35, -2, 58, -67, -56, -42, -73, -19, 37], 10) == "NÃO"
    assert solve([13, 91, 56, -62, 96, -5, -84, -36, -46, -13], 9) == "NÃO"
    assert solve([19, 29, -17, -71, -75, -27, -56, -53, 65, 83], 2) == "SIM"
    assert solve([-58, -29, -35, -18, 43, -28, -76, 43, -13, 6], 3) == "SIM"
    assert solve([88, -17, -96, 43, 83, 99, 25, 90, -39, 86], 1) == "SIM"

def test_case_three():
    test_array = problem1_format_input("tests/input1.txt")
    for test_case in test_array:
        assert solve(test_case[0], int(test_case[1])) == test_case[2]

