def insert(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        # If new interval ends before current interval starts, insert and return
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        # If new interval starts after current interval ends, keep current
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        # Overlapping intervals, merge them
        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
    res.append(newInterval)
    return res
