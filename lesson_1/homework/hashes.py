import csv
import hashlib


def create_hash(data, hash):
    data = data.encode('cp1251')
    if hash == 'md5':
        h = hashlib.md5()
        h.update(data)
        return h.hexdigest()
    elif hash == 'sha1':
        h = hashlib.sha1()
        h.update(data)
        return h.hexdigest()
    elif hash == 'sha512':
        h = hashlib.sha512()
        h.update(data)
        return h.hexdigest()
    else:
        print('Неверный хеш метод')


with open('need_hashes.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for data in reader:
        print(', '.join(data))
        result = create_hash(data[0], data[1])
        data[2] = result
        print(data)