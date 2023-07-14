def func(*data):
    # 找出每一組的第二個字，放進列表
    middle_names = get_middle_names(data)

    result = {}
    for middle_name in middle_names:
        if middle_name in result:
            result[middle_name] += 1
        else:
            result[middle_name] = 1

    # flag
    not_unique_name = True
    for key, value in result.items():
        if value == 1:
            print(data[middle_names.index(key)])
            # 當有唯一一個中間名出現時，把 not_unique_name 設為 False
            not_unique_name = False

    if not_unique_name:
        print("沒有")


# 利用函式找出每個姓名的第二個字，並放入 middle_names 列表
def get_middle_names(names):
    middle_names = []
    for name in names:
        middle_names.append(name[1])  # 取第二個字
    return middle_names


func("彭大牆", "王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
