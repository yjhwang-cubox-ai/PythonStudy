num_list = [1,2,3]

new_list = [n+1 for n in num_list]

name = "Angela"
name_list = [n for n in name]

double = [n*2 for n in range(1,5)]

print(new_list)
print(name_list)
print(double)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
long_names = [name.upper() for name in names if len(name)>5]

print(long_names)