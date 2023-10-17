horaInicial = int(input('Informe a hora inicial: '))
minutoIncial = int(input('Informe o minuto incial: '))
horaFinal = int(input('Informe a hora final: '))
minutoFinal = int(input('Informe o minuto final: '))

horarioInicial = horaInicial * 60 + minutoIncial
horarioFinal = horaFinal * 60 + minutoFinal

if horarioInicial < horarioFinal : duracao = horarioFinal - horarioInicial
ese: duracao = 24 * 60 - horarioInicial - horarioFinal

print('Horas: ', duracao//60)
print('Minutos: ', duracao%60)
