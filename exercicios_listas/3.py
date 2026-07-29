nomes = ['ana', 'CARLOS', 'mArla', 'JOÃO', 'pedro']
nomes_formatados = [n.capitalize() for n in nomes]

print('nomes:', *nomes_formatados)
