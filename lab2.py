def min_board_size(N, W, H):
    def is_enough_space(size):
        return (size // W) * (size // H) >= N

    smallest_num, largest_num = 1, max(W, H) * N
    min_size = largest_num

    while smallest_num <= largest_num:
        mid = (smallest_num + largest_num) // 2
        if is_enough_space(mid):
            min_size = mid
            largest_num = mid - 1
        else:
            smallest_num = mid + 1

    return min_size
