# def adunare(a, b):
#     return a + b
#
# def scadere(a, b):
#     return a - b
#
# def inmultire(a, b):
#     return a * b
#
# def impartire(a, b):
#     return a / b
#
# class Angajat:
#     marire = 1.50
#
#     def __init__(self, prenume, nume, salar):
#         self.prenume = prenume
#         self.nume = nume
#         self.salar = salar
#
#     def fullname(self):
#         return f'{self.prenume} {self.nume}'
#
#     def email(self):
#         return f'{self.prenume}.{self.nume}@email.com'
#
#     def raise_salar(self):
#         self.salar = int(self.salar * self.marire)
#
#
# # bogdan = Angajat('bogdan', 'ivan', 50)
# # print(bogdan.prenume)
# # print(bogdan.nume)
# # print(bogdan.salar)
# # print(bogdan.fullname())
# # print(bogdan.email())
# #
# # print(bogdan.salar)
# # bogdan.raise_salar()
# # print(bogdan.salar)


magazie = {
    '1':'ceva',
    '2': 'altceva',
    '3': 'din nou ceva',
    '4': 5453,
    '5': 489080
}

dict = magazie.copy()
print(dict)
dict.pop('3')
print(dict)

new_dict = {}
lista_cu_valori = []
for i in dict:
    lista_cu_valori.append(dict[i])

for i in range(len(dict)):
    new_dict[str(i + 1)] = lista_cu_valori[i]


print(new_dict)