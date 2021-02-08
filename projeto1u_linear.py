import numpy as np
from random import randint
import time
import matplotlib.pyplot as plt
from lmfit.models import LinearModel 
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=11, usetex=True)
fig = plt.figure(figsize=(10,5))
plt.tick_params(direction='in', which='major', top='on', right='on')
plt.tick_params(direction='in', which='minor')
font = {'family' : 'serif','color': 'black','weight': 'bold', 'size': 6, 'style': 'italic'}
#----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------FUNÇÕES----------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def gerar_vetor(tamanho):#ok
	"""retorna um vetor aleatorio de tamanho informado"""
	tamanho = int(tamanho)
	vec = []
	for i in range(tamanho):
		vec.append(randint(0, tamanho))
	return vec


#1ª funcao
def tmaximo(vetor):#busca simples - ok
	"""retorna o valor o tempo para encontrar o valor máximo dentro de um vetor"""
	for i in range(len(vetor)):
		g = time.time()
		if max(vetor) == vetor[i]:
			break
	v = time.time()
	return v - g

#print(gerar_vetor(10))
#print(tmaximo(gerar_vetor(10000)))
samples = [10, 50, 100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 
5500, 6000, 6500, 7000, 7500, 8000]
y = []
for i in range(len(samples)):
	y.append(tmaximo(gerar_vetor(samples[i])))
	print(tmaximo(gerar_vetor(samples[i])))
	print('\n')


mod = LinearModel()
pars = mod.guess(y, x = samples)
out = mod.fit(y, pars, x = samples)

print(out.fit_report())



plt.plot(samples, y, '.', c='red', label = 'Points')
#plt.plot(samples, out.best_fit, 'g-', alpha = 0.3, label='initial fit')
plt.plot(samples, out.best_fit, 'b-', alpha = 0.3, label='best fit')
plt.xlabel("N")
plt.ylabel("Time(sec)")
plt.grid()
plt.legend(loc = 'best')
plt.savefig('/home/bruno/Dropbox/BTI/ED1/Projeto1u/linear.pdf',dpi=200)
plt.show()