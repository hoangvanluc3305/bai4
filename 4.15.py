print("HOÀNG VĂN LỰC")
print("MSSV:235752021610065")

chuoi = input('Nhập chuỗi cac tu tieng anh: ')
ds_list = chuoi.split()
ds_list.sort()
print('cac tu theo thu tu tu dien:')
for tu in ds_list:
    print(tu)
