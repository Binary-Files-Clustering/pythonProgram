class SparseVector:
    def __init__(self):
        self.values = {}

    def __getitem__(self, item):
        if item in self.values:
            return self.values[item]
        return 0

    def __setitem__(self, key, value):
        self.values[key] = value

