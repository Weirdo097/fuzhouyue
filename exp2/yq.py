import sys
txt_name = sys.argv[1]  # 命令行传入“yq_in.txt”

with open(txt_name, "r", encoding='gbk')as r:
    txt = r.readlines()  # 读取文件内容，返回列表

l_list = []  # l_list 列表存放去掉'\n'后的若干组字符串
for line in txt:  # line --> 字符串
    line = line.strip('\n')  # 去掉’\n‘,返回字符串
    l_list.append(line)

flag = ''
c_list = [] # 存放切分好的字符串
for i in range(len(l_list)):
    loc = l_list[i].split('\t', 1)[0]
    if flag == loc:
        c = l_list[i].split('\t', 1)[1] + '\n'
        c_list.append(c)
    else:
        if i == 0:  # 当loc=='浙江省'，不输出前面的'\n'
            p = l_list[i].split('\t', 1)[0] + '\n'
        else:
            p = '\n' + l_list[i].split('\t', 1)[0] + '\n'

        c_list.append(p)
        c = l_list[i].split('\t', 1)[1] + '\n'
        c_list.append(c)
        flag = loc

with open("yp_out.txt", "w", encoding='gbk') as w:
    w.write(''.join(c_list))
