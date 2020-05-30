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





