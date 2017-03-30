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


file_write = []
with open('need_hashes.csv', 'r', encoding='cp1251') as file:
    reader = csv.reader(file, delimiter=';')
    for data in reader:
        result = create_hash(data[0], data[1])
        data[2] = result
        file_write.append(data)

with open('need_hashes1.csv', 'a', newline='') as f:
    writer = csv.writer(f,delimiter=';')
    for row in file_write:
        writer.writerow(row)



class TestHash(unittest.TestCase):
    def test_hash_sha1(self):
        self.assertEqual(create_hash('I love Python', 'sha1'), '9233eac58259dd3a13d6c9c59f8001823b6b1fee')

    def test_hash_sha512(self):
        self.assertEqual(create_hash('Guido like beer', 'sha512'),
                         '9490ca5a146f482ea40649b832017dbec7279462766ec6e02fac4c7910584c50572b3efd3d257c089431b8b88603226a9d3aa2fcd4185fcc8db9f71114e06d93')

    def test_hash_md5(self):
        self.assertEqual(create_hash('Я люблю Питон', 'md5'), '1190b0a5e7b09ec3145999044c728854')


if __name__ == '__main__':
    unittest.main()
