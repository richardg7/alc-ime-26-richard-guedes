import numpy as np

def resolve_lu(A, b):
    """
    Resolve o sistema linear Ax = b utilizando a decomposição LU sem pivoteamento.
    Retorna as matrizes L, U e o vetor solução x.
    """
    # Converte as entradas para arrays do numpy (tipo float para evitar truncamento)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = A.shape[0]
    
    # Inicializa L como matriz identidade e U como matriz de zeros
    L = np.eye(n)
    U = np.zeros((n, n))
    
    # 1. Decomposição LU (Sem pivoteamento)
    for k in range(n):
        # Verifica se o pivô é nulo
        if A[k, k] == 0:
            raise Exception("Pivô nulo encontrado durante a decomposição. Sugere-se utilizar uma função alternativa com pivoteamento para a solução deste sistema.")
            
        # Preenche a linha k da matriz U (que recebe os coeficientes atualizados)
        for j in range(k, n):
            U[k, j] = A[k, j]
            #print(U)
            
        # Calcula os multiplicadores e preenche a coluna k da matriz L
        for i in range(k+1, n):
            # O multiplicador 'm' é a razão entre o elemento a zerar e o pivô
            m = A[i, k] / U[k, k]
            # O multiplicador é armazenado na matriz L
            L[i, k] = m
            #print(L)
            
            # Atualiza os elementos restantes da matriz A
            for j in range(k, n):
                A[i, j] = A[i, j] - (m * U[k, j])
                #print(A)
                
    # 2. Substituição Progressiva (Ly = b)
    y = np.zeros(n)
    for i in range(n):
        soma = 0.0
        for j in range(i):
            soma += L[i, j] * y[j]
        y[i] = b[i] - soma
        #print(y)
        
    # 3. Substituição Regressiva (Ux = y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = 0.0
        for j in range(i + 1, n):
            soma += U[i, j] * x[j]
        x[i] = (y[i] - soma) / U[i, i]
        #print(x)
        
    return L, U, x

# Bloco de testes (opcional) para demonstrar que a função funciona
if __name__ == '__main__':
    # Exemplo de sistema:
    # 2x1 + 3x2 = 8
    # 4x1 + 9x2 = 21
    A_teste = [[2, 3],
               [4, 9]]
    b_teste = [8, 21]
    
    L_res, U_res, x_res = resolve_lu(A_teste, b_teste)
    
    print("Matriz L:")
    print(L_res)
    print("\nMatriz U:")
    print(U_res)
    print("\nVetor solução x:")
    print(x_res)
