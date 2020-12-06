#!/usr/bin/env python
# -*- coding: utf-8 -*-


from decouple import config
import requests
from PIL import Image, ImageFilter
from io import BytesIO
import datas
import os


username = config("USER")
URL = "https://www.tapmusic.net/collage.php?user={}&size=5x5&caption=true&type=".format(username)
CAMINHO = "C:\\" + os.path.join('Users', 'Jhonata','Desktop', "Projeto Jornada Musical", "data") + "\\"
	


def pega_imagem(tipo):
    r = requests.get(URL + tipo)
    im = Image.open(BytesIO(r.content))
    return im
   

def salva_imagem(Imagem, pasta, endereco):
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    Imagem.save(pasta + endereco + ".jpg")


print("RODANDO...")

if(datas.dia_semana_hoje() == 5):
	pasta = CAMINHO + "SEMANAL\\"  + str(datas.ano()) + "\\" + str(datas.mes_hoje()) + "\\"
	
	imagem = pega_imagem("7day")
	salva_imagem(imagem, pasta, str(datas.dia_hoje()))


if(datas.dia_hoje() == 1):
	pasta = CAMINHO  + "MENSAL\\"  + str(datas.ano()) + "\\"
		
	imagem = pega_imagem("1month")
	salva_imagem(imagem, pasta, str(datas.mes_hoje() - 1))


if(datas.mes_hoje() == 1 and
	datas.dia_hoje() == 1):
	pasta = CAMINHO + "ANUAL\\" 

	imagem = pega_imagem("12month")
	salva_imagem(imagem, pasta, str(datas.ano()-1))


print("FINALIZADO")