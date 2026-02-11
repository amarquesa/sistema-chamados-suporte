chamados = []

def abrir_chamado():
    titulo = input("Título do chamado: ")
    prioridade = input("Prioridade (Baixa/Média/Alta): ")
    
    chamado = {
        "titulo": titulo,
        "prioridade": prioridade,
        "status": "Aberto"
    }
    
    chamados.append(chamado)
    print("\nChamado aberto com sucesso!\n")

def listar_chamados():
    if not chamados:
        print("\nNenhum chamado registrado.\n")
        return

    print("\nLista de Chamados:")
    for i, chamado in enumerate(chamados):
        print(f"{i + 1} - {chamado['titulo']} | Prioridade: {chamado['prioridade']} | Status: {chamado['status']}")
    print()

def atualizar_status():
    listar_chamados()
    try:
        numero = int(input("Digite o número do chamado: ")) - 1
        if 0 <= numero < len(chamados):
            novo_status = input("Novo status (Em andamento/Resolvido): ")
            chamados[numero]["status"] = novo_status
            print("\nStatus atualizado com sucesso!\n")
        else:
            print("Chamado inválido.")
    except:
        print("Entrada inválida.")

def menu():
    while True:
        print("==== SISTEMA DE CHAMADOS ====")
        print("1 - Abrir chamado")
        print("2 - Listar chamados")
        print("3 - Atualizar status")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            abrir_chamado()
        elif opcao == "2":
            listar_chamados()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.\n")

menu()
