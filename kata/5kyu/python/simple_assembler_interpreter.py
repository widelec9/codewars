class Assembler:
    def __init__(self):
        self.inst = {'mov': self.mov, 'inc': self.inc, 'dec': self.dec, 'jnz': self.jnz}
        self.reg = dict()
        self.pc = 0
    
    def get_reg(self):
        return self.reg
    
    def exec(self, prog):
        prog = [(instr.split()[0], [str(op) for op in instr.split()[1:]]) for instr in prog]
        while self.pc < len(prog):
            self.inst[prog[self.pc][0]](*prog[self.pc][1])
    
    def mov(self, r, v):
        self.reg[r] = int(v) if v.lstrip('-').isnumeric() else self.reg[v]
        self.pc += 1
    
    def inc(self, r):
        self.reg[r] += 1
        self.pc += 1
    
    def dec(self, r):
        self.reg[r] -= 1
        self.pc += 1
    
    def jnz(self, v, j):
        if (v.isdigit() and int(v) != 0) or (v in self.reg.keys() and self.reg[v] != 0):
            self.pc += int(j)
        else:
            self.pc += 1


def simple_assembler(program):
    a = Assembler()
    a.exec(program)
    return a.get_reg()


code = '''\
mov a -10
mov b a
inc a
dec b
jnz a -2'''
print(simple_assembler(code.splitlines()))

# code = '''\
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a'''
# print(simple_assembler(code.splitlines()), {'a': 1})

# code = '''\
# mov c 12
# mov b 0
# mov a 200
# dec a
# inc b
# jnz a -2
# dec c
# mov a b
# jnz c -5
# jnz 0 1
# mov c a'''
# print(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})
