import time
import matplotlib.pyplot as plt 
import random
from random import randint
from random import SystemRandom#aumenta aleatoriedade
random = SystemRandom ()
from lmfit.models import LinearModel, StepModel
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize=11, usetex=True)
#fig = plt.figure(figsize=(10,5))
plt.tick_params(direction='in', which='major', top='on', right='on')
plt.tick_params(direction='in', which='minor')

def busca_binaria(vetor, elemento):
	first = 0
	last = len(vetor) - 1
	found = False
	t = time.time()
	while first <= last and not found:
		midpoint = (first + last)//2
		if vetor[midpoint] == elemento:
			found = True

		else:
			if elemento < vetor[midpoint]:
				last = midpoint - 1
				#print(last)
			else:
				first = midpoint + 1
	g = time.time()
	return [found, g - t] #vai retornar se encontrou e o devido tempo




def gerar_vetor(tamanho):#ok
	"""retorna um vetor aleatorio de tamanho informado"""
	tamanho = int(tamanho)
	vec = []
	for i in range(tamanho):
		vec.append(random.choice(range(tamanho)))
	vec.sort()
	return vec


#vec = gerar_vetor(10)
#vec.sort()
#print(vec)

samples = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 
5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000]





#v = gerar_vetor(1000)
#print(v)
#print(busca_binaria(v, 501)[0])

x, y = [], []

for i in range(len(samples)):
	if (busca_binaria(gerar_vetor(samples[i]), 53)[0]) == True:
		x.append(samples[i])
		y.append(busca_binaria(gerar_vetor(samples[i]), 53)[1])#que é o tempo


####procurando a função

step_mod = StepModel(form='erf', prefix='step_')
line_mod = LinearModel(prefix='line_')

pars = line_mod.make_params(intercept=min(y), slope=0)
pars += step_mod.guess(y, x=x, center= 7000)

mod = step_mod + line_mod
out = mod.fit(y, pars, x=x)


plt.plot(x, y, '1', c='blue', label = 'Points')

plt.plot(x, out.init_fit, 'k--', label='initial fit', lw=0.5, alpha =0.5)
plt.plot(x, out.best_fit, 'r-', label='best fit', lw=0.5, alpha =0.5)

plt.xlabel("N")
plt.ylabel("Time(sec)")
plt.grid()
#plt.legend(loc = 'best')
plt.savefig('/home/bruno/Dropbox/BTI/ED1/Projeto1u/bin.pdf',dpi=200)
plt.show()




#print(busca_binaria(vec, 20))