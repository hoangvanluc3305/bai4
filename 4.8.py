print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

day_tu = input('Nhập cac day tu: ').split()
max_length = max(len(tu) for tu in day_tu)
tu_dai_nhat = [tu for tu in day_tu if len(tu) == max_length]
print('Tu dai nhat:', ' '.join(tu_dai_nhat))
