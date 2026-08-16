# hora de inicio del evento
hora_inicio = 23
minutos_inicio = 58
# duración del evento en minutos
duracion = 642

# total de minutos transcurridos desde las 00:00 de la hora de inicio
total_minutos = minutos_inicio + duracion

# los minutos finales son el resto de dividir entre 60
minutos_final = total_minutos % 60
# las horas "extra" que se suman son la división entera entre 60
horas_extra = total_minutos // 60

# la hora final da la vuelta cada 24 horas
hora_final = (hora_inicio + horas_extra) % 24

print("Hora de inicio:", hora_inicio, ":", minutos_inicio)
print("Duración (min):", duracion)
print("Hora final:", hora_final, ":", minutos_final)
