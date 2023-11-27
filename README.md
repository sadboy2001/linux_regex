Для подсчета общего количества выполненных запросов можно просто посчитать количество строк в лог-файле.

Для подсчета количества запросов по HTTP-методам можно использовать библиотеку re в сочетании с командой search. Например, чтобы подсчитать количество запросов методом GET или POST, можно выполнить следующую команду:

if re.search(r'POST', line):
  post_count += 1

Аналогично можно подсчитать количество запросов для других методов, перечисленных в RFC 7231 и RFC 5789.

Для определения топ-3 IP-адресов, с которых были сделаны запросы, можно использовать команду re.findall. Например, чтобы вывести список IP-адресов и количество запросов для каждого адреса, можно выполнить следующую команду:

ip_addresses = re.findall(ip_addr, data)
  top_3_ip_addresses = Counter(ip_addresses).most_common(3)

Для определения топ-3 самых долгих запросов можно использовать команду re.search в сочетании с командой sort. Например, чтобы вывести список запросов, отсортированных по времени выполнения в порядке убывания, можно выполнить следующую команду:

regex_time = r'[0-9]+$'
match1 = re.search(regex_time, line)
  if match1:
    i.append(int(match1.group()))
i.sort(reverse=True)
a = str(i[0])

В этой команде мы используем поиск элементов, чтобы выбрать IP-адрес, URL и время выполнения запроса. Затем мы сортируем результаты по времени выполнения в порядке убывания и выводим топ-3 запросов.
