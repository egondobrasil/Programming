from datetime import date

weekday = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
d = date(2026, 1, 19)

print('Hoje é '+weekday[d.weekday()])
print('Amanhã é '+weekday[(d.weekday()+1)%7])