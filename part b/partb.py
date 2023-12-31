def calc_probs(d):
    p = [0] * 11
    for i in range(1, 7):
        for j in range(1, 7):
            p[i + j - 2] += d.count(i) * d.count(j)
    t = sum(p)
    p = [x / t for x in p]
    return p
    
class LCG:
    def _init_(self, s=42, a=1664525, c=1013904223, m=2**32):
        self.r = s
        self.a = a
        self.c = c
        self.m = m

    def gen_rand(self):
        self.r = (self.a * self.r + self.c) % self.m
        return self.r
        
def undoom_dice(A, B):
    lcg = LCG(s=42)
    o_probs = calc_probs(A)
    n_A = [lcg.gen_rand() % 4 + 1 for i in range(6)]

    n_probs = calc_probs(n_A)

    n_B = []
    for i in range(6):
        max_s = min(6, round(B[i] * n_probs[i] / o_probs[i]))
        max_s = max(1, max_s)
        n_B.append(lcg.gen_rand() % max_s + 1)
    return n_A, n_B

A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 6]
n_A, n_B = undoom_dice(A, B)

print("Original A:", A)
print("Original B:", B)
print("New A:", n_A)
print("New B:", n_B)