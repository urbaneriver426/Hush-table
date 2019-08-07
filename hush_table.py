class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):        
        result = 0
        for i in range(len(value)):
            result += (ord(value[i]) * (1+i))
        result = result % self.size
        return result
    
    def seek_slot(self, value):
        slot_number = self.hash_fun(value)
        if self.slots[slot_number] is None:
            return slot_number
        else:
            for i in range(-slot_number+self.step, slot_number, self.step):
                if i < 0:
                    x = i*(-1)
                    print("x", x)
                if self.slots[x] is None:
                    return x
        return None

    def put(self, value):
        slot_number = self.seek_slot(value)
        if slot_number is not None:
            self.slots[slot_number] = value
            return slot_number
        else:
            return None

    def find(self, value):
        # находит индекс слота со значением, или None
        return None

hash = HashTable(17,3)
print(hash.hash_fun("a"))
print(hash.seek_slot("a"))
print(hash.put("a"))
print(hash.put("a"))
