class Select:
    # 初始化方法
    def __init__(self, TxtIn, TxtOut, province):
        self.TxtIn = TxtIn
        self.TxtOut = TxtOut    # self.属性 = 传进来的形参
        self.province = province

    # 读入文件
    def ReadTxt(self):
        with open(self.TxtIn, "r", encoding='gbk')as r:
            yq_txt = r.readlines()  # 读取文件内容，返回列表
        return yq_txt

    # 去除换行符
    def cut(self):
        txt = self.ReadTxt()
        l_list = []  # l_list 列表存放去掉'\n'后的若干组字符串
        for line in txt:  # line --> 字符串
            string = line.strip('\n')  # 去掉’\n‘,返回字符串
            l_list.append(string)
        return l_list

    # 切分字符串
    def ListToArray(self):
        l_list = self.cut()
        c_list = []  # 存放按照制表符切分好的小数组
        for i in range(len(l_list)):
            string = l_list[i].split('\t')
            c_list.append(string)
        return c_list

    # 筛选指定省份
    def screen(self):
        array_list = self.ListToArray()
        flag = self.province
        screen_list = []
        for i in range(len(array_list)):
            loc = array_list[i][0]
            if flag == loc:
                city_num = array_list[i][1] + '\t' + array_list[i][2] + '\n'
                screen_list.append(city_num)
        return screen_list

    # 写出文件
    def WriteTxt(self):
        txt_out = self.TxtOut
        write_list = self.screen()
        with open(txt_out, "w", encoding='gbk') as w:
            w.write(''.join(write_list))
