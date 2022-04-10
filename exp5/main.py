# coding=utf-8
import sys  # 命令行传参
import Select
import Sort

# 筛选
if len(sys.argv) == 4:
    ZJ = Select.Select(sys.argv[1], sys.argv[2], sys.argv[3])
    ZJ.WriteTxt()

# 排序
if len(sys.argv) == 3:
    ArrangeTotal = Sort.Sort(sys.argv[1], sys.argv[2])
    ArrangeTotal.WriteTxt()

