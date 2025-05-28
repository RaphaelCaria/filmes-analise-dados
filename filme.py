with open('Filmes.txt', 'r') as entrada:
    saida = open('Filmesdel.csv', 'w', encoding='utf-8')
    rk = []
    filme = []
    nota = []
    ano = []
    genero = []
    for line in entrada:
        if line [5] == '_' and line[8].isnumeric():
            campos = line.split('|')
            rk.append(campos[1].strip())
            filme.append(campos[2].strip())
            ano.append(campos[3].strip())
            nota.append(campos[4].strip().replace(',', '.'))
            genero.append(campos[5].strip())
        elif line [5] == '_' and not line[8].isnumeric():
            camposd = line.split ('|')
            n= int(camposd[0].replace('_', '').strip())
            saida.write(f'{n}; {rk[n-1]}; {filme[n-1]}; {ano[n-1]}; {nota[n-1]};{genero[n-1]}\n')