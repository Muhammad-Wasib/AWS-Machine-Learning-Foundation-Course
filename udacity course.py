import numpy as np
import math

# first example of clean code
test_score = [88, 92, 79, 93, 85]
print(np.mean(test_score))
curved_test_score = [math.sqrt(score) * 10 for score in test_score]
print(np.mean(curved_test_score))

# second
age_list = [47, 12, 28, 52, 35]
for i, age in enumerate(age_list):
    if age < 18:
        is_minor = True
        age_list[i] = 'minor'
print(age_list)


# Third
def flat_curve(arr, n):
    return (i + n for i in arr)


def square_root_curve(arr):
    return (math.sqrt(i) * 10 for i in arr)


test_score = [88, 92, 79, 93, 85]
curved_5 = flat_curve(test_score, 5)
curved_10 = flat_curve(test_score, 10)
curved_sqrt = square_root_curve(test_score)

for score_list in test_score, curved_5, curved_10, curved_sqrt:
    print(np.mean(score_list))
