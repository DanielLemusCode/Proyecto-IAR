class Statistics:
    def __init__(self, lista):
        self._lista = lista

    def sum(self):
        suma1 = sum(self._lista)
        return suma1

    def length(self):
        longitud1 = len(self._lista)
        return longitud1

    def average(self):
        prom1 = sum(self._lista)/len(self._lista)
        return prom1
       
Lista1 = [10, 23, 45, 22, 67, 45]
Lista2 = [1, 2, 3, 4, 5]
Lista3 = [100, 200, 300, 400, 500]

stats1 = Statistics(Lista1)
stats2 = Statistics(Lista2)
stats3 = Statistics(Lista3)

print(stats1.sum())
print(stats2.length())
print(stats3.average())