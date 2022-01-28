# Ines Gomes, 96742

############################
# Projeto 2:               #
# Tecnico Battle Simulator #
############################

###############
# TAD posicao #
###############

# contrutores
def cria_posicao(x, y):
    """
    Esta funcao verifica os argumentos e devolve a posicao composta pelos dois argumentos.
    cria_posicao: natural x natural -> posicao
    """
    if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
        raise ValueError('cria_posicao: argumentos invalidos')
    return x, y


def cria_copia_posicao(p):
    """
    Esta funcao recebe uma posicao e cria uma copia desta.
    cria_copia_posicao: posicao -> posicao
    """
    return cria_posicao(obter_pos_x(p), obter_pos_y(p))


# seletores
def obter_pos_x(p):
    """
    Esta funcao devolve a coordenada x de uma posicao.
    obter_pos_x: posicao -> natural
    """
    return p[0]


def obter_pos_y(p):
    """
    Esta funcao devolve a coordenada y de uma posicao.
    obter_pos_y: posicao -> natural
    """
    return p[1]


# reconhecedor
def eh_posicao(arg):
    """
    Esta funcao verifica se um argumento corresponde a uma posicao valida.
    eh_posicao: universal -> booleano
    """
    if not (isinstance(arg, tuple) and len(arg) == 2 and isinstance(obter_pos_x(arg), int) and
            isinstance(obter_pos_y(arg), int) and obter_pos_x(arg) > 0 and obter_pos_y(arg) > 0):
        return False
    return True


# teste
def posicoes_iguais(p1, p2):
    """
    Esta funcao verifica se duas posicoes sao iguais entre si.
    posicoes_iguais: posicao x posicao -> booleano
    """
    if obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2):
        return True
    return False


# transformador
def posicao_para_str(p):
    """
    Esta funcao transforma uma posicao numa cadeia de carateres que a representa.
    posicao_para_str: posicao -> str
    """
    return str((obter_pos_x(p), obter_pos_y(p)))


# funcoes de alto nivel
def obter_posicoes_adjacentes(p):
    """
    Esta funcao devolve um tuplo que contem as posicoes adjacentes a posico dada, de acordo com a ordem de leitura.
    obter_posicoes_adjacentes: posicao -> tuplo
    """
    lista = [(obter_pos_x(p), obter_pos_y(p) - 1), (obter_pos_x(p) - 1, obter_pos_y(p)),
             (obter_pos_x(p) + 1, obter_pos_y(p)), (obter_pos_x(p), obter_pos_y(p) + 1)]
    adjacentes = ()
    for posicao in lista:
        if obter_pos_x(posicao) >= 0:
            if obter_pos_y(posicao) >= 0:
                adjacentes += posicao,
    return adjacentes


###############
# TAD unidade #
###############

# construtor
def cria_unidade(p, v, f, string):
    """
    Esta funcao verifica os argumentos e devolve a unidade composta pelos argumentos dados.
    cria_unidade: posicao x natural x natural x str -> unidade
    """
    if not (isinstance(p, tuple) and eh_posicao(p) and isinstance(v, int) and isinstance(f, int) and
            isinstance(string, str) and v > 0 and f > 0 and string != ''):
        raise ValueError('cria_unidade: argumentos invalidos')
    return tuple((p, v, f, string))


def cria_copia_unidade(u):
    """
    Esta funcao recebe uma unidade e cria uma copia da mesma.
    cria_copia_unidade: unidade -> unidade
    """
    return cria_unidade(obter_posicao(u), obter_vida(u), obter_forca(u), obter_exercito(u))


# seletores
def obter_posicao(u):
    """
    Esta funcao devolve a posicao onde se encontra a unidade.
    obter_posicao: unidade -> posicao
    """
    return u[0]


def obter_exercito(u):
    """
    Esta funcao devolve o exercito a que a unidade pertence.
    obter_exercito: unidade -> str
    """
    return u[3]


def obter_forca(u):
    """
    Esta funcao devolve a forca de ataque que tem a unidade.
    obter_forca: unidade -> natural
    """
    return u[2]


def obter_vida(u):
    """
    Esta funcao devolve os pontos de vida que tem a unidade.
    obter_vida: unidade -> natural
    """
    return u[1]


# modificadores
def muda_posicao(u, p):
    """
    Esta funcao altera a posicao em que a unidade se encontra e devolve a unidade alterada.
    muda_posicao: unidade x posicao -> unidade
    """
    unidade = list(u)
    unidade[0] = p
    return tuple(unidade)


def remove_vida(u, v):
    """
    Esta funcao subtrai o valor dos pontos de vida v a unidade dada e devolve a unidade alterada.
    remove_vida: unidade x natual -> unidade
    """
    unidade = list(u)
    unidade[1] -= v
    return tuple(unidade)


# reconhecedor
def eh_unidade(arg):
    """
    Esta funcao verifica se um argumento corresponde a uma unidade valida.
    eh_unidade: universal -> booleano
    """
    if not (isinstance(arg, tuple) and len(arg) != 4 and obter_vida(arg) >= 0 and obter_forca(arg) >= 0 and
            isinstance(obter_exercito(arg), str) and obter_exercito(arg) != ''):
        return False
    return True

# teste
def unidades_iguais(u1, u2):
    """
    Esta funcao verifica se duas unidades sao iguais entre si.
    unidades_iguais: unidade x unidade -> booleano
    """
    if not (posicoes_iguais(obter_posicao(u1), obter_posicao(u2)) and obter_vida(u1) == obter_vida(u2) and
            obter_forca(u1) == obter_forca(u2) and obter_exercito(u1) == obter_exercito(u2)):
        return False
    return True


# transformadores
def unidade_para_char(u):
    """
    Esta funcao devolve a  primeira letra do exercito a que a unidade pertence em maiuscula.
    unidade_para_char: unidade -> str
    """
    exercito_lista = list(obter_exercito(u))
    return exercito_lista[0].upper()


def unidade_para_str(u):
    """
    Esta funcao devolve uma representacao especifica da unidade.
    unidade_para_str: unidade -> str
    """
    return str(unidade_para_char(u)) + str([obter_vida(u), obter_forca(u)]) + '@' + str(obter_posicao(u))


# funcoes de alto nivel
def unidade_ataca(u1, u2):
    """
    Esta funcao retira o valor dos pontos de vida da segunda unidade correspondentes a forca de ataque
    da primeira unidade.
    Devolve True se u2 for destruida.
    unidade_ataca: unidade x unidade -> booleano
    """
    if obter_vida(remove_vida(u2, obter_forca(u1))) <= 0:
        return True
    return False


def ordenar_unidades(t):
    """
    Esta funcao recebe um tuplo de unidades e devolve um tuplo com as mesmas unidades ordenadas de acordo
    com a ordem de leitura.
    ordenar_unidades: tuplo -> tuplo
    """
    lista, y, x, res, unidades_ordenadas = [], [], [], [], ()
    for unidade in t:
        # lista contendo todas as posicoes
        lista += obter_posicao(unidade),
    for posicao in lista:
        x += obter_pos_x(posicao),
        y += obter_pos_y(posicao),
    for j in range(max(y) + 1):
        for i in range(max(x) + 1):
            if (i, j) in lista:
                res += (i, j),
    for posicao in res:
        for unidade in t:
            if posicao == obter_posicao(unidade):
                unidades_ordenadas += unidade,
    return unidades_ordenadas


############
# TAD mapa #
############

# construtor
def cria_mapa(d, w, e1, e2):
    """
    Esta funcao verifica os argumentos e devolve o mapa composto pelos argumentos dados.
    cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa
    """
    if not (len(d) == 2 and isinstance(d, tuple) and isinstance(d[0], int) and isinstance(d[1], int) and
            d[0] >= 3 and d[1] >= 3 and isinstance(w, tuple) and isinstance(e1, tuple) and
            len(e1) >= 1 and isinstance(e2, tuple) and len(e2) >= 1 and (eh_unidade(u) for u in e1) and
            (eh_unidade(u) for u in e2)):
        raise ValueError('cria_mapa: argumentos invalidos')
    if len(w) > 0:
        for p in w:
            if not (eh_posicao(p) and p[0] != 0 and p[1] != 0):
                raise ValueError('cria_mapa: argumentos invalidos')
    for u in e1:
        if not (obter_pos_x(obter_posicao(u)) < d[0] and obter_pos_y(obter_pos_x(u)) < d[1]):
            raise ValueError('cria_mapa: argumentos invalidos')
    for u in e2:
        if not (obter_pos_x(obter_posicao(u)) < d[0] and obter_pos_y(obter_pos_x(u)) < d[1]):
            raise ValueError('cria_mapa: argumentos invalidos')
    return d, w, e1, e2


def cria_copia_mapa(m):
    """
    Esta funcao recebe um mapa e cria uma copia do mesmo.
    cria_copia_mapa: mapa -> mapa
    """
    return cria_mapa(obter_tamanho(m), m[1], m[2], m[3])


# seletores
def obter_tamanho(m):
    """
    Esta funcao devolve um tuplo correspondente a dimensao Nx e Ny do mapa, respetivamente.
    obter_tamanho: mapa -> tuplo
    """
    return m[0][0], m[0][1]


def obter_nome_exercitos(m):
    """
    Esta funcao devolve um tuplo com duas cadeias de carateres correspondentes aos exercitos.
    obter_nome_exercitos: mapa -> tuplo
    """
    list = obter_exercito(m[2][0]), obter_exercito(m[3][0])
    return tuple(sorted(list))


def obter_unidades_exercito(m, e):
    """
    Esta funcao devolve um tuplo que contem as unidades que pertencem aos exercito dado, ordenadas
    segundo a ordem de leitura.
    obter_unidades_exercito: mapa x str -> tuplo
    """
    if e == m[2][0][3]:
        return ordenar_unidades(m[2])
    if e == m[3][0][3]:
        return ordenar_unidades(m[3])


def obter_todas_unidades(m):
    """
    Esta funcao devolve um tuplo que contem todas as unidades, ordenadas pela ordem de leitura.
    obter_todas_unidades: mapa -> tuplo
    """
    todas_unidades = m[2] + m[3]
    return ordenar_unidades(todas_unidades)


def obter_unidade(m, p):
    """
    Esta funcao devolve a unidade que se encontra na posicao dada.
    obter_unidade: mapa x posicao -> unidade
    """
    for unidade in m[2]:
        if obter_posicao(unidade) == p:
            return unidade
    for unidade in m[3]:
        if obter_posicao(unidade) == p:
            return unidade


# modificadores
def eliminar_unidade(m, u):
    """
    Esta funcao elimina a unidade dada, deixando a sua posicao livre no mapa.
    eliminar_unidade: mapa x unidade -> mapa
    """
    m, m[2], m[3] = list(m), list(m[2]), list(m[3])
    for unidade in m[2]:
        if unidade == u:
            m[2].remove(u)
    m[2] = tuple(m[2])
    for unidade in m[3]:
        if unidade == u:
            m[3].remove(u)
    m[3] = tuple(m[3])
    return tuple(m)


def mover_unidade(m, u, p):
    """
    Esta funcao altera a posicao da unidade dada para a posicao dada, deixando a posicao onde se encontrava livre.
    mover_unidade: mapa x unidade x posicao -> mapa
    """
    m, m[2], m[3] = list(m), list(m[2]), list(m[3])
    nova_unidade = muda_posicao(cria_copia_unidade(u), p)
    for i in range(2, 4):
        for j in range(len(m[i])):
            if m[i][j] == u:
                m[i][j] = nova_unidade
    m[2], m[3] = tuple(m[2]), tuple(m[3])
    return tuple(m)


# reconhecedores
def eh_posicao_unidade(m, p):
    """
    Esta funcao avalia se a posicao dada esta ocupada por uma unidade.
    eh_posicao_unidade: mapa x posicao -> booleano
    """
    if obter_unidade(m, p):
        return True
    return False


def eh_posicao_corredor(m, p):
    """
    Esta funcao avalia se a posicao dada corresponde a um corredor.
    eh_posicao_corredor: mapa x posicao -> booleano
    """
    return not eh_posicao_parede(m, p)


def eh_posicao_parede(m, p):
    """
    Esta funcao avalia se a posicao dada corresponde a uma parede.
    eh_posicao_parede: mapa x posicao -> booleano
    """
    return p[0] == 0 or p[1] == 0 or p[0] == m[0][0] - 1 or p[1] == m[0][1] - 1 or p in m[1]


# teste
def mapas_iguais(m1, m2):
    """
    Esta funcao avalia se dois mapas sao iguais.
    mapas_iguais: mapa x mapa -> booleano
    """
    if not (len(m1[0]) == len(m2[0]) and len(m1[1]) == len(m2[1]) and len(m1[2]) == len(m2[2]) and
            len(m1[3]) == len(m2[3]) and obter_tamanho(m1) == obter_tamanho(m2) and m1[1] == m2[1] and
            m1[2] == m2[2] and m1[3] == m2[3]):
        return False
    return True

# transformador
def mapa_para_str(m):
    """
    Esta funcao devolve a cadeia de carateres que representa o mapa.
    mapa_para_str: mapa -> str
    """
    Nx, Ny = obter_tamanho(m)[0], obter_tamanho(m)[1]
    w, e1, e2 = m[1], m[2], m[3]
    mapa = ''
    for y in range(Ny):
        if y == 0 or y == Ny - 1:
            for x in range(Nx):
                mapa += '#'
            mapa += '\n'
        else:
            for x in range(Nx):
                if x == 0 or x == Nx - 1:
                    mapa += '#'
                else:
                    if len(w) > 0:
                        if (x, y) in w or (x, y) == w:
                            mapa += '#'
                        else:
                            lista_posicoes = [obter_posicao(u1) for u1 in e1] + [obter_posicao(u2) for u2 in e2]
                            if (x, y) in lista_posicoes:
                                for unidade in e1:
                                    if (x, y) == obter_posicao(unidade):
                                        mapa += unidade_para_char(unidade)
                                for unidade in e2:
                                    if (x, y) == obter_posicao(unidade):
                                        mapa += unidade_para_char(unidade)
                            else:
                                mapa += '.'
            mapa += '\n'
    return mapa[:-1]


# funcoes de alto nivel
def obter_inimigos_adjacentes(m, u):
    """
    Esta funcao devolve um tuplo com as unidades inimigas adjacentes a unidade dada de acordo com a ordem de leitura.
    obter_inimigos_adjacentes: mapa x unidade -> tuplo
    """
    pos_adjacentes = obter_posicoes_adjacentes(obter_posicao(u))
    res, ordenadas = (), ()
    #se a unidade esta no e1
    if obter_exercito(u) == (obter_exercito(m[2][0])):
        for unidade in m[3]:
            if obter_posicao(unidade) in pos_adjacentes:
                res += unidade,
    else:
        for unidade in m[2]:
            if obter_posicao(unidade) in pos_adjacentes:
                res += unidade,
    if res != ():
        ordenadas = ordenar_unidades(res)
    return ordenadas


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


######################
# Funcoes Adicionais #
######################

def calcula_pontos(m, str):
    '''
    Esta funcao devolve a pontuacao do exercito ao qual a string dada corresponde.
    calcula_pontos: mapa x str -> int
    '''
    pontuacao = 0
    for unidade in m[2]:
        if obter_exercito(unidade) == str:
            for unidade in m[2]:
                pontuacao += obter_vida(unidade)
        break
    for unidade in m[3]:
        if obter_exercito(unidade) == str:
            for unidade in m[3]:
                pontuacao += obter_vida(unidade)
        break
    return pontuacao


def simula_turno(m):
    '''
    Esta funcao modifica o mapa dado e devolve um mapa apos um turno de batalha completo.
    simula_turno: mapa -> mapa
    '''
    for u in obter_todas_unidades(m):
        m, m[2], m[3] = list(m), list(m[2]), list(m[3])
        u = obter_unidade(m, obter_posicao(u))
        if u is not None:
            inimigos_adjacentes = obter_inimigos_adjacentes(m, u)
            #se tem adjacente
            if inimigos_adjacentes != ():
                #se a adjacente der para destruir
                for i in range(2, 4):
                    for j in range(len(m[i])):
                        if m[i][j] == obter_unidade(m, inimigos_adjacentes[0]):
                            m[i][j] = remove_vida(obter_unidade(m, inimigos_adjacentes[0]), obter_forca(u))
                            if obter_vida(m[i][j]) <= 0:
                                m = eliminar_unidade(m, m[i][j])
                                break

            #se nao tem adjacente
            else:
                p = obter_movimento(m, u)
                m = mover_unidade(m, u, obter_movimento(m, u))
                u_movida = obter_unidade(m, p)
                inimigos_adjacentes = obter_inimigos_adjacentes(m, u_movida)
                m, m[2], m[3] = list(m), list(m[2]), list(m[3])
                #se tem adjacente (depois de se mover)
                if inimigos_adjacentes != ():
                    # se a adjacente der para destruir
                    for i in range(2, 4):
                        for j in range(len(m[i])):
                            if m[i][j] == obter_unidade(m, inimigos_adjacentes[0]):
                                m[i][j] = remove_vida(obter_unidade(m, inimigos_adjacentes[0]), obter_forca(u_movida))
                                if obter_vida(m[i][j]) <= 0:
                                    m = eliminar_unidade(m, m[i][j])
                                    break
    m = list(m)
    m[2], m[3] = tuple(m[2]), tuple(m[3])
    return tuple(m)


def simula_batalha(string, bool):
    with open(string, "r") as file:
        line_lista = []
        file.seek(0)
        for line in file.readlines():
            line_lista += eval(line),
        # obter e1
        info_unidades_e1 = []
        for arg in line_lista[1]:
            info_unidades_e1 += arg,
        e1 = ()
        for pos in line_lista[4]:
            u = (pos, info_unidades_e1[1], info_unidades_e1[2], info_unidades_e1[0])
            e1 += u,
        # obter e2
        info_unidades_e2 = []
        for arg in line_lista[2]:
            info_unidades_e2 += arg,
        e2 = ()
        for pos in line_lista[5]:
            u = (pos, info_unidades_e2[1], info_unidades_e2[2], info_unidades_e2[0])
            e2 += u,
    m = (line_lista[0], line_lista[3], e1, e2)

    # quando bool = True
    nome_e1 = obter_nome_exercitos(m)[0]
    nome_e2 = obter_nome_exercitos(m)[1]
    if bool:
        print(mapa_para_str(m))
        print('[ ' + nome_e1 + ':' + str(calcula_pontos(m, nome_e1)) + ' ' +
              nome_e2 + ':' + str(calcula_pontos(m, nome_e2)) + ' ]')
        while calcula_pontos(m, nome_e1) > 0 or calcula_pontos(m, nome_e2) > 0:
            if calcula_pontos(m, nome_e1) == 0 or calcula_pontos(m, nome_e2) == 0:
                break
            if mapas_iguais(m, simula_turno(m)):
                return "EMPATE"
            print(mapa_para_str(simula_turno(m)))
            m = simula_turno(m)
            print('[ ' + nome_e1 + ':' + str(calcula_pontos(m, nome_e1)) + ' ' +
                  nome_e2 + ':' + str(calcula_pontos(m, nome_e2)) + ' ]')

    #quando bool = False
    if not bool:
        print(mapa_para_str(m))
        print('[ ' + nome_e1 + ':' + str(calcula_pontos(m, nome_e1)) + ' ' +
              nome_e2 + ':' + str(calcula_pontos(m, nome_e2)) + ' ]')
        while calcula_pontos(m, nome_e1) > 0 or calcula_pontos(m, nome_e2) > 0:
            if calcula_pontos(m, nome_e1) == 0 or calcula_pontos(m, nome_e2) == 0:
                break
            if mapas_iguais(m, simula_turno(m)):
                return "EMPATE"
            m = simula_turno(m)
        print(mapa_para_str(m))
        print('[ ' + nome_e1 + ':' + str(calcula_pontos(m, nome_e1)) + ' ' +
              nome_e2 + ':' + str(calcula_pontos(m, nome_e2)) + ' ]')

    #exercito vencedor
    if calcula_pontos(m, nome_e1) > calcula_pontos(m, nome_e2):
        return nome_e1
    if calcula_pontos(m, nome_e1) < calcula_pontos(m, nome_e2):
        return nome_e2

f = open("gomes.txt", "w+")
f.write("(10, 10)\n('FAP', 5, 15)\n('AMCT', 7, 12)\n((3, 2), (7, 5), (8, 3), (3, 8))\n((1, 1), (2, 1), (4, 1), (4, 2), (4, 3), (9, 3), (9, 4))\n((1, 4), (1, 5), (2, 5), (4, 8), (3, 8), (5, 7))")
f.close()
#print(simula_batalha("gomes.txt", True))
m = ((5, 5), (1, 1), (((1, 2), 30, 30, 'FAP'), ((1, 3), 30, 30, 'FAP')), (((3, 2), 11, 11, 'AMCT'), ((2, 3), 11, 11, 'AMCT')))
m1 = simula_turno(m)
print(mapa_para_str(m))
print(mapa_para_str(simula_turno(m1)))
