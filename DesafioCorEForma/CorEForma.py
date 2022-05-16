"""
Crie um software em sua linguagem de preferência, que consiga fazer o reconhecimento de cor e forma,
ex: cor verde e quadrado
"""
# importar os pacotes
import numpy  # biblioteca que trabalha numeros
import argparse  # biblioteca que analisa argumentos
import cv2  # biblioteca de visão computacional

"""# Construção das análises e análise propriamente dita de argumentos
ap = argparse.ArgumentParser()  # aqui chamamamos o método de analise de argumentos da biblioteca, setamos a função na variável ap
ap.add_argument("-i", "--image", help="path to thee image")  # adiciona-se o argumento a ser analisado pela variável
args = vars(ap.parse_args())  # a variável args recebe os argumentos de ap
# houve a tentativa de passar direto, porém não funciona, os passos devem ser respeitados pela hierarquia códigos
"""
# carregar imagens
circuloVerde = cv2.imread(".\imgs\circuloverde.png")  # Variável autoexplicativa
quadradoVerde = cv2.imread(".\imgs\quadradoverde.jpg")#Variável autoexplicativa
quadradoVermelho = cv2.imread('.\imgs\quadradovermelho.png')#Variável autoexplicativa



#Definição da lista de limites das cores
boundaries = [([25, 51, 0], [204,255,229])] #limite do verde, definido entre o verde mais escuro e mais claro, utilizando uma palheta de cores

def Cor(image):
    #loop pelos limites
    global booleano
    booleano = False
    for (lower, upper) in boundaries:
        #criar uma lista com as fronteiras utilizando numpy tipificando 8bits para as palhetas, inferior e superior
        lower = numpy.array(lower, dtype = "uint8")
        upper = numpy.array(upper, dtype = "uint8")
        #encontra os limites específicos e aplica a mascara
        if cv2.inRange(image, lower.any(), upper.):
            booleano = True
    return booleano

print(Cor(circuloVerde))
#print(Cor(quadradoVermelho))
#print(Cor(quadradoVerde))
