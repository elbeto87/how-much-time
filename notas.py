birth_day_eze = datetime.date(1987,6,26)
birth_day_sol = datetime.date(1987,5,30)
initial_date_relation = datetime.date(2005,5,30)
today = datetime.date.today()

days_birth_eze = float((today - birth_day_eze).days)
days_birth_sol = float((today - birth_day_sol).days)
days_date_relation = float((today - initial_date_relation).days)

print(days_birth_eze)
print(days_date_relation)


#(days_birth_eze + unk) * 0.33 = (days_date_relation + unk)
#days_birth_eze * 0.33 + unk * 0.33 = days_date_relation + unk
unk_eze = ((days_birth_eze * 0.33) - days_date_relation) / 0.66
unk_sol = ((days_birth_sol * 0.5) - days_date_relation) / 0.5

fecha_final_eze = today + datetime.timedelta(days=unk_eze)
fecha_final_sol = today + datetime.timedelta(days=unk_sol)

print(fecha_final_sol)