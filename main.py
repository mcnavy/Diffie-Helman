from random import randint


class DHKE:
    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.__secret = randint(1, 1000)  # own secret number
        self.openKey = 0  # number will  sent to 2nd person
        self.resKey = 0  # number received from 2nd person
        self.K = 0  # final secret key

    def generate_openkey(self):
        self.openKey = (self.g ** self.__secret) % self.p


    def receive_key(self,rec):
        self.resKey = rec

    def generate_secretkey(self):
        self.K = (self.resKey ** self.__secret) % self.p


def prime():  # generate prime number
    P = []
    for i in range(1, 1000):
        a = 0
        for j in range(1, i + 1):
            b = i % j
            if b == 0:
                a = a + 1
        if a == 2:
            P.append(i)
    t = len(P)
    n = randint(0, t)
    return P[n]


p = prime()  # set non-secret p
print("P = ", p)

g = randint(1, 100)  # set non-secret g
print("G = ",g)
Alice = DHKE(p, g)

Bob = DHKE(p, g)
Alice.generate_openkey()
print("Alice open number = ", Alice.openKey)
Bob.generate_openkey()
print("Bobs open number = ", Bob.openKey)
Alice.receive_key(Bob.openKey)
print("Alice received", Alice.resKey)
Bob.receive_key(Alice.openKey)
print("Bob received", Bob.resKey)
Alice.generate_secretkey()
print("Alice got secret number = ", Alice.K)
Bob.generate_secretkey()
print("Bob got secret number = ",Bob.K)
