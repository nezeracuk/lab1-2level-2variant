def min_board_size(N, W, H):
    smallest_num, largest_num = 1, max(W, H) * N
    min_size = largest_num

    while smallest_num <= largest_num:
        mid = (smallest_num + largest_num) // 2
        if (mid // W) * (mid // H) >= N:
            min_size = mid
            largest_num = mid - 1
        else:
            smallest_num = mid + 1

    return min_size
