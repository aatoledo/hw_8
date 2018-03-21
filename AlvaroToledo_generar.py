import numpy as np
import matplotlib.pyplot as plt

M = 10000

#Primera funcion
def sample_1 (N):
	#arreglo a y probabilidades p
	a = [10, -5, 3, 9]
	distri = np.random.choice(a, N, p =[0.1,0.4,0.2,0.3])
	return distri

#Segunda funcion (exponencial)
def  sample_2 (N):
	#distribucion
	beta = 0.5 
	expo = np.random.exponential (beta , N)
	return expo

#Tercera funcion (promedio)
def get_mean(sampling_fun, N, M):
	#Corre las funcions M veces
	valores = 0
	promedio = []
	for i in range (M):
		valores = np.mean(sampling_fun(N))
		promedio.append(valores)
	return promedio


#Ejecutar las funciones
#Variables y constantes
rep = [10,100,1000]
samples = [sample_1, sample_2]
for a in range (len(rep)):
	N = rep[a]
	for b in range (len(samples)):
		nombre = samples[b]
		resultado = get_mean(nombre, N, M)
		np.savetxt ("sample_" + str(b+1) + "_" + str(N) + ".txt", resultado)







		

