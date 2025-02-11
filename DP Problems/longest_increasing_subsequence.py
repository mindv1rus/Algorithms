def LongestIncreasingSubsequence(list):
    memo = [-1] * len(list)
    print("memo before algorithm = ", memo)
    path_memo = [-1] * len(list)
    for i in range(len(list)):
        path_memo[i] = [list[i]]
    print("path memo after initialization = ", path_memo)
    LongestIncreasingSubsequenceOfi(list, memo, path_memo, 0)

    print("memo after algorithm = ", memo)
    print("path memo after algorithm = ", path_memo)
    return max(memo)



def LongestIncreasingSubsequenceOfi(list, memo, path_memo, i):
    if i == (len(list) - 1):
        memo[i] = 1
        return 1
    
    current_max = 1
    index_of_max = -1

    for j in range((i + 1), len(list)):
        current_sum = 1
        if memo[j] == -1:
            LongestIncreasingSubsequenceOfi(list, memo, path_memo, j)
        if list[i] < list[j]:
            current_sum += memo[j]
            
        if current_sum > current_max:
            current_max = current_sum
            index_of_max = j

    if index_of_max != -1:     
        path_memo[i].extend(path_memo[index_of_max])
        
    memo[i] = current_max
    return current_max




sequence = [5, 2, 8, 6, 3, 6, 9, 5]
print("The longest increasing subsequence has ", LongestIncreasingSubsequence(sequence), " values.")