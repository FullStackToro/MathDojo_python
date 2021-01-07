class MathDojo:
    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result += a
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for a in nums:
            self.result -= a
        return self

# crear una instruccion:
md = MathDojo()
md2 = MathDojo()
md3 = MathDojo()
# para probar:
x3 = md3.add(2).add(2, 5, 1).add(3, 2).result #15
x2 = md2.add(30).subtract(2, 5, 1).subtract(3, 2).subtract(4).result #13
x1 = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x1,x2,x3)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!
