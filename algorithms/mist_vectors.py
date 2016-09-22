from math import sqrt


class MistInstruction:
    def __init__(self, inst_str):
        self.categ = int(inst_str[:inst_str.find(" ")], 16)
        self.inst = int(inst_str[inst_str.find(" ")+1: inst_str.find(" | ")], 16)
        args_str = inst_str[inst_str.find(" | ")+3:]
        self.args = []
        for arg in args_str.split(" "):
            self.args.append(int(arg, 16))

    def __repr__(self):
        return str(self.categ) + " " + str(self.inst) + " | " + " ".join([str(arg) for arg in self.args])

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)


class InstructionSet:
    def __init__(self, inst_lst):
        self.lst = inst_lst

    def __eq__(self, other):
        return self.lst == other.lst

    def __hash__(self):
        return sum([hash(inst) for inst in self.lst])


class SparseVector:
    """
    ATTENTION! The dictionary keys are of type InstructionSet just FYI.
    """
    def __init__(self):
        self.values = {}

    def __getitem__(self, item):
        if item in self.values:
            return self.values[item]
        return 0

    def __setitem__(self, key, value):
        self.values[key] = value

    def normal(self):
        return sqrt(sum(pow(val, 2) for val in self.values.values()))

    def scale(self):
        normal = self.normal()
        for key in self.values:
            self.values[key] /= normal


class MISTVector:
    """
    ATTENTION! The dictionary keys are of type InstructionSet just FYI.
    """
    def __init__(self, dir_path, file_name):
        self.vec = create_vector_from_file(dir_path+file_name)
        self.name = file_name[:file_name.find(".")]

    def __getitem__(self, item):
        return self.vec[item]

    def __setitem__(self, key, value):
        self.vec[key] = value


def create_vector_from_file(mist_file_path):
    Q = 2
    with open(mist_file_path) as f:
        str_instructions = f.readlines()
    vec = SparseVector()
    for i in xrange(len(str_instructions)-Q):
        key = InstructionSet([MistInstruction(str_instructions[i+j]) for j in xrange(Q)])
        if key in vec:
            vec[key] += 1
        else:
            vec[key] = 1
    vec.scale()
    return vec



