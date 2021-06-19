def binary_search(a, x):
    # 탐색할 범위를 저장하는 변수 start, end
    # 리스트 전체를 범위로 탐색 시작(0 ~ len(a)-1)

    start = 0
    end = len(a) - 1 # 컴퓨터는 0부터 세기때문에 if d = [1,2,3,4,5] len(d) = 5

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1 # 찾지 못했을 때

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d,36))
print(binary_search(d,50))