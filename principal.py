from decouple import config
import requests
from PIL import Image, ImageFilter
from io import BytesIO
import datas
import os


username = config("USER")
URL = f"https://www.tapmusic.net/collage.php?user={username}&size=5x5&caption=true&type="
CAMINHO = os.path.join(os.getcwd(), 'data')


def pega_imagem(tipo):
    r = requests.get(URL + tipo)
    im = Image.open(BytesIO(r.content))
    return im
   

def salva_imagem(Imagem, diretorio, nome_arquivo):
	if not os.path.exists(diretorio):
		os.makedirs(diretorio)

	Imagem.save(f"{diretorio}\\{nome_arquivo}.jpg")
	print(f"Imagem salva como: {diretorio}\\{nome_arquivo}.jpg")


if(datas.dia_semana_hoje() == 5):
	diretorio = os.path.join(CAMINHO, "SEMANAL", str(datas.ano()), str(datas.mes_hoje()))

	imagem = pega_imagem("7day")
	salva_imagem(imagem, diretorio, datas.dia_hoje())


if(datas.dia_hoje() == 1):

    imagem = pega_imagem("1month")
    if(datas.mes_hoje() == 1):   

        diretorio = os.path.join(CAMINHO, "MENSAL", (str(datas.ano() - 1)))
        salva_imagem(imagem, diretorio, 12)

    else:
        diretorio = os.path.join(CAMINHO, "MENSAL", str(datas.ano()))

        salva_imagem(imagem, diretorio, (datas.mes_hoje() - 1))


if(datas.mes_hoje() == 1 and
	datas.dia_hoje() == 1):
	diretorio = os.path.join(CAMINHO, "ANUAL")

	imagem = pega_imagem("12month")
	salva_imagem(imagem, diretorio, (datas.ano()-1))
