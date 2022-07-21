def campos_iguais(origem, destino, lista_de_erros):
    '''Verifica se origem e destino são iguais'''
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais.'

def tem_numeros(valor_campo, nome_campo, lista_de_erros):
    '''Verifica se há campos com números'''
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não pode conter números.'

def valida_data(data_ida, data_volta, lista_de_erros):
    '''Verifica se a data de ida é maior que a data de volta'''
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que data de ida.'

def valida_pesquisa(data_ida, data_pesquisa, lista_de_erros):
    '''Valida se a data de ida é correspondente ao dia em que está pesquisando.'''
    if data_pesquisa > data_ida:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que a data de hoje.'