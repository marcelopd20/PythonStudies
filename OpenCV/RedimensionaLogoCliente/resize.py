import cv2
from urllib.request import urlopen
import numpy as np
#https://surveygizmolibrary.s3.amazonaws.com/library/396824/logoconfrabusiness.jpg

def convert(url):
    req = urlopen(f'{url}')#baixa arquivo da logo pela url
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    src = cv2.imdecode(arr, -1)

    h, w = src.shape[:2]#tira medidas 
    prop = w/h #calcula proporção
    #de acordo com o tamanho redimensiona o logo
    if prop >= (1/3):
        new_height = int(100)
        new_width = int((100*w)/h)
        scaled = cv2.resize(src, (new_height, new_width), interpolation = cv2.INTER_AREA)
    else:
        new_width = int(300)
        new_height = int((300*h)/w)
        scaled = cv2.resize(src, (new_height, new_width), interpolation = cv2.INTER_AREA)
    #adiciona 4 canal para aceitar fundo transparente   
    scaled = cv2.cvtColor(scaled, cv2.COLOR_BGR2BGRA)
    #cria fundo transparente
    img_height, img_width, n_channels = 100, 300, 4
    logo_cliente = np.zeros((img_height, img_width, n_channels), dtype=np.uint8)
    #cola  logo
    x_offset = y_offset = 0
    logo_cliente[y_offset:y_offset+scaled.shape[0], x_offset:x_offset+scaled.shape[1]] = scaled
    #salva arquivo como logo_cliente.png
    
    return cv2.imwrite('logo_cliente.png', logo_cliente)

#convert("https://surveygizmolibrary.s3.amazonaws.com/library/396824/organicos.jpg")