def monotony(array):
    increases = 0
    decreases = 0
    if len(array) == 0:
        return True
    else:
        for i in range(len(array) - 1):
            if array[i + 1] >= array[i]:
                increases += 1
        for i in range(len(array) - 1):
            if array[i + 1] <= array[i]:
                decreases += 1
        if increases == len(array) - 1 or decreases == len(array) - 1:
            return True
        else:
            return False
