'''
*----------------------------------------------------------------------------------*
*                           FATEC São Caetano do Sul                               *
*                                Atividade B2 - 3                                  *
*  Autor: 1681432612030 - Pedro Gabriel                                            *
*  Objetivo: Arvore Binaria                                                        *
*  Data: 12/05/2026                                                                *
*----------------------------------------------------------------------------------*
'''
 
from collections import deque
 
 
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
 
 
class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz
 
    
 
    def _em_ordem(self, raiz=None):
        """Gerador em-ordem (esq → raiz → dir)."""
        pilha, atual = [], raiz if raiz is not None else self.raiz
        while pilha or atual:
            while atual:
                pilha.append(atual)
                atual = atual.esq
            atual = pilha.pop()
            yield atual
            atual = atual.dir
 
    def _altura(self, no):
        """Altura recursiva de um nó (-1 se vazio)."""
        if not no:
            return -1
        return 1 + max(self._altura(no.esq), self._altura(no.dir))
 
    def _buscar(self, valor):
        """Retorna o nó com o valor dado, ou None."""
        atual = self.raiz
        while atual:
            if valor == atual.valor:
                return atual
            atual = atual.esq if valor < atual.valor else atual.dir
        return None
 
    
 
    def analisar_arvore(self):
        anterior = None
        for no in self._em_ordem():
            if anterior and no.valor <= anterior.valor:
                print("A árvore não é uma BST válida.")
                return
            anterior = no
        print("A árvore é uma BST válida.")
 
    def imprimir_nos_internos(self):
        internos = [no.valor for no in self._em_ordem() if no.esq or no.dir]
        print(*internos)
 
    def imprimir_folhas(self):
        folhas = [no.valor for no in self._em_ordem() if not no.esq and not no.dir]
        print(*folhas)
 
    def imprimir_niveis(self):
        if not self.raiz:
            return
        fila = deque([self.raiz])
        while fila:
            for _ in range(len(fila)):
                no = fila.popleft()
                print(no.valor, end=' ')
                if no.esq: fila.append(no.esq)
                if no.dir: fila.append(no.dir)
            print()
 
    def calcular_altura(self, no=None):
        return self._altura(no or self.raiz)
 
    def calcular_profundidade(self, valor):
        atual, profundidade = self.raiz, 0
        while atual:
            if valor == atual.valor:
                return profundidade
            atual = atual.esq if valor < atual.valor else atual.dir
            profundidade += 1
        return -1
 
    def imprimir_ancestrais(self, valor):
        ancestrais, atual = [], self.raiz
        while atual:
            if valor == atual.valor:
                print(*ancestrais)
                return
            ancestrais.append(atual.valor)
            atual = atual.esq if valor < atual.valor else atual.dir
 
    def imprimir_descendentes(self, valor):
        no = self._buscar(valor)
        if not no:
            return
        descendentes = [
            n.valor
            for lado in (no.esq, no.dir)
            for n in self._em_ordem(lado)
        ]
        print(*descendentes)
