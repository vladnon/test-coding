def countTriples( n: int) -> int:
    left, right = 0, n - 1
    count = 0
    while left <= right:
        cur_sum_squares = (left ** 2 + right ** 2) 
        if cur_sum_squares > n * n: 
            left += 1
        elif cur_sum_squares == n * n:
            count += 1
        else:
            right += 1
    return count


if __name__ == "__main__":
    
    graph = {
        1 : {2 : 5, 3 : 1},
        2 : {4 : 2, 3 : 3}, 
        3 : {2 : 3, 4 : 6},
        4 : {2: 2, 3: 6}
    }

    # print(algorithm(graph, 1, 4))
    print(countTriples(5))