def string_sum(array):
    if array == []:
        return 0
    else:
        return len(array[0]) + string_sum(array[1:])
answer = string_sum(["ab", "c", "def", "ghi"])
print(answer)

def evenn(array):
    if array == []:
        return []
    elif array[0] % 2 == 0:
        return [array[0]] + evenn(array[1:])
    else:
        return evenn(array[1:])
new_answer = evenn([1,2,3,4,5,6,7,8,9,10])
print(new_answer)

def triangular_numbers(n):
    if n == 0:
        return 0
    else:
        return n + triangular_numbers(n-1)
numbers = triangular_numbers(7)
print(numbers)

def find_x(string, index=0):
    if string == "x":
        return index
    else:
        return find_x(string[1:], index+1)

x=find_x("abdcex")
print(x)

def unique_paths(rows, columns):
    if rows==1 or columns == 1:
        return 1
    else:
        return unique_paths(rows-1, columns) + unique_paths(rows, columns-1)
find_path=unique_paths(3, 2)
print(find_path)

from itertools import count

print(next(iter(count(0, 10))))
