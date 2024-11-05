
immutable_var=(0, 1, 2, False, 'apple')
print(immutable_var)
#print(type(immutable_var))


 ##попытка изменить элементы кортежа
# #immutable_var[3]="Text" # (обоснованная ошибка)
print('Неизменяем, но может хранить в себе изменяемые объекты:', immutable_var)


#               0           1       2       3
mutable_list=['python', 'urban', 'module', 1.5]
print(mutable_list)
#print(type(mutable_list))

 #элементы списка mutable_list изменены
mutable_list[0]='programms'
mutable_list[2]='module1.5.py'
mutable_list.remove(1.5)
  #Вывод измененного списка mutable_list.
print('Update_list:', mutable_list)