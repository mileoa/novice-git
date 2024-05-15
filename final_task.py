# Функция проверки нахождения одной строки в другой.

def is_contain_substring(string, substring):
    # Проверяем до символа, после которого проверять нет смысла,
    # так как длинна подстроки будет больше кол-ва оставшихся символов.
    for i in range(len(string) - len(substring) + 1):
        for j in range(len(substring)):
            if substring[j] != string[i + j]:
                break
            # Если успешно проверили последний символ, 
            # то возвращаем True.
            elif j == len(substring) - 1:
                return True
    # Если проверили все необходимые символы в первой строке
    # и они не совпали с искомой подстрокой, то возвращаем False.
    return False

main_string = str(input("Введите строку, в которой будем искать: "))
string_to_search = str(input("Введите строку, которую будем искать: "))
print(is_contain_substring(main_string, string_to_search))
