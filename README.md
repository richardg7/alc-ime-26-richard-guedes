# Álgebra Linear Computacional - Pós-grad-2026.6 - PGED-IME

**Autor:** Richard Guedes  
**Avaliação:** P1 - Questão 5  
**Repositório:** [alc-ime-26-richard-guedes](https://github.com/richardg7/alc-ime-26-richard-guedes)

---

## Descrição do Projeto

Este repositório contém a resolução da **Questão 5** da prova P1 da disciplina de **Álgebra Linear Computacional** do curso de Pós-graduação do PGED-IME (2026.6). 

O objetivo principal desta questão é implementar, em Python, um algoritmo capaz de resolver um sistema linear $Ax = b$ através da **Decomposição LU** clássica, sem o uso de bibliotecas de fatoração prontas ou pivoteamento.

O código-fonte se encontra no arquivo `.py` deste diretório e foi construído seguindo estritamente as restrições e orientações acadêmicas propostas.

---

## Requisitos Atendidos

De acordo com o enunciado da prova, a função `resolve_lu(A, b)` contempla os seguintes itens:

1. **Construção Explícita de $L$ e $U$**: 
   - A matriz $L$ (triangular inferior) é inicializada com $1$s na diagonal principal.
   - A matriz $U$ (triangular superior) recebe os valores de $A$ a cada iteração de eliminação.
   - **Sem Pivoteamento**: Se um pivô nulo for detectado durante o processo de eliminação, o código dispara uma `Exception` alertando o usuário.

2. **Substituição Progressiva e Regressiva**: 
   - O algoritmo não utiliza funções como `numpy.linalg.solve`. Após obter $L$ e $U$, o código implementa laços matemáticos para realizar a Substituição Progressiva (para encontrar $y$ em $Ly = b$) e a Substituição Regressiva (para encontrar $x$ em $Ux = y$).

3. **Multiplicadores na Matriz $L$**:
   - Durante a fase de eliminação Gaussiana, o multiplicador `m` de cada linha é calculado e inserido **diretamente em sua respectiva posição na matriz $L$**, comprovando o relacionamento direto entre o método de eliminação e a fatoração LU.

4. **Uso Restrito do Numpy**:
   - A biblioteca `numpy` é utilizada apenas para alocar e formatar as matrizes por meio das funções permitidas: `numpy.array`, `numpy.eye` e `numpy.zeros`. O restante da álgebra foi construído manualmente utilizando loops (`for`).

5. **Explicabilidade Visual (Prints de Debug)**:
   - Foram adicionadas chamadas `print()` dentro dos laços `for`. Essa adição tem propósitos estritamente didáticos para acompanhar as matrizes $L$ e $U$ crescendo elemento a elemento em tempo real no terminal, o que facilita o entendimento das operações de linha exigidas no vídeo de apresentação.

---

## Como Executar

Basta possuir o Python instalado com a biblioteca Numpy. Execute o arquivo da seguinte forma pelo terminal:

```bash
python alc-p1-Q5-richard.py
```


Ao rodar o arquivo, o bloco de execução principal (`__main__`) testará automaticamente um sistema $2x2$ de exemplo, imprimindo passo a passo a decomposição LU e exibindo o vetor solução final.
