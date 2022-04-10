import sys  # 命令行传参
import tkinter
import difflib
import Select
import Sort
from tkinter import messagebox

# 筛选
if len(sys.argv) == 4:
    ZJ = Select.Select(sys.argv[1], sys.argv[2], sys.argv[3])
    ZJ.WriteTxt()

    # 弹出提示窗口
    root = tkinter.Tk()
    root.withdraw()  # 去掉root窗口
    tkinter.messagebox.showinfo(title='Info', message='成功执行')

    # 验证输出文件正确率
    a = open(ZJ.TxtOut).readlines()
    b = open('./true_out1.txt').readlines()
    s = difflib.SequenceMatcher(None, a, b)
    s_ratio = s.ratio()
    print('输出文件正确率：%.2f%%' % (s_ratio * 100))
# 排序
if len(sys.argv) == 3:
    ArrangeTotal = Sort.Sort(sys.argv[1], sys.argv[2])
    ArrangeTotal.WriteTxt()

    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo(title='Info', message='成功执行')
    # 验证输出文件正确率
    a = open(ArrangeTotal.TxtOut).readlines()
    b = open('./true_out2.txt').readlines()
    s = difflib.SequenceMatcher(None, a, b)
    s_ratio = s.ratio()
    print('输出文件正确率：%.2f%%' % (s_ratio * 100))
