"""
冒泡排序:始终是相邻的两个元素相比较，如果前面的比后面大就交换两个位置的值
"""


def bubble_sort(aList):
    n = len(aList)
    for j in range(n - 1):
        b = False
        for i in range(n - j - 1):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                b = True
        if b == False:
            break


"""
选择排序：默认第一位就是最小的，用第一跟后面的所有人比较，遇见一个更小的就记录当前的下标，一轮下来就能记录哪个是最小，然后用第一个与最小的数值交换
"""


def select_sort(aList):
    n = len(aList)
    for j in range(n - 1):
        minIndex = j
        for i in range(j + 1, n):
            if aList[minIndex] > aList[i]:
                minIndex = i
        aList[j], aList[minIndex] = aList[minIndex], aList[j]


"""
插入排序：假如前面第一个元素是有序的，用后面的逐个元素插入到前面的有序序列里面去
"""


def insert_sort(aList):
    n = len(aList)
    for j in range(n - 1):
        i = j
        while i >= 0:
            if aList[i + 1] < aList[i]:
                aList[i], aList[i + 1] = aList[i + 1], aList[i]
                i -= 1
            else:
                break


"""
希尔排序：设置一个间隔取出相应位置的值，然后把这些值进行插入排序，然后取一个间隔小一点的值，再进行插入排序
"""


def shell_sort(aList):
    n = len(aList)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            while i > 0:
                if aList[i] < aList[i - gap]:
                    aList[i], aList[i - gap] = aList[i - gap], aList[i]
                    i -= gap
                else:
                    break
        gap //= 2


"""
快速排序：先取出第一个元素，low游标从左边开始碰到比第一个元素大的就停住，hight游标从右边开始碰到比第一个元素小的就停住，然后交换low游标处与hight游标处的值,直到两个游标重合，第一个元素就在游标的前面位置
"""


def quick_sort(aList, first, last):
    if first >= last:
        return
    mid_value = aList[first]
    low = first
    hight = last
    while low < hight:
        while low < hight and aList[hight] >= mid_value:
            hight -= 1
        aList[low] = aList[hight]
        while low < hight and aList[low] < mid_value:
            low += 1
        aList[hight] = aList[low]
    aList[low] = mid_value
    quick_sort(aList, first, low - 1)
    quick_sort(aList, low + 1, last)


"""
归并排序：将元素进行对半拆分成单个元素，然后对各自拆出来的元素进行逐层合并
"""


def merge_sort(aList):
    n = len(aList)
    if n <= 1:
        return aList
    mid = n // 2
    left_list = merge_sort(aList[:mid])
    right_list = merge_sort(aList[mid:])
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_list) and right_point < len(right_list):
        if left_list[left_point] < right_list[right_point]:
            result.append(left_list[left_point])
            left_point += 1
        else:
            result.append(right_list[right_point])
            right_point += 1
    result += left_list[left_point:]
    result += right_list[right_point:]
    return result


"""
二分查找：每次取一半的值与目标值比较，在左边继续取左边的一半，在右边继续取右边的一半
"""


def binary_search(aList, item):
    n = len(aList)
    if n > 0:
        mid = n // 2
        if aList[mid] == item:
            return True
        elif aList[mid] < item:
            return binary_search(aList[mid + 1:], item)
        elif aList[mid] > item:
            return binary_search(aList[:mid], item)
    return False

"""
二叉树遍历：
1.层次遍历：从上往下，从左往右  0123456789
2.先序遍历：中 左 右  0137849256
3.中序遍历：左 中 右  7381940526
4.后序遍历：左 右 中  7839415620
"""


if __name__ == '__main__':
    a = [33, 2, 7, 55, 1, 24]
    # bubble_sort(a)
    # select_sort(a)
    # insert_sort(a)
    # shell_sort(a)
    # quick_sort(a,0,len(a)-1)
    a = merge_sort(a)
    print(binary_search(a, 24))
    print(binary_search(a, 25))
    print(a)
