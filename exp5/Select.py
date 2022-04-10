class Select:
    # ��ʼ������
    def __init__(self, TxtIn, TxtOut, province):
        self.TxtIn = TxtIn
        self.TxtOut = TxtOut    # self.���� = ���������β�
        self.province = province

    # �����ļ�
    def ReadTxt(self):
        with open(self.TxtIn, "r", encoding='gbk')as r:
            yq_txt = r.readlines()  # ��ȡ�ļ����ݣ������б�
        return yq_txt

    # ȥ�����з�
    def cut(self):
        txt = self.ReadTxt()
        l_list = []  # l_list �б���ȥ��'\n'����������ַ���
        for line in txt:  # line --> �ַ���
            string = line.strip('\n')  # ȥ����\n��,�����ַ���
            l_list.append(string)
        return l_list

    # �з��ַ���
    def ListToArray(self):
        l_list = self.cut()
        c_list = []  # ��Ű����Ʊ���зֺõ�С����
        for i in range(len(l_list)):
            string = l_list[i].split('\t')
            c_list.append(string)
        return c_list

    # ɸѡָ��ʡ��
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

    # д���ļ�
    def WriteTxt(self):
        txt_out = self.TxtOut
        write_list = self.screen()
        with open(txt_out, "w", encoding='gbk') as w:
            w.write(''.join(write_list))
