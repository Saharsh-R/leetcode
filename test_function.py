import pytest
from main import Solution

sol = Solution()


@pytest.mark.parametrize(
    "input1, input2, expected_output",
    [
        ("abcdefd", "d", "dcbaefd"),   
        ("abcdefd", "z", "abcdefd"), 
    ],
)
def test_addition(input1, input2, expected_output):
    assert sol.reversePrefix(input1, input2) == expected_output