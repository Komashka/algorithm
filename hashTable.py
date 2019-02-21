class HashTable:
    def __init__(self, hash_type, values):
        self.coll = 0
        self.hash_type = hash_type
        self.values = values
        self.lst = [[] for i in range(int(len(self.values) * 1.2))]
        self.made()

    def made(self):
        if self.hash_type == 1 or self.hash_type == 2:
            for i in self.values:
                self.chained_add(i)
        else:
            for i in self.values:
                self.hash_insert(i)

    def chained_add(self, k):
        if self.hash_type == 1:
            key = self.division(k)
        elif self.hash_type == 2:
            key = self.multiplication(k)
        self.lst[key].append(k)
        if len(self.lst[key]) > 1:
            self.coll += 1

    def chained_search(self, k):
        if self.hash_type == 1:
            key = self.division(k)
        elif self.hash_type == 2:
            key = self.multiplication(k)
        if not self.lst[key]:
            return None
        else:
            return self.lst[key][0]

    def find_sum(self, s):
        if self.hash_type == 1 or self.hash_type == 2:
            for i in self.values:
                if self.chained_search(s - i) and s - i in self.values:
                    return i, s - i
        else:
            for i in self.values:
                if self.hash_search(s - i):
                    return i, s - i
        return None

    def hash_insert(self, k):
        i = 0
        while i != len(self.lst):
            if self.hash_type == 3:
                key = self.linear(k, i)
            elif self.hash_type == 4:
                key = self.powertwo(k, i)
            elif self.hash_type == 5:
                key = self.double(k, i)
            if not self.lst[key]:
                self.lst[key].append(k)
                return key
            else:
                self.coll += 1
                i += 1
        return "eroor"

    def hash_search(self, k):
        i = 0
        while i != len(self.lst):
            if self.hash_type == 3:
                key = self.linear(k, i)
            elif self.hash_type == 4:
                key = self.powertwo(k, i)
            elif self.hash_type == 5:
                key = self.double(k, i)
            if self.lst[key] == [k]:
                return True
            elif self.lst[key] == []:
                break
            else:
                i += 1
        return None

    def linear(self, k, i):
        m = len(self.values)
        return (k + i) % m

    def powertwo(self, k, i):
        return (k + 7 * i + 11 * (i ** 2)) % len(self.values)

    def double(self, k, i):
        h1 = self.division(k)
        h2 = 1 + (k % 2)
        return (h1 + i * h2) % len(self.lst)

    def multiplication(self, k):
        a = 0.618034
        return int((k * a % 1) * len(self.lst))

    def division(self, k):
        return k % len(self.lst)

    def get_collisions_amount(self):
        return self.coll