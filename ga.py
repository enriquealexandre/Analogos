from numpy.random import randint
from numpy.random import rand
 
# Función objetivo. Una chorrada
def onemax(x):
	return -sum(x)
 
# Selección por torneo
def selection(pop, scores, k=3):
	# Primero selecciono un individuo al azar
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		# Ahora hago el torneo, y compruebo si el nuevo es mejor
		if scores[ix] < scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]
 
# Función de crossover
def crossover(p1, p2, r_cross):
	# En principio los hijos son copias de los padres
	c1, c2 = p1.copy(), p2.copy()
	# Ahora recombino
	if rand() < r_cross:
		# Selecciono el punto de cruce
		pt = randint(1, len(p1)-2)
		# Cruzo los dos individuos
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]
 
# Operador de mutación
def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		# Veo si muta
		if rand() < r_mut:
			# Cambio un bit
			bitstring[i] = 1 - bitstring[i]
 
# Algoritmo genético
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
	# Creo una población inicial aleatoria
	pop = [randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
	# Mejor solución hasta el momento
	best, best_eval = 0, objective(pop[0])
	# Ahora itero para cada generación
	for gen in range(n_iter):
		# Evaluación de los individuos
		scores = [objective(c) for c in pop]
		# Actualizo la mejor solución
		for i in range(n_pop):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				print(">%d, new best f(%s) = %.3f" % (gen,  pop[i], scores[i]))
		# Selección
		selected = [selection(pop, scores) for _ in range(n_pop)]
		# Creamos los nuevos individuos
		children = list()
		for i in range(0, n_pop, 2):
			# Agrupamos los padres
			p1, p2 = selected[i], selected[i+1]
			# crossover y mutación
			for c in crossover(p1, p2, r_cross):
				# Mutación
				mutation(c, r_mut)
				# Lo guardo para la próxima generación
				children.append(c)
		# Reemplazo la población
		pop = children
	return [best, best_eval]
 
# Número de iteraciones
n_iter = 100
# Tamaño de cada individuo
n_bits = 20
# Tamaño de la población
n_pop = 100
# Porcentaje de crossover
r_cross = 0.9
# Probabilidad de mutación
r_mut = 1.0 / float(n_bits)
# Ejecutamos el algoritmo
best, score = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut)
print('¡Hecho!')
print('f(%s) = %f' % (best, score))