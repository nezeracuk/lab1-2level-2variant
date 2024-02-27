def monotony(array):
    tedium = array[1] >= array[0]
    for i in range(2, len(array)):
        if (array[i] >= array[i - 1]) != tedium:
            return False
    return True



