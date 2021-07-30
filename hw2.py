# 1. После запуска предлагает пользователю ввести текст, содержащий любые слова,
# слоги, числа или их комбинации, разделенные пробелом.
# 2. Считывает строку с текстом, и разбивает его на элементы списка, считая
# пробел символом разделителя.
# 3. Печатает этот же список элементов (через пробел), однако с удаленными
# дубликатами.

input_list = input().split()
buff = {}
res_list = " ".join([buff.setdefault(x, x) for x in input_list if x not in buff])
print(res_list)
