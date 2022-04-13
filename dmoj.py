def add_until_100(array):
    total=0
    for a in array:
        if total + a <= 100:
            total+=a
        else:
            break
    return total
print(add_until_100([1,2,3,4,5,6,7,8,9,10]))

def golomb(n, memory=dict()):
    if n == 1:
        return 1
    elif n in memory:
        return memory[n]
    else:
        number = 1 + golomb(n - golomb(golomb(n - 1)))
        memory[n] = number
        return number

print(golomb(100))

def unique_paths(rows, columns, memory=dict()):
    if rows==1 or columns==1:
        return 1
    elif f"{rows} {columns}" in memory:
        return memory[f"{rows} {columns}"]
    elif f"{columns} {rows}" in memory:
        return memory[f"{columns} {rows}"]
    else:
        row_m = unique_paths(rows-1, columns)
        column_m = unique_paths(rows, columns-1)
        memory[f"{rows} {columns}"] = row_m + column_m
        memory[f"{columns} {rows}"] = column_m + row_m
        return row_m + column_m
        
print(unique_paths(10, 20))
