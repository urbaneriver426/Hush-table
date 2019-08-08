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
            flag = False
            cont = True
            while cont == True:
                slot_number += 3
                if slot_number >= self.size:
                    if flag == False:
                        slot_number = slot_number - self.size
                        flag = True
                    else:
                        return None
                if self.slots[slot_number] is None:
                    return slot_number
        return None

    def put(self, value):
        slot_number = self.seek_slot(value)
        if slot_number is not None:
            self.slots[slot_number] = value
            return slot_number
        else:
            return None
