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
# Altere a funcao para fazer uso da tecnica de mapeamento associativo

#paginas = [[-1, "0100"], [-1, "1101"], [-1, "1100"], [-1, "1001"], [-1, "0101"], [-1, "0001"], [-1, "0000"], [-1, "1111"]]
paginas = [-1] * 8


def mapeamentoAssociativo(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global paginas

    variavelI = random.randint(0,7)

    paginaRequisitada = endereco >> 2
    byteRequisitado = endereco & 3

    print('PÁGINA REQUISITADA: ', paginaRequisitada)
    print('BYTE REQUISITADO: ', byteRequisitado)
    print('TABELA DE MAPEAMENTO: ', paginas)
    print('NÚMERO ALEATÓRIO: ', variavelI)

    if not paginaRequisitada in paginas:
        pagina = memoriaSecundaria.getPagina(paginaRequisitada)
        paginas[variavelI] = paginaRequisitada
        memoriaPrincipal.setPagina(pagina, variavelI)

    #if paginaRequisitada in paginas:
    else:
        print("A página requisitada já foi atribuída à memória principal")
        for i in range(len(paginas)):
            # percorre a lista até encontrar o endereço da página requisitada
            if paginas[i] == paginaRequisitada:
                print("PÁGINA ARMAZENADA NO ENDEREÇO: ", i)
                return i

    #retorna endereco
    return variavelI

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
                               funcaoMapeamento=mapeamentoAssociativo,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1028, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoAssociativo, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

