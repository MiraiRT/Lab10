def insert(list, data):
    list.append(data)
    return procedure(list, len(list) - 1)


def procedure(list, index):
    if index // 2 > 0:
        if list[index // 2] > list[index]:
            tmp = list[index // 2]
            list[index // 2] = list[index]
            list[index] = tmp
        procedure(list, index // 2)
    return list


def print90(list, index, lvl):
    if 2 * index + 1 < len(list):
        print90(list, 2 * index + 1, lvl + 1)
    print(lvl * '   ', list[index])
    if 2 * index < len(list):
        print90(list, 2 * index, lvl + 1)


def delMin(list):
    tmp = list[1]
    findPlace = list[len(list) - 1]
    rotateMin(list, 1, findPlace)
    list[len(list) - 1] = tmp
    return list.pop(len(list) - 1)


def rotateMin(list, index, findPlace):
    if 2 * index + 1 < len(list) and 2 * index < len(list):
        if findPlace < list[2 * index] and findPlace < list[2 * index + 1]:
            list[index] = findPlace
        elif list[2 * index] < list[2 * index + 1]:
            list[index] = list[2 * index]
            rotateMin(list, 2 * index, findPlace)
        else:
            list[index] = list[2 * index + 1]
            rotateMin(list, 2 * index + 1, findPlace)


l = [68, 65, 32, 24, 26, 21, 19, 13, 16, 14]
h = [None]
for ele in l:
    h = insert(h, ele)
    print('Print 90 :')
    print90(h, 1, 0)


