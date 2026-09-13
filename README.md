# Projeto de Memória Virtual

Este projeto consiste em uma simulação de arquitetura de computadores em Python, focada na implementação e teste de diferentes técnicas de mapeamento entre memória principal (cache) e memória secundária.

---

## Estrutura do projeto

O projeto é composto pelos seguintes módulos escritos em Python:

- **Memoria.py**: Contém as classes `MemoriaPrincipal` e `MemoriaSecundaria`, além de funções utilitárias para geração de hash, exibição do estado das memórias (`dumpMemorias`) e o motor de testes automatizados (`testaMapeamento`).

- **MapeamentoDireto.py**: Implementa a técnica de mapeamento direto.

- **MapeamentoAssociativo.py**: Implementa a técnica de mapeamento totalmente associativo.

- **MapeamentoAssociativoPorConjunto.py**: Implementa a técnica de mapeamento associativo por conjunto.

- **MapeamentoCustomizado.py**: Contém uma implementação personalizada de mapeamento.

---

## Técnicas de mapeamento implementadas

1. **Mapeamento Direto**: Cada bloco da memória secundária é mapeado para um local específico e fixo na memória principal com base no resto da divisão do número da página.

2. **Mapeamento Associativo**: Um bloco da memória secundária pode ser colocado em qualquer linha da memória principal, permitindo maior flexibilidade.

3. **Mapeamento Associativo por Conjunto**: Combina características do mapeamento direto e associativo, dividindo a memória em conjuntos onde os blocos podem ser posicionados livremente.

4. **Mapeamento Customizado**: Lógica personalizada para gerenciamento de páginas entre os níveis de memória.
