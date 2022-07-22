from problems.problem3 import solve
from tests.input_test_case import problem3_format_input

def test_case_one():
    assert solve(2017) == '13.09.2017'
    assert solve(2005) == '13.09.2005'
    assert solve(2001) == '13.09.2001'
    assert solve(2022) == '13.09.2022'
    assert solve(1758) == '13.09.1758'
    assert solve(2600) == '13.09.2600'

def test_case_two():
    assert solve(1920) == '12.09.1920'
    assert solve(2020) == '12.09.2020'
    assert solve(2024) == '12.09.2024'
    assert solve(2400) == '12.09.2400'
    assert solve(1520) == '12.09.1520'
    assert solve(2804) == '12.09.2804'

def test_case_three():
    test_array = problem3_format_input("tests/input3.txt")
    for test_case in test_array:
        if test_case[1]:
            assert solve(test_case[0]) == '12.09.'+str(test_case[0])
        else:
            assert solve(test_case[0]) == '13.09.'+str(test_case[0])
