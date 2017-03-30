import csv
import hashlib
import unittest


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


class TestHash(unittest.TestCase):
    def test_hash_sha1(self):
        self.assertEqual(create_hash('I love Python', 'sha1'), '9233eac58259dd3a13d6c9c59f8001823b6b1fee')

    def test_hash_sha512(self):
        self.assertEqual(create_hash('I love Python', 'sha512'), '9233eac58259dd3a13d6c9c59f8001823b6b1fee')

    def test_hash_md5(self):
        self.assertEqual(create_hash('I love Python', 'md5'), '9233eac58259dd3a13d6c9c59f8001823b6b1fee')

