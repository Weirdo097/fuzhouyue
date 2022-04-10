from pypinyin import lazy_pinyin  # ������ת����ƴ����������


class Sort:
    # ��ʼ������
    def __init__(self, TxtIn, TxtOut):
        # self.����= ���������β�
        self.TxtIn = TxtIn
        self.TxtOut = TxtOut

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

    # �з��ַ�����ת����['xxʡ'��'xx��','����']����ʽ
    def ListToArray(self):
        l_list = self.cut()
        c_list = []  # ��Ű����Ʊ���зֺõ�С����
        for i in range(len(l_list)):
            string = l_list[i].split('\t')
            c_list.append(string)
        return c_list

    # ���ܣ����ܸ�ʡ���������������������ݼ���˳������
    def ProvinceSum(self):
        arrange_list = self.ListToArray()
        final_list = []  # ��Ű��ջ��������ź����[xxʡ������]С����
        flag = arrange_list[0][0]
        total = 0
        # ��ʡ������������
        for i in range(len(arrange_list)):
            province = arrange_list[i][0]
            if flag == province:
                num = int(arrange_list[i][2])
                data = [province, num]
                total = total + data[1]
                data[1] = total
                # ����ȡ���һ��ʡ�ݣ���ֱ�Ӱ�data�����б�
                if i == len(arrange_list) - 1:
                    final_list.append(data)
            else:
                # ����һ��ʡ�ݵ�data�����б�
                final_list.append(data)
                total = 0  # ��ʡ�ݲ����ʱ����������
                # �ڲ����ʱ������ʱ��ȡ����[province��num]�����б�
                num = int(arrange_list[i][2])
                data = [province, num]
                total = total + data[1]
                data[1] = total
                # �޸ĵ�ǰʡ��
                flag = province
        # ��ʡ�ݰ��ջ��������ݼ���˳������
        sorted_list = sorted(final_list, key=lambda final_list: final_list[1], reverse=True)
        return sorted_list  # ��ʽΪ��[xxʡ��xx�����֣�]

    # ����
    # 1��ʡ�䰴�ջ��������ݼ�����������һ����������ĸ��С����
    # 2���м䰴�ջ���������������������һ����������ĸ��С����
    def ArrangeCity(self):
        c_list = self.ListToArray()
        province = self.ProvinceSum()

        num_arrange = []  # ��š�����������ת����int����ʱ��С����
        arrange = []  # ��Ű��ջ�������������С����
        province_arrange = []  # ��Ű���ʡ�ݹ�����С����

        for i in range(len(c_list)):
            c_list[i][2] = int(c_list[i][2])  # ��stringת����int����
            num_arrange.append(c_list[i])
            arrange = sorted(num_arrange, key=lambda num_arrange: num_arrange[2], reverse=True)  # ���ջ�����������
        # ʡ����
        # province�����ջ��������ݼ���ʡ�б�
        for j in range(len(province)):
            p1 = province[j][0]
            for k in range(len(arrange)):
                p2 = arrange[k][0]
                if p1 == p2:
                    province_arrange.append(arrange[k])  # ����ͬʡ�ݵ�С����ۼ���һ�𣨰��յݼ�˳��
        # ������
        # province_arrange������ʡ�ݹ������б�
        length = len(province_arrange)
        for m in range(0, length - 1):
            min_index = m
            for n in range(m + 1, length):
                if province_arrange[min_index][0] == province_arrange[n][0]:  # ��ʡ����ͬ����Ƚϻ��������Ĵ�С
                    if province_arrange[min_index][2] == province_arrange[n][2]:  # ������������ͬ����Ƚϳ���ƴ����ĸ�Ĵ�С
                        if lazy_pinyin(province_arrange[min_index][1]) > lazy_pinyin(province_arrange[n][1]):
                            min_index = n
            # ����
            if m != min_index:
                temp = province_arrange[min_index]
                province_arrange[min_index] = province_arrange[m]
                province_arrange[m] = temp

        return province_arrange

    # �����1��ʡ+�������� ֻ����һ�Σ� 2����+�������� �������γ��֣�3����ʡ֮����һ��
    def OutTxt(self):
        p_num = self.ProvinceSum()
        pc_num = self.ArrangeCity()

        out_list = []
        for i in range(len(p_num)):
            p1 = p_num[i][0]
            total_num = str(p_num[i][1])
            if i == 0:
                p = p1 + '\t' + total_num + '\n'  # [ʡ������]
            else:
                p = '\n' + p1 + '\t' + total_num + '\n'
            flag = ''
            for j in range(len(pc_num)):
                p2 = pc_num[j][0]
                if p1 == p2:
                    c = pc_num[j][1] + '\t' + str(pc_num[j][2]) + '\n'  # [�У���������]
                    if flag == p2:
                        out_list.append(c)
                    if flag == '':
                        out_list.append(p)
                        flag = p2
        return out_list

    # д���ļ�
    def WriteTxt(self):
        txt_out = self.TxtOut
        write_list = self.OutTxt()
        with open(txt_out, "w", encoding='gbk') as w:
            w.write(''.join(write_list))
