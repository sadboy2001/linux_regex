import datetime
import re
import os
from collections import Counter


dirname = "/mnt/d/��������"
filename = 'access.log'

filepath = os.path.join(dirname, filename)

regex_time = r'[0-9]+$'
ip_addr = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

post_count = 0
get_count = 0
i = []
b = []

with open(filepath, 'r') as file:
    for line in file:
        if re.search(r'POST', line):
            post_count += 1

with open(filepath, 'r') as file:
    for line in file:
        if re.search(r'GET', line):
            get_count += 1

with open(filepath, 'r') as file:
    for line in file:
        match1 = re.search(regex_time, line)
        if match1:
            i.append(int(match1.group()))

i.sort(reverse=True)
a = str(i[0])

with open(filepath, 'r') as file:
    for line in file:
        if a in line:
            b.append(line)

with open(filepath, 'r') as file:
    lines = file.readlines()
    num_lines = len(lines)

with open(filepath, 'r') as file:
    data = file.read()
    ip_addresses = re.findall(ip_addr, data)
    top_3_ip_addresses = Counter(ip_addresses).most_common(3)

    print('���-3 IP-������� �� ���������� ��������:')
    for ip_address, count in top_3_ip_addresses:
        print(f'{ip_address}: {count}')

print(f'���������� POST-�������� � ����� {filename}: {post_count}')
print(f'���������� GET-�������� � ����� {filename}: {get_count}')
print(f'� ����� {filename} ���������� {num_lines} �����.')
print(f'����� ������ ������� � ������ ������ �����: \n{b[0]}\n{b[1]}\n{b[2]}')

filename = datetime.datetime.now().strftime('%d-%m-%Y-%H:%M-scan.json')
with open(filename, 'w') as f:
    f.write(f'���������� POST-�������� � ����� {filename}: {post_count}')
    f.write(f'���������� GET-�������� � ����� {filename}: {get_count}')
    f.write(f'� ����� {filename} ���������� {num_lines} �����.')
    f.write(f'����� ������ ������� � ������ ������ �����: \n{b[0]}\n{b[1]}\n{b[2]}')
