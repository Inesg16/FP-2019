# 96742 Ines Gomes


def eh_labirinto(maze):
    '''eh_labirinto: universal -> booleano
    Esta funcao avalia se o argumento correponde a um labirinto.

    Argumento: maze

    Retorna True se o argumento e valido
    ou retorna False se:
    - o argumento (maze) nao for tuplo
    - e (elemento de maze) nao for tuplo
    - o primeiro e ultimo elemento de e nao correspondem a paredes (1s)
    - os elementos e nao forem 0s ou 1s
    - os elementos de e nao forem inteiros
    - o primeiro e ultimo elemento de maze nao corresponderem a paredes (nao forem formados por 1s)
    - o labirinto for menor que um 3x3, ou seja, se o numero de elementos de maze for menor que 3 ou o numero de elementos de e for menor que 3.
    '''
    if type(maze) != tuple:                                 #se maze nao foi tuplo
        return False
    for e in maze:
        if type(e) != tuple or e[0] != 1 or e[-1] != 1:     # Se e nao e tuplo e Se posicoes externas correspondem a paredes (nas posições interiores)
            return False
        if len(e) != len(maze[0]):                          # Se os elementos de maze nao tiverem todos o mesmo numero de elementos
            return False
        for i in e:
            if i != 1 and i != 0 and type(i) != int:        # Se um elemento de maze nao for formado por 0 ou 1 ou nao for inteiro
                return False
    for e in range(-1, 1):                                  # Se as posicoes externas nao corresponderem a paredes (posicoes exteriores)
        for i in maze[e]:
            if i != 1:
                return False
    if len(maze) <= 3 or len(maze[0]) <= 3:                 # Se o numero de elementos de maze for menor ou igual a 3 e o numero de elementos de cada elemento for menor ou igual a 3, o labirinto e mais pequeno ou igual a um 3x3
        return False
    else:
        return True


def eh_posicao(position):
    '''eh_posicao: universal -> booleano
    Esta funcao avalia se o argumento corresponde a uma posicao.

    Argumento: posicao

    Retorna True se o argumento e valido
    ou retorna False se:
    - posicao nao for um tuplo
    - posicao nao for composta por dois valores, um x e um y
    - e (elementos de posicao) nao forem inteiros
    - e forem negativos.
    '''
    if type(position) != tuple:                             # se nao for um tuplo
        return False
    if len(position) != 2:                                  # se nao forem dois valores
        return False
    for e in position:
        if type(e) != int:                                  # se valores nao forem int
            return False
        if e < 0:                                           # se valores negativos
            return False
    else:
        return True


def eh_conj_posicoes(conjunto):
    ''' eh_conj_posicoes: universal -> booleano
    Esta funcao avalia se o argumento corresponde a um conjunto de posicoes

    Argumento: conjunto

    Retorna True se o argumento e valido
    Retorna False se:
    - o conjunto nao for tuplo
    - o conjunto for formado por mais que 2 posicoes
    - a funcao eh_posicao retornar False, ou seja, se algum elemento do conjunto nao corresponder a uma posicao).
    '''
    if type(conjunto) != tuple:   # se nao for tuplo
        return False
    if len(conjunto) > 2:         # se tiver mais de 2 posicoes
        return False
    for e in conjunto:
        if not eh_posicao(e):     # se a funcao eh_posicao(conjunto) for falsa(se o argumento corresponde a uma posicao)
            return False
    else:
        return True


def tamanho_labirinto(maze):
    '''tamanho_labirinto: labirinto -> tuplo
    Esta funcao avalia se o argumento corresponde a um labirinto e devolve o tamanho do labirinto.

    Argumento: maze

    Retorna um tuplo correspondente ao tamanho de maze
    ou retorna o erro 'tamanho_labirinto: argumento invalido' se eh_labirinto retornar False, ou seja, se o argumento nao corresponder a um labirinto valido.
    '''
    if not eh_labirinto(maze):                                       # se eh_labirinto for falso (avalia o labirinto)
        raise ValueError("tamanho_labirinto: argumento invalido")
    x = len(maze)
    y = len(maze[0])
    t = (x, y)
    return t


def eh_mapa_valido(maze, conjunto):
    '''eh_mapa_valido: labirinto x conj_posicoes -> booleano
    Esta funcao avalia a validade dos argumentos e se o segundo argumento corresponde a um conjunto de posicoes compativeis no labirinto

    Argumentos: maze e conjunto

    Retorna True se os argumentos forem validos
    ou retorna False se alguma das posicoes do conjunto corresponderem a uma parede
    ou retorna o erro 'eh_mapa_valido: algum dos argumentos e invalido' se:
     - eh_labirinto retornar False (logo o argumento maze nao corresponde a um labirinto valido)
     - eh_conj_posicoes retornar False (logo o argumento conjunto nao corresponde a um conjunto de posicoes valido).
    '''
    if not (eh_labirinto(maze) and eh_conj_posicoes(conjunto)):
        raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")
    for p in conjunto:
        x = p[0]
        y = p[1]
        if x > len(maze) or y > len(maze[0]) or maze[x][y] == 1:                  # se no ponto (x,y) ha parede
            return False
    else:
        return True


def eh_posicao_livre(maze, conjunto, position):
    ''' eh_posicao_livre: labirinto x conj_posicoes x posicao -> booleano
    Esta funcao avalia a validades dos argumentos e se a posicao e livre, ou seja, se nao esta ocupada por paredes ou por unidades.

    Argumentos: maze, conjunto e posicao

    Retorna True se a posicao corresponder a uma posicao livre
    ou retorna False se:
    - eh_mapa_valido retornar False (logo a posicao encontra se numa parede do labirinto)
    - a posicao for ocupada por outras unidades
    ou retorna o erro 'eh_posicao_livre: algum dos argumentos e invalido' se:
    - eh_labirinto retornar False (logo o argumento maze nao corresponde a um labirinto valido)
    - eh_conj_posicoes retornar False (logo o argumento conjunto nao corresponde a um conjunto de posicoes valido)
    - eh_posicao retornar False (logo o argumento posicao nao corresponde a uma posicao valida).
    '''
    if not (eh_labirinto(maze) and eh_conj_posicoes(conjunto) and eh_posicao(position)):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
    if not eh_mapa_valido(maze, (position,)):              # se a posicao nao for ocupada por parede
        return False
    if position in conjunto:                               # se a posicao for ocupada por unidades
        return False
    else:
        return True


def posicoes_adjacentes(position):
    ''' posicoes_adjacentes: posicao -> conj_posicoes
    Esta funcao recebe uma posicao e devolve o conjunto de posicoes adjacentes a posicao dada, pela ordem de leitura de um labirinto.

    Argumento: posicao

    Retorna um tuplo que contem o conjunto de posicoes adjacentes
    ou retorna o erro 'posicoes_adjacentes: argumento invalido' se
    - eh_posicao retornar False (logo o argumento nao corresponde a uma posicao valida).
    '''
    if not eh_posicao(position):
        raise ValueError("posicoes_adjacentes: argumento invalido")
    x = position[0]
    y = position[1]
    lista = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    for tuplo in range(3, -1, -1):
        for i in lista[tuplo]:                                  # para cada elemento do tuplo da lista:
            if i < 0:                                           # se o elemento for negativo:
                del lista[tuplo]                                # apaga da lista o tuplo que contem o elemento
                break
    return tuple(lista)


def mapa_str(maze, unidades):
    ''' mapa_str: labirinto x conj_posicoes -> cad. carateres
    Esta funcao devolve uma cadeia de carateres que representa graficamente o labirinto e as unidades.

    Argumentos: maze e conjunto de posicoes (unidades)

    Retorna a cadeia de carateres correspondente a representacao grafica de maze e das unidades no labirinto
    ou retorna o erro 'mapa_str: algum dos argumentos e invalido' se:
    - eh_labirinto retornar False (logo o argumento maze nao corresponde a um labirinto valido)
    - a posicao se encontra numa parede do labirinto.
    '''
    if not (eh_labirinto(maze)):
        raise ValueError("mapa_str: algum dos argumentos e invalido")
    mapa = ""
    lista = []
    for e in maze:
        tuplos_lista = list(e)
        lista += [tuplos_lista]             # lista do maze em que os elementos sao tambem listas
    for e in unidades:                      # Conversao das unidades em posicao da lista do maze
        x = e[0]
        y = e[1]
        if maze[x][y] == 1:                 # se em (x, y) há parede
            raise ValueError("mapa_str: algum dos argumentos e invalido")
        lista[x][y] = 2                     # a lista e alterada nas posicoes em que ha unidades e passa a ser igual a 2
    for i in range(len(lista[0])):
        for e in range(len(lista)):
            if lista[e][i] == 1:
                mapa += '#'
            if lista[e][i] == 0:
                mapa += '.'
            if lista[e][i] == 2:
                mapa += 'O'
        mapa += '\n'
    return mapa


def obter_objetivos(maze, unidades, position):
    '''obter_objetivos: labirinto x conj_posicoes x posicao -> conj_posicoes
    Esta funcao devolve o conjunto de posicoes objetivo, adjacentes a uma das unidades recebidas, e avalia a validade dos argumentos.

    Argumentos: maze, conjunto de posicoes (unidades) e posicao

    Retorna um tuplo com o conjunto das posicoes objetivo
    ou retorna o erro 'obter_objetivos: algum dos argumentos e invalido' se:
    - eh_labirinto retornar False (logo o argumento maze nao corresponde a um labirinto valido)
    - eh_conj_posicoes retornar False (logo o argumento conjunto nao corresponde a um conjunto de posicoes valido)
    - eh_posicao retornar False (logo o argumento posicao nao corresponde a uma posicao valida)
    - a posicao nao fizer parte do conjunto das unidades.
    '''
    res = ()
    if not (eh_labirinto(maze) and eh_conj_posicoes(unidades) and eh_posicao(position)):
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    if position not in unidades:
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    unidades_lista = list(unidades)
    for i in unidades_lista:
        if i == position:                                  # remover a posicao inicial do conjunto das unidades
            unidades_lista.remove(i)
    for j in unidades_lista:
        objetivos = posicoes_adjacentes(j)
        for e in objetivos:
            if e == position:                             # se o elemento foi a posicao inicial, nao se adiciona esta posicao ao res
                res = ()
            if not eh_posicao_livre(maze, unidades, e):   # se a posicao nao for livre este elemento nao entra no res
                res += ()
            else:
                res += (e,)                               # se for livre adiciona ao resultado(tuplo final)
    return res


def obter_caminho(maze, unidades, position):
    '''obter_caminho: labirinto x conj_posicoes x posicao -> conj_posicoes
    Esta funcao devolve um conjunto de posicoes correspondente ao caminho de numero minimo de passos desde a posicao dada ate a posicao objetivo.

    Argumentos: maze, conjunto de posicoes (unidades) e posicao

    Retorna o conjunto de posicoes que definem o caminho de numero minimo de passos
    ou retorna o erro 'obter_caminho: algum dos argumentos e invalido' se:
    - eh_labirinto retornar False (logo o argumento maze nao corresponde a um labirinto valido)
    - eh_conj_posicoes retornar False (logo o argumento conjunto nao corresponde a um conjunto de posicoes valido)
    - eh_posicao retornar False (logo o argumento posicao nao corresponde a uma posicao valida).
    '''
    if not (eh_labirinto(maze) and eh_conj_posicoes(unidades) and eh_posicao(position)):
        raise ValueError("obter_caminho: algum dos argumentos e invalido")
    try:
        objetivos = obter_objetivos(maze, unidades, position)
    except ValueError:
        raise ValueError("obter_caminho: algum dos argumentos e invalido")
    visitadas = ()
    lista_exploracao = [(position, ())]
    while lista_exploracao:
        posicao_atual = lista_exploracao[0][0]
        caminho_atual = lista_exploracao[0][1]
        lista_exploracao = lista_exploracao[1:]
        if posicao_atual not in visitadas:
            visitadas += posicao_atual
            caminho_atual += (posicao_atual,)
            if posicao_atual in objetivos:
                return caminho_atual
            else:
                for e in posicoes_adjacentes(posicao_atual):
                    if eh_mapa_valido(maze, (position,)):
                        lista_exploracao += [(e, caminho_atual)]


def mover_unidade(maze, unidades, position):
    '''mover_unidade: labirinto x conj_posicoes x posicao -> conj posicoes
    Esta funcao devolve o conjunto de posicoes actualizado correspondente as unidades presentes no labirinto apos a unidade dada ter realizado um unico movimento.

    Argumentos: maze, conjunto de posicoes (unidades) e posicao

    Retorna um conjunto de posicoes depois da unidade se ter movido
    ou retorna o erro 'mover_unidade: algum dos argumentos e invalido' se:
    - eh_labirinto retornar False (logo o argumento maze nao corresponde a um labirinto valido)
    - eh_conj_posicoes retornar False (logo o argumento conjunto nao corresponde a um conjunto de posicoes valido)
    - eh_posicao retornar False (logo o argumento posicao nao corresponde a uma posicao valida)
    - se a posicao nao estiver no conjunto de posicoes dado (unidades).
    '''
    if not (eh_labirinto(maze) and eh_conj_posicoes(unidades) and eh_posicao(position)):
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    if position not in unidades:
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    caminho = obter_caminho(maze, unidades, position)
    lista_unidades = list(unidades)
    for i in range(len(unidades)):
        if unidades[i] == position:
            indice = i
    if len(caminho[1]) < 2:
        return unidades
    lista_unidades[indice] = caminho[1]
    return tuple(lista_unidades)
