from datetime import date


def ano():

	hoje = date.today()
	return hoje.year

def mes_hoje():
	hoje = date.today()
	return hoje.month

def dia_hoje():
	hoje = date.today()
	return hoje.day

def dia_semana_hoje():
	hoje = date.today()
	return hoje.isoweekday()