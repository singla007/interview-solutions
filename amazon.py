#
# z = list(map(int, input().split(" ")))
#
# print(z)


def maxValue(n, rounds):
    arr = n*[0]
    for i in rounds:
        start_ind = i[0] - 1
        last_ind = i[1]
        investment = i[2]
        for j in range(start_ind,last_ind):
            arr[j] = arr[j]+investment

    return max(arr)

print("hello")
print(maxValue(4, [[2,3,603],[1,1,286],[4,4,882]]))