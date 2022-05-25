import numpy as np

"""
def test_random_numpy():
    mean = 5
    sdev = 3
    sample_size = 1000000

    sample = np.random.normal(mean, sdev, sample_size)

    np.testing.assert_almost_equal(mean, np.mean(sample), decimal=2)
    np.testing.assert_almost_equal(sdev, np.std(sample), decimal=2)



def sum_of_squares(sequence):
    # Your code here
    sum = 0

    for number in sequence:
        sum = sum + number**2
    
    return sum

print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))
"""

def sum_of_squares(sequence):
    # Your code here
    sum = 0

    for number in sequence:
        sum = sum + float(number)**2
    
    return sum

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))