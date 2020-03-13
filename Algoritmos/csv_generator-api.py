# Importação das Bibliotecas
import numpy as np
import pandas as pd
import wave
import struct
import glob
import os
from tqdm import tqdm
import csv
import math

diretorio = ["D:/UFPI/TÓPICOS ESPECIAIS EM INTELIGÊNCIA ARTIFICIAL/database", 
            "D:/UFPI/TÓPICOS ESPECIAIS EM INTELIGÊNCIA ARTIFICIAL/CSV_files"]

# Variaveis
origin_path = str(input("Informe o caminho da pasta que contém as subpastas com os áudios: ")).replace('\\', '/')
csv_path = str(input("Informe o caminho da pasta onde será salvo o arquivo CSV: ")).replace('\\', '/')
print('[ATENÇÃO] O nome da classe será o nome de cada pasta.')
csv_name = str(input("Informe o nome do arquivo CVS: "))
audio_path = glob.glob(origin_path + '/*/*.wav')

# Função de Extrassão de Caracteristicas
def extraction_data_class(audio_path, index):

    opened_audio = wave.open(audio_path, "rb").getparams()

# Pegar nome da pasta para usar como nome da classe
    class_name = replace_audio_path(audio_path)
   
    save_to_csv(index, opened_audio[2], opened_audio[0], (opened_audio[1] * 8), opened_audio[3] / opened_audio[2], class_name)


# Salva os dados na matriz
def save_to_csv(index, framerate, nchannels, bits, duration, class_name):
    with open(csv_path + '/' + csv_name + '.csv', 'a', newline='') as f:
        file = csv.writer(f)
        file.writerow([index, framerate, nchannels, bits, duration, class_name])

def replace_audio_path(audio_path):

    audio_path = audio_path.replace('\\', '/')
    end = audio_path.rfind("/")
    start = audio_path.rfind("/", 1, end - 1)
    class_name = audio_path[start + 1 : end]

    return class_name 

# Escreve o cabeçalho na primeira linha do file .csv e salva ele
with open(csv_path + '/' + csv_name + '.csv', 'w', newline='') as f:
        
        file = csv.writer(f)

        header = ['Sampling_Rate','Channels','Bits','Duration','Class']
        file.writerow(header)

# tqdm mostra a barra de carregamento
# enumerate indexa as linhas no file.csv
for index, audio_path in enumerate(tqdm(audio_path)):
    extraction_data_class(audio_path, index)