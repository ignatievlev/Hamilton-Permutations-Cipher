from typing import List

def gamilton_cypher(full_str: str, marchroute_list: List[List[int]], marchroute_input: List[int]) -> str:
    result = ''
    i = 0
    j = 0
    while i != len(full_str):
        sp = list(full_str[i: i + 8])
        string_convert = []

        for j in marchroute_input:
            for crypto_key in marchroute_list[j]:
                string_convert.append(sp[crypto_key])
            result += ''.join(string_convert)
        i += 8

    return result

# маршруты шифрования с помощью которых выполняется обход строки
m1 = [4, 2, 5, 0, 1, 3, 6, 7]
m2 = [7, 1, 3, 6, 4, 2, 5, 0]
m3 = [3, 6, 1, 2, 4, 7, 0, 5]
m4 = [5, 0, 6, 3, 2, 1, 7, 4]
marchroute_list = [m1, m2, m3, m4]

string_input = input("Введите строку для шифрования:")
marchroute_input = list(map(int, input("Введите номера маршрутов шифрования через запятую:").split(',')))

len_string_input = len(string_input)

# если длина строки не кратна восьми, то заполним её звёздочками до длины, кратной восьми
if len_string_input % 8 != 0:
    full_str = string_input.ljust(len_string_input + 8 - len_string_input % 8, '*')
else:
    full_str = string_input

print("Зашифрованная строка:", gamilton_cypher(full_str, marchroute_list, marchroute_input))
