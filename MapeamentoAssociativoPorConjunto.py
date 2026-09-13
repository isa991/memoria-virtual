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

paginas = [-1] * 8

def mapeamentoAssociativoPorConjunto(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global paginas

    paginaRequisitada = endereco >> 2
    byteRequisitado = endereco & 3

    resto = paginaRequisitada % 2

    print('PÁGINA REQUISITADA: ', paginaRequisitada)
    print('BYTE REQUISITADO: ', byteRequisitado)
    print('TABELA DE MAPEAMENTO: ', paginas)
    
    if not paginaRequisitada in paginas:
        pagina = memoriaSecundaria.getPagina(paginaRequisitada)
        paginas[variavelI] = paginaRequisitada
        memoriaPrincipal.setPagina(pagina, resto)
        variavelI = variavelI + 1
    else:
        print("A página requisitada já foi atribuída à memória principal")
        print("PÁGINA ARMAZENADA NO ENDEREÇO: ", resto)

    #retorna endereco
    return 0

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
                               funcaoMapeamento=mapeamentoAssociativoPorConjunto,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1028, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoAssociativoPorConjunto, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)