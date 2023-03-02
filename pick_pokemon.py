type_table = {
    "一般": 0,  # normal
    "格斗": 1,  # fighting
    "飞行": 2,  # flying
    "毒": 3,  # poison
    "地面": 4,  # ground
    "岩石": 5,  # rock
    "虫": 6,  # bug
    "幽灵": 7,  # ghost
    "钢": 8,  # steel
    "火": 9,  # fire
    "水": 10,  # water
    "草": 11,  # grass
    "电": 12,  # electric
    "超能力": 13,  # psychic
    "冰": 14,  # ice
    "龙": 15,  # dragon
    "恶": 16,  # dark
    "妖精": 17  # fairy
}
counter_table = [
    [1, 1, 1, 1, 1, 0.5, 1, 0, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 0.5, 0.5, 1, 2, 0.5, 0, 2, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5],
    [1, 2, 1, 1, 1, 0.5, 2, 1, 0.5, 1, 1, 2, 0.5, 1, 1, 1, 1, 1],
    [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2],
    [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1],
    [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5],
    [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 1, 2, 1, 1, 2],
    [1, 1, 1, 1, 1, 0.5, 2, 1, 2, 0.5, 0.5, 2, 1, 1, 2, 0.5, 1, 1],
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 1, 0.5, 1, 1],
    [1, 1, 0.5, 0.5, 2, 2, 0.5, 1, 0.5, 0.5, 2, 0.5, 1, 1, 1, 0.5, 1, 1],
    [1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 2, 0.5, 0.5, 1, 1, 0.5, 1, 1],
    [1, 2, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 0, 1],
    [1, 1, 2, 1, 2, 1, 1, 1, 0.5, 0.5, 0.5, 2, 1, 1, 0.5, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 1, 2, 1, 0],
    [1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 0.5],
    [1, 2, 1, 0.5, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 1, 1, 2, 2, 1]
]
while True:
    enemy_types = []
    tera_type = None
    tera_filter = []
    res = []
    enemy_info = input("原本属性以及太晶属性：").split(" ")
    tera_type = enemy_info[-1]
    enemy_types = enemy_info[:-1]
    for attack_type in range(len(counter_table)):
        if counter_table[attack_type][type_table[tera_type]] >= 1:
            tera_filter.append(attack_type)
    res2x = []
    res1x = []
    for attack_type in tera_filter:
        flag = 0
        for enemy_type in enemy_types:
            if counter_table[type_table[enemy_type]][attack_type] == 2:
                flag = 1
                break
        if flag == 0:
            if counter_table[attack_type][type_table[tera_type]] == 2:
                res2x.append(attack_type)
            else:
                res1x.append(attack_type)
    if len(res2x) != 0:
        res = res2x
        res_str = ['2x']
    else:
        res = res1x
        res_str = ['1x']
    for i in res:
        for j in type_table:
            if type_table[j] == i:
                res_str.append(j)
    print(res_str)
