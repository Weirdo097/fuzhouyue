import sys  # 命令行传参
from pypinyin import lazy_pinyin  # 将汉字转化成拼音进行排序


# 读入文件
def ReadTxt(txt_in):
    with open(txt_in, "r", encoding='gbk')as r:
        yq_txt = r.readlines()  # 读取文件内容，返回列表
    return yq_txt


# 写出文件
def WriteTxt(txt_out, write_list):
    with open(txt_out, "w", encoding='gbk') as w:
        w.write(''.join(write_list))


# 去除换行符
def cut(txt):
    l_list = []  # l_list 列表存放去掉'\n'后的若干组字符串
    for line in txt:  # line --> 字符串
        string = line.strip('\n')  # 去掉’\n‘,返回字符串
        l_list.append(string)
    return l_list


# 切分字符串：转换成['xx省'，'xx市','数字']的形式
def ListToArray(l_list):
    c_list = []  # 存放按照制表符切分好的小数组
    for i in range(len(l_list)):
        string = l_list[i].split('\t')
        c_list.append(string)
    return c_list


# exp3
# 筛选指定省份
def screen(flag, array_list):
    screen_list = []
    for i in range(len(array_list)):
        loc = array_list[i][0]
        if flag == loc:
            city_num = array_list[i][1] + '\t' + array_list[i][2] + '\n'
            screen_list.append(city_num)
    return screen_list


# exp4
# 汇总：汇总各省患病人数，并按照人数递减的顺序排列
def ProvinceSum(arrange_list):
    final_list = []  # 存放按照患病总数排好序的[xx省，总数]小数组
    flag = arrange_list[0][0]
    total = 0
    # 各省患病人数汇总
    for i in range(len(arrange_list)):
        province = arrange_list[i][0]
        if flag == province:
            num = int(arrange_list[i][2])
            data = [province, num]
            total = total + data[1]
            data[1] = total
            # 若读取最后一个省份，则直接把data加入列表
            if i == len(arrange_list) - 1:
                final_list.append(data)
        else:
            # 把上一个省份的data加入列表
            final_list.append(data)
            total = 0  # 当省份不相等时，重置总数
            # 在不相等时，将此时读取到的[province，num]加入列表
            num = int(arrange_list[i][2])
            data = [province, num]
            total = total + data[1]
            data[1] = total
            # 修改当前省份
            flag = province
    # 将省份按照患病总数递减的顺序排序
    sorted_list = sorted(final_list, key=lambda final_list: final_list[1], reverse=True)
    return sorted_list  # 格式为：[xx省，xx（数字）]


# 排序：1、省间按照患病总数递减排序；若总数一样，按照字母大小排序；2、市间按照患病人数排序；若患病人数一样，按照字母大小排序
def ArrangeCity(c_list, province):
    num_arrange = []  # 存放“患病人数”转换成int类型时的小数组
    arrange = []  # 存放按照患病人数排序后的小数组
    province_arrange = []  # 存放按照省份归类后的小数组

    for i in range(len(c_list)):
        c_list[i][2] = int(c_list[i][2])  # 将string转换成int类型
        num_arrange.append(c_list[i])
        arrange = sorted(num_arrange, key=lambda num_arrange: num_arrange[2], reverse=True)  # 按照患病人数排序
    # 省排序
    # province：按照患病总数递减的省列表
    for j in range(len(province)):
        p1 = province[j][0]
        for k in range(len(arrange)):
            p2 = arrange[k][0]
            if p1 == p2:
                province_arrange.append(arrange[k])  # 把相同省份的小数组聚集在一起（按照递减顺序）
    # 市排序
    # province_arrange：按照省份归类后的列表
    length = len(province_arrange)
    for m in range(0, length - 1):
        min_index = m
        for n in range(m + 1, length):
            if province_arrange[min_index][0] == province_arrange[n][0]:  # 若省份相同，则比较患病人数的大小
                if province_arrange[min_index][2] == province_arrange[n][2]:  # 若患病人数相同，则比较城市拼音字母的大小
                    if lazy_pinyin(province_arrange[min_index][1]) > lazy_pinyin(province_arrange[n][1]):
                        min_index = n
        # 交换
        if m != min_index:
            temp = province_arrange[min_index]
            province_arrange[min_index] = province_arrange[m]
            province_arrange[m] = temp

    return province_arrange


# 输出：1、省+患病总数 只出现一次； 2、市+患病人数 换行依次出现；3、各省之间间隔一行
def OutTxt(p_num, pc_num):
    out_list = []
    for i in range(len(p_num)):
        p1 = p_num[i][0]
        total_num = str(p_num[i][1])
        if i == 0:
            p = p1 + '\t' + total_num + '\n'  # [省，总数]
        else:
            p = '\n' + p1 + '\t' + total_num + '\n'
        flag = ''
        for j in range(len(pc_num)):
            p2 = pc_num[j][0]
            if p1 == p2:
                c = pc_num[j][1] + '\t' + str(pc_num[j][2]) + '\n'  # [市，该市总数]
                if flag == p2:
                    out_list.append(c)
                if flag == '':
                    out_list.append(p)
                    flag = p2
    return out_list


def main():
    # exp3
    if len(sys.argv) == 4:
        # 读取数据
        yq_txt = ReadTxt(sys.argv[1])  # sys.argv[1]：命令行传入的“yq_in04.txt”
        # 设置变量存放传入的“yq_out04.txt”和“浙江省”
        yq_out_txt = sys.argv[2]  # sys.argv[2]：命令行传入的参数“yq_out04.txt”
        load = sys.argv[3]  # sys.argv[3]：命令行传入的参数“浙江省”

        # 数据处理
        line_List = cut(yq_txt)
        array = ListToArray(line_List)

        # 筛选数据
        screen_list = screen(load, array)
        # 写出数据
        WriteTxt(yq_out_txt, screen_list)

    # exp4
    if len(sys.argv) == 3:
        # 读取数据
        yq_txt = ReadTxt(sys.argv[1])  # sys.argv[1]：命令行传入的“yq_in03.txt”
        yq_out_txt = sys.argv[2]  # sys.argv[2]：命令行传入的参数“yq_out03.txt”
        # 数据处理
        line_List = cut(yq_txt)
        array = ListToArray(line_List)

        # 计算各省患病总数
        ProvinceSum_list = ProvinceSum(array)
        # 排序
        arrange_list = ArrangeCity(array, ProvinceSum_list)
        # 设置输出格式
        out_list = OutTxt(ProvinceSum_list, arrange_list)
        WriteTxt(yq_out_txt, out_list)


if __name__ == "__main__":
    main()
