class LRUCache:

    def __init__(self, capacity=16):
        self.entries = {}
        self.capacity = capacity

    def put(self, key, value):
        for c_key in self.entries.keys():
            self.entries[c_key] = (
                self.entries[c_key][0], self.entries[c_key][1] + 1)
        self.entries[key] = (value, 1)
        for c_key in self.entries.keys():
            if self.entries[c_key][1] > self.capacity:
                del self.entries[c_key]
                break

    def get(self, key):
        try:
            index = self.entries[key][1]
            for c_key in self.entries.keys():
                if self.entries[c_key][1] < index:
                    self.entries[c_key] = (
                        self.entries[c_key][0], self.entries[c_key][1] + 1)
            self.entries[key] = (self.entries[key][0], 1)
            return self.entries[key][0] if key in self.entries.keys() else None
        except (KeyError):
            return None


cache = LRUCache(2)

cache.put("Petrov", 55521)
cache.put("Kuznecov", 97832)
cache.put("chase", 2134567890)

print(cache.get("Kuznecov"))
print(cache.get("Petrov"))


print(cache.get("should_get_None"))
