def sum_of_intervals(intervals):
    counted = []
    for interval in intervals:
        for num in range(interval[0], interval[1]):
            if num not in counted:
                counted.append(num)
    return len(counted)