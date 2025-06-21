file = open(r'C:\Python\president_height.csv', mode='rt')
file_list = file.readlines()
file_list.pop(0)
print(file_list)
names = []
heights = []
for line in file_list:
    print(line)

    val = line.split(',')
    print(val)

    height = int(val[2].strip('\n'))
    print(height)

    heights.append(height)
    names.append(val[1])

print(heights)
print(names)
max_height = max(heights)
print(max_height)
index_max_height = heights.index(max_height)
print(index_max_height)
print(names[index_max_height])

x = 0
for x in range(6):
    max_height = max(heights)
    print (max_height)
    heights.pop(heights.index(max_height))
x += 1



