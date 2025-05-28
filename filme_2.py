with open('Filmes.txt', 'r') as entrada:
    saida = open('Filmesdel_2.csv', 'w', encoding='utf-8')
    lista = []
    for line in entrada:
        if line [5] == '_' and line[8].isnumeric():
            campos = line.split('|')
            for c in range (1,6):
                lista.append(campos[c].strip())
        elif line [5] == '_' and not line[8].isnumeric():
            camposd = line.split ('|')
            n= int(camposd[0].replace('_', '').strip())
            saida.write(f'{n};{lista[(n-1)*5]};{lista[(n-1)*5+1]};{lista[(n-1)*5+2]};{lista[(n-1)*5+3]};{lista[(n-1)*5+4]};{camposd[1].strip()}\n')