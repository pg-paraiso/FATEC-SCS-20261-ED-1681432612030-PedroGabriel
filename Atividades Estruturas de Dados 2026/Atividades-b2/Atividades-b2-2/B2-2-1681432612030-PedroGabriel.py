fila_adm = []
fila_aluno = []

def adicionar_documento():
    nome = input("Nome do arquivo: ")
    paginas = int(input("Quantidade de páginas: "))
    tipo = input("Tipo (1 para ADM / 2 para Aluno): ")
    
    documento = [nome, paginas]
    
    if tipo == "1":
        fila_adm.append(documento)
        print("Arquivo enviado para a fila prioritária (ADM).")
    else:
        fila_aluno.append(documento)
        print("Arquivo enviado para a fila de alunos.")

def mostrar_estado():
    print("\n--- STATUS DAS FILAS ---")
    print(f"ADM: {len(fila_adm)} documento(s) aguardando.")
    print(f"Alunos: {len(fila_aluno)} documento(s) aguardando.")
    
    print("Fila ADM:", fila_adm)
    print("Fila Aluno:", fila_aluno)

def imprimir_proximo():
    if len(fila_adm) > 0:
        doc = fila_adm.pop(0)
        print(f"Imprimindo documento ADM: {doc[0]}")
    elif len(fila_aluno) > 0:
        doc = fila_aluno.pop(0)
        print(f"Imprimindo documento Aluno: {doc[0]}")
    else:
        print("Não há nada para imprimir no momento.")

menu = True
while menu:
    print("\n--- GERENCIADOR DE IMPRESSÃO ---")
    print("1 - Adicionar Documento")
    print("2 - Consultar Filas")
    print("3 - Processar Impressão (Refresh)")
    print("4 - Sair")
    
    opcao = input("Escolha o que fazer: ")
    
    if opcao == "1":
        adicionar_documento()
    elif opcao == "2":
        mostrar_estado()
    elif opcao == "3":
        imprimir_proximo()
    elif opcao == "4":
        print("Encerrando sistema...")
        menu = False
    else:
        print("Opção inválida, tenta de novo.")
