#!/usr/bin/python3
def weight_average(my_list=[]):
    totalScore = 0
    totalWeight = 0
    if not my_list:
        return (0)
    for a in my_list:
        totalScore += (a[0] * a[1])
        totalWeight += a[1]

    Average = totalScore / totalWeight
    return (Average)
