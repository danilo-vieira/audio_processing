from pydub import AudioSegment
from pydub.utils import db_to_float
from pydub.silence import split_on_silence
from pydub.playback import play
import time
import sys
import os
from tqdm import tqdm

class AudioLoad():

	def __init__(self,path_audio):

		self.file = path_audio
		self.name = self.get_name_file()
		self.audio_object = AudioSegment.from_wav(self.file)
		self.time_in_seconds = self.audio_object.duration_seconds
		self.time_in_miliseconds = self.time_in_seconds * 1000
		self.number_of_slices = self.get_number_slices() 

	def get_name_file(self):
		
		name = self.file.split("/")[-1]
		name = name.split(".")[0]
		return name

	def get_number_slices(self):

		number_of_slices = self.time_in_miliseconds // 60000

		return int(number_of_slices)



class AudioSplit():

	def __init__(self, path_origin , path_destination , class_name ,time_duration_slice):

		self.folder_with_files = path_origin
		self.folder_destination = path_destination
		self.time_duration = time_duration_slice
		self.class_name = class_name
		self.audios_segments = self.get_files_in_folder()


	def generate_splits(self):

		for x in tqdm(range(len(self.audios_segments))):
			
			start_slice = 0	
			end_slice = self.time_duration
			
			for i in range(self.audios_segments[x].number_of_slices):
				
				audio_slice=self.audios_segments[x].audio_object[start_slice:end_slice]
				
				destination_slice = self.folder_destination+"/"+self.audios_segments[x].name+"__split__{}".format(i)
				audio_slice.export(destination_slice+".wav",format="wav")

				start_slice = end_slice
				end_slice+=self.time_duration

			#print("[Ok] - Finalizado slipt do audio atual")
			#print("+----------------------------------------------------------------+")

		print("[Finalized] Todos os splits da classe {} foram finaliados ".format(self.class_name))
		slices_path = os.listdir(self.folder_destination)
		print("Foram gerados {} novos audios".format(len(slices_path)))

	def get_files_in_folder(self):

		files = os.listdir(self.folder_with_files)
		audios_list = list()

		print("[Start] Iniciando a classe ", self.class_name)
		print("[Wait] Carregando os audios ({})".format(self.folder_with_files))
		
		for i in tqdm(range(len(files))):
			if ".wav" in files[i]:
				local_file = self.folder_with_files+"/"+files[i]
				audio  = AudioLoad(local_file)
				audios_list.append(audio)

		print("[Ok] Todos os audios foram carregados")
		print("+----------------------------------------------------------------+")
		return audios_list


origem = "D:/UFPI/TÓPICOS ESPECIAIS EM INTELIGÊNCIA ARTIFICIAL/database/0"
destino = "D:/UFPI/TÓPICOS ESPECIAIS EM INTELIGÊNCIA ARTIFICIAL/database_with_cuts/0"
classe = "0"

queenBee = AudioSplit(origem, destino, classe, 30000)
queenBee.generate_splits()