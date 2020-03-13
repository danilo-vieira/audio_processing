import pandas as pd
import matplotlib.pyplot as plt

csv_path = str(input("Informe o caminho da pasta onde será salvo o arquivo CSV: ")).replace('\\', '/')
csv_name = str(input("Informe o nome do arquivo CVS: "))
metadata_path = pd.read_csv(csv_path + '/' + csv_name + '.csv', index_col = 0)

# Plotagem de gráficos

# Gráfico do Tamanho dos aúdios
plt.hist(metadata_path['Duration'], rwidth=0.9, color='#86bf91')
plt.rcParams['figure.figsize'] = (6,6)
plt.xlabel('Duração')
plt.ylabel('População')
plt.title('Histograma com a duração dos aúdios')
plt.grid(False)
plt.show()

# Gráfico da Frequência dos aúdios
plt.hist(metadata_path['Sampling_Rate'], rwidth=0.9, color='#86bf91')
plt.rcParams['figure.figsize'] = (6,6)
plt.xlabel('Taxa de amostragem')
plt.ylabel('População')
plt.title('Histograma da taxa de amostragem dos áudios')
plt.grid(False)
plt.show()

# Gráfico de Bits dos aúdios

plt.hist(metadata_path['Bits'], rwidth=0.9, color='#86bf91')
plt.rcParams['figure.figsize'] = (6,6)
plt.xlabel('Quantidade de bits')
plt.ylabel('População')
plt.title('Histograma da quantidade de bits dos áudios')
plt.grid(False)
plt.show()

# Gráfico de Canais dos aúdios

plt.hist(metadata_path['Channels'], rwidth=0.9, color='#86bf91')
plt.rcParams['figure.figsize'] = (6,6)
plt.xlabel('Canais')
plt.ylabel('População')
plt.title('Histograma da quantidade de canais por classe')
plt.grid(False)
plt.show()

plt.hist(metadata_path['Class'], rwidth=0.9, color='#86bf91')
plt.rcParams['figure.figsize'] = (6,6)
plt.xlabel('Clases')
plt.ylabel('População')
plt.title('Histograma da quantidade de classes na base')
plt.grid(False)
plt.show()


print(metadata_path['Class'].value_counts().to_frame())