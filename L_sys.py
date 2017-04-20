# This module is a class that represents an L-system string generator


class L_sys:
    def __init__(self):
        self.alphabet = set()
        self.seed = ''
        self.rules = {}
        self.string = ''
        
    def make_alphabet(self,S):
        self.alphabet = set(c for c in S)
        for c in S:
            self.rules[c] = c
            
    def make_seed(self,S):
        for c in S:
            if c not in self.alphabet:
                return
        self.seed = S
        self.string = S

    def make_rule(self,c, R):
        for s in R:
            if s not in self.alphabet:
                return
        self.rules[c] = R

    def gen_next(self):
        s = ''
        for c in self.string:
            s += self.rules[c]
        self.string = s
        return s
            
    def __repr__(self):
        return 'L-system string generator\n Current string: "%s"'%self.string

# factory method
def create_sys(alphabet, seed):
    sys = L_sys()
    sys.make_alphabet(alphabet)
    if seed in sys.alphabet:
        sys.make_seed(seed)
        return sys





