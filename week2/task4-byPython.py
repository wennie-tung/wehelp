def get_number(index):
    base = 4  # 起始值
    increment = 3  # 每個區塊的增量 3
    block_index = (index - 1) // 2  # 取得所在區塊的索引
    print(base + block_index * increment - (1 if index % 2 == 0 else 0))

get_number(1)  # Output: 4
get_number(5)  # Output: 10
get_number(10)  # Output: 15