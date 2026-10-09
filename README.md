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

---

## Apresentação e Demonstração

### Imagem Explicativa
Abaixo, a representação visual explicativa das matrizes no console:

![Execução e Matrizes](01.png)

### Vídeo da Resolução
Para assistir à explicação detalhada do código e ver as operações em andamento, reproduza o vídeo abaixo:

<video src="./alc-p1-Q5-richard.mp4" controls="controls" muted="muted" style="max-height:640px; min-height: 200px">
  Seu navegador não suporta a tag de vídeo.
</video>

*(Caso o player nativo do GitHub não seja renderizado no seu navegador, você pode baixar ou [assistir ao vídeo clicando aqui](./alc-p1-Q5-richard.mp4))*

---

### Resumo da Explicação (Roteiro do Vídeo)

Para facilitar o acompanhamento, segue a síntese do raciocínio estruturado no vídeo (com duração de ~1m15s):

1. **Abertura (0:00 - 0:10):** 
   Apresentação da função `resolve_lu`, construída importando exclusivamente os construtores básicos do `numpy` (restrição da questão). As matrizes $L$ e $U$ são inicializadas com a identidade e zeros, respectivamente.
2. **Decomposição LU e Multiplicadores (0:11 - 0:35):** 
   No loop de decomposição (linha 18), há a checagem de pivô nulo, disparando uma `Exception` se necessário. Os elementos de $U$ recebem a cópia do estado atual da matriz. 
   **O ponto mais importante** ocorre na linha 29: o multiplicador $m$ é calculado pela divisão do elemento pelo pivô. Assim que $m$ é obtido, ele é **armazenado diretamente na posição correspondente de $L$** (linha 33), demonstrando como a matriz $L$ herda explicitamente os multiplicadores da eliminação de Gauss.
3. **Resolução por Substituição (0:36 - 0:55):** 
   Na segunda etapa, a matriz $L$ construída é utilizada para resolver $Ly = b$ via *Substituição Progressiva* (linha 42). A seguir, a matriz $U$ é empregada para resolver $Ux = y$ via *Substituição Regressiva* (linha 51), percorrendo o sistema de baixo para cima.
4. **Fechamento e Teste (0:56 - 1:15):** 
   A função retorna $L$, $U$ e $x$. Executando o teste ao final do código, comprova-se visualmente a correção do método: a matriz $L$ armazena os multiplicadores abaixo da diagonal principal com 1s na diagonal, $U$ torna-se perfeitamente triangular superior, e o vetor $x$ atinge o resultado matemático exato.
