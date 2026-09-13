import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento


# Parâmetros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal

variavelI = 0
paginas = [-1] * 8

def mapeamentoCustomizado(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global variavelI
    global paginas


    paginaRequisitada = endereco >> 2
    byteRequisitado = endereco & 3


    print('PÁGINA REQUISITADA: ', paginaRequisitada)
    print('BYTE REQUISITADO: ', byteRequisitado)
    print('TABELA DE MAPEAMENTO: ', paginas)

    if not paginaRequisitada in paginas:
        pagina = memoriaSecundaria.getPagina(paginaRequisitada)
        paginas[variavelI] = paginaRequisitada
        memoriaPrincipal.setPagina(pagina, variavelI)
        variavelI = variavelI + 1

    #if paginaRequisitada in paginas:
    else:
        print("A página requisitada já foi atribuída à memória principal")
        for i in range(8):
            # percorre a lista até encontrar o endereço da página requisitada
            if paginas[i] == paginaRequisitada:
                print("PÁGINA ARMAZENADA NO ENDEREÇO: ", i)
                return i

    #retorna endereco
    return variavelI - 1

#esta função só deve ser utilizada caso precise inicializar alguma variavel para o mapeamento
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '__main__':

    #executa funcao de mapeamento com 20 enderecos em modo Debug
    testaMapeamento(nEnderecos=20, 
                               nPaginasMemoriaPrincipal=8, 
                               nPaginasMemoriaSecundaria=16, 
                               debug=True, 
                               funcaoMapeamento=mapeamentoCustomizado,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=300, 
                               nPaginasMemoriaPrincipal=128, 
                               nPaginasMemoriaSecundaria=512, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoCustomizado, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

