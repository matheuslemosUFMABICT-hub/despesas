print("-"*30+"PROGRAMA DE GASTOS"+"-"*30)
salarioTotal=valorDespesaTotal = None
alimentacao=transporte=saude=lazer=outros = 0
especificacaoDespesa=especificacao = "Nenhuma informação cadastrada"
valorAlimentacao=valorTransporte=valorSaude=valorLazer=valorOutros = 0.0
mensagemMenuInicial = ("#"*30)+"\nSELECIONE A OPÇÃO DESEJADA:\n1-ADICIONAR SALÁRIO E VALORES\n2-ADICONAR DESPESAS\n3-SALDOS E DESPESAS\n4-ESTATÍSTICAS\n5- RETORNAR AO MENU\n6-SAIR E LIMPAR DADOS\n"+("#"*30)+"\n"

numeroOpcao = int(input("\nOLÁ! SEJA BEM-VINDO!\n\n>SELECIONE A OPÇÃO DESEJADA:\n1-ADICIONAR SALÁRIO E VALORES\n2-ADICONAR DESPESAS\n3-SALDOS E DESPESAS\n4-ESTATÍSTICAS\n"))

while(numeroOpcao>=1 and numeroOpcao<=6):

    match numeroOpcao:
        #Salário
        case 1:
            print("-"*30+"CADASTRO SALARIO"+"-"*30)
            salario = input("\nDIGITE O SALÁRIO RECEBIDO: ")
            especificacao = "SALARIO RECEBIDO------R$"+salario

            salarioTotal = float(salario)

            opcaoSelecionada = int(input("\n>Deseja adicionar outro valor recebido nesse periodo?\n1-SIM\n2- NAO\n"))

            while(opcaoSelecionada!=1 and opcaoSelecionada!=2):
                opcaoSelecionada = int(input("\nOPÇÃO SELECIONADA INVÁLIDA!\nDeseja adicionar outro valor recebido nesse periodo?\n1- SIM\n2- NAO\n"))

            while(opcaoSelecionada==1):
                valorAdicionado = input(">DIGITE O VALOR A MAIS RECEBIDO: ")
                valorEspecificado= input("\n>O VALOR É A RESPEITO DE: ")
                especificacao = especificacao+ "\n"+(valorAdicionado+"------R$"+ valorEspecificado)
                
                salarioTotal= salarioTotal+ float(valorAdicionado)
                opcaoSelecionada = int(input("\n>Deseja adicionar outro valor recebido nesse periodo?\n1-SIM\n2-NAO\n"))

            numeroOpcao = int(input(mensagemMenuInicial))
        #Despesas
        case 2: 
            print("-"*30+"CADASTRO DESPESAS"+"-"*30)
            valorDespesaTotal = input("\n>DIGITE O VALOR DA DESPESA ATUAL:   \n")
            motivoDespesa = input("\n>DIGITE O MOTIVO DA DESPESA:   \n")
            especificacaoDespesa = motivoDespesa+ "----"+ valorDespesaTotal
            tipoDespesa = input(">DIGITE O TIPO DA DESPESA: \nA-ALIMENTAÇÃO\nT-TRANSPORTE\nS-SAÚDE\nL-LAZER\nO-OUTROS")
            valorDespesaTotal= float(valorDespesaTotal)

            while(tipoDespesa!="A" and tipoDespesa!="a" and tipoDespesa!="T" and tipoDespesa!="t"  and tipoDespesa!="S" and tipoDespesa!="s"  and tipoDespesa!="L" and tipoDespesa!="l" and tipoDespesa!="O" and tipoDespesa!="o"):
                tipoDespesa = input("\nOPA! PARECE QUE ESTÁ DIGITANDO O TIPO DE DESPESA ERRADO!\nDIGITE UMA DAS OPÇÕES: A-ALIMENTAÇÃO\nT-TRANSPORTE\nS-SAÚDE\nL-LAZER\nO-OUTROS")
            
            if(tipoDespesa=="A" or tipoDespesa=="a"):
                alimentacao=1
                valorAlimentacao = valorDespesaTotal
            elif(tipoDespesa=="T" or tipoDespesa=="t"):
                transporte =1
                valorTransporte = valorDespesaTotal
            elif(tipoDespesa=="S" or tipoDespesa=="s"):
                saude =1
                valorSaude = valorDespesaTotal
            elif(tipoDespesa=="L" or tipoDespesa=="l"):
                lazer=1
                valorLazer = valorDespesaTotal
            elif(tipoDespesa=="O" or tipoDespesa=="o"):
                outros =1
                valorOutros = valorDespesaTotal
            
            opcaoSelecionada = int(input("\n>Deseja adicionar outra despesa?\n1-SIM\n2-NÃO\n"))

            while(opcaoSelecionada!=1 and opcaoSelecionada!=2):
                opcaoSelecionada = int(input("\nOPCAO SELECIONADA INVÁLIDA!\n>Deseja adicionar outro valor recebido nesse periodo?\n1-SIM\n2-NAO\n"))
            
            while(opcaoSelecionada==1):
                valorDespesaAdicionada = input("\n>Digite o valor da despesa:   \n")
                motivoDespesa = input("\n>Digite o motivo da despesa:      \n")
                especificacaoDespesa = especificacaoDespesa+"\n"+ (motivoDespesa+ "------R$"+ valorDespesaAdicionada)
                valorDespesaAdicionada=float(valorDespesaAdicionada)
                valorDespesaTotal = (valorDespesaTotal+valorDespesaAdicionada)

                tipoDespesa = input("DIGITE O TIPO DA DESPESA:\nA- ALIMENTAÇÃO\nT - TRANSPORTE\nS- SAÚDE\nL- LAZER\nO- OUTROS")
                
                while(tipoDespesa!="A" and tipoDespesa!="a" and tipoDespesa!="T" and tipoDespesa!="t"  and tipoDespesa!="S" and tipoDespesa!="s"  and tipoDespesa!="L" and tipoDespesa!="l"  and tipoDespesa!="O" and tipoDespesa!="o"):
                    tipoDespesa = input("OPA!PARECE QUE ESTÁ DIGITANDO O TIPO DE DESPESA ERRADO!\n DIGITE UMA DAS OPÇÕES: \nA- ALIMENTAÇÃO\nT - TRANSPORTE\n S- SAÚDE\n L- LAZER\n O- OUTROS")
                
                if(tipoDespesa=="A" or tipoDespesa=="a"):
                    alimentacao=alimentacao+1
                    valorAlimentacao = valorAlimentacao+valorDespesaAdicionada
                elif(tipoDespesa=="T" or tipoDespesa=="t"):
                    transporte =transporte+1
                    valorTransporte = valorTransporte+ valorDespesaAdicionada
                elif(tipoDespesa=="S" or tipoDespesa=="s"):
                    saude =saude+1
                    valorSaude = valorSaude+valorDespesaAdicionada
                elif(tipoDespesa=="L" or tipoDespesa=="l"):
                    lazer=lazer+1
                    valorLazer = valorLazer+valorDespesaAdicionada
                elif(tipoDespesa=="O" or tipoDespesa=="o"):
                    outros =outros+1
                    valorOutros = valorOutros+valorDespesaAdicionada

                opcaoSelecionada = int(input("Deseja adicionar outra despesa?\n1-SIM\n2-NAO\n"))

            numeroOpcao = int(input(mensagemMenuInicial))

        #Saldos
        case 3:
            print("-"*30+"SALDOS"+"-"*30)
            if(salarioTotal!=None and valorDespesaTotal!=None):
                opcaoSaldo = int(input("\nDIGITE UMA DAS OPÇÕES:\n1-SALDO CONTA MÊS\n2-SALDO ATUAL\n3-SALDO DESPESAS\n4-VER DESCRIÇÃO DAS DESPESAS e SALDOS DE SALÁRIO\n5-RETORNAR AO MENU INICIAL\n"+"-"*30))
                match opcaoSaldo:
                    case 1: 
                        print("\nO VALOR TOTAL NA CONTA É: R$", salarioTotal,"\n")
                        numeroOpcao = int(input(mensagemMenuInicial))
                    case 2: 
                        print("\nVALORES ADICIONADOS + SALÁRIO:\n", salarioTotal,"\n")
                        print("\nVALORES TOTAL DAS DESPESAS: \n", valorDespesaTotal,"\n")

                        saldoAtual = (salarioTotal-valorDespesaTotal)
                        print("\nSALDO ATUAL: R$", saldoAtual,"\n")
                        numeroOpcao = int(input(mensagemMenuInicial))

                    case 3: 
                        print("\nVALORES TOTAL DAS DESPESAS: ", valorDespesaTotal,"\n")
                        numeroOpcao = int(input(mensagemMenuInicial))
                    
                    case 4:
                        print(especificacaoDespesa)
                        numeroOpcao = int(input(mensagemMenuInicial))
                    
                    case 5:
                        numeroOpcao = int(input(mensagemMenuInicial))

            elif(salarioTotal==None):
                print("\nOPA! PARECE QUE NÃO HÁ UM SALÁRIO CADASTRADO!\nIREMOS DIRECIONAR VOCÊ PARA ADICIONAR VALORES\n"+"-"*30)
                numeroOpcao = 1
            elif(valorDespesaTotal==None):
                print("\nOPA! PARECE QUE NÃO HÁ DESPESAS CADASTRADAS!\nIREMOS DIRECIONAR VOCÊ PARA O CADASTRO DE DESPESAS\n"+"-"*30)
                numeroOpcao = 2
            else:
                numeroOpcao = int(input("\n OPA! PARECE QUE NÃO HÁ SALÁRIO E NEM DESPESAS CADASTRADAS, FAÇA SEU CADASTRO E ADICIONE AS SUAS DESEPESAS: \n1- ADICIONAR SAÁRIO E VALORES\n 2- ADICONAR DESPESAS\n"+"-"*30))
                while(numeroOpcao<1 or numeroOpcao>2):
                    numeroOpcao = int(input("\n OPÇÃO INVÁLIDA!\nPARECE QUE NÃO HÁ SALÁRIO E NEM DESPESAS CADASTRADAS, FAÇA SEU CADASTRO E ADICIONE AS SUAS DESEPESAS: \n1- ADICIONAR SALÁRIO E VALORES\n 2- ADICONAR DESPESAS"))
            
        #Estatísticas
        case 4: 
            print("-"*30+"ESTATÍSTICAS"+"-"*30)
            if(salarioTotal!=None and valorDespesaTotal!=None):
           
                opcaoEstatitica = int(input("\n SELECIONE A OPÇÃO DESEJADA:\n1-MÉDIA DE GASTOS NO MÊS\n2- GASTOS POR CATEGORIA\n3- SITUAÇÃO FINANCEIRA\n4-GRÁFICO\n5-VOLTAR AO MENU INICIAL\n"))
                while(opcaoEstatitica<1 or opcaoEstatitica>5):
                    opcaoEstatitica=int(input("OPÇÃO INVÁLIDA!\n>ESCOLHA UMA DAS OPÇÕES: \n1-MÉDIA DE GASTOS NO MÊS\n2-GASTOS POR CATEGORIA\n3-SITUAÇÃO FINANCEIRA\n4-GRÁFICO\n5-VOLTAR AO MENU INICIAL\n"+"-"*30))
                match opcaoEstatitica:
                    case 1: 
                        mediaGastosMes= valorDespesaTotal/30
                        print("A MÉDIA DE GASTO DIÁRIA É: R$", mediaGastosMes,"/dia\n")
                        numeroOpcao = int(input(mensagemMenuInicial))

                    case 2:
                        print("\nGASTO COM ALIMENTAÇÃO: R$", valorAlimentacao,"\n")
                        print("GASTO COM TRANSPORTE: R$", valorTransporte,"\n")
                        print("GASTO COM SAÚDE: R$",valorSaude,"\n")
                        print("GASTO COM LAZER: R$",valorLazer,"\n")
                        print("GASTO COM OUTROS: R$",valorOutros,"\n")
                        numeroOpcao = int(input(mensagemMenuInicial))

                    case 3: 
                        if(salarioTotal>valorDespesaTotal):
                            diferenca = (salarioTotal-valorDespesaTotal)
                            print("Oba! Parece que sua situação financeira está ok, o saldo restante é de R$:",diferenca)
                            numeroOpcao = int(input(mensagemMenuInicial))
                        else:
                            diferenca = (salarioTotal-valorDespesaTotal)
                            print("Parece que necessita verificar sua saúde financeira, pois as despesas foram maiores que seus ganhos, restando um saldo negativo de: R$",diferenca)
                            numeroOpcao = int(input(mensagemMenuInicial))
                    case 4: 
                        print("-"*30+"GRÁFICOS POR CATEGORIA"+"-"*30)
                        divisaoAlimentacao =round(valorAlimentacao/10)
                        divisaoTransporte = round(valorTransporte/10)
                        divisaoSaude = round(valorSaude/10)
                        divisaoLazer = round(valorLazer/10)
                        divisaoOutros = round(valorOutros/10)

                        n= 100/valorDespesaTotal
                        porceGastoAlimentacao = valorAlimentacao*n
                        porceGastoTransporte = valorTransporte*n
                        porceGastoSaude = valorSaude*n
                        porceGastoLazer = valorLazer*n
                        porceGastoOutros= valorOutros*n

                        print("Alimentação:", end= "")
                        for i in range(0, divisaoAlimentacao):
                            print("█", end="")
                        print(round(porceGastoAlimentacao,2),"%")
                        print("\n"+"-"*30)
                        print("Transporte:", end= "")
                        for i in range(0, divisaoTransporte):
                            print("█", end="")
                        print(round(porceGastoTransporte,2),"%")
                        print("\n"+"-"*30)
                        print("Saúde:", end= "")
                        for i in range(0, divisaoSaude):
                            print("█", end="")
                        print(round(porceGastoSaude,2),"%")
                        print("\n"+"-"*30)
                        print("Lazer:", end= "")
                        for i in range(0, divisaoLazer):
                            print("█", end="")
                        print(round(porceGastoLazer,2),"%")
                        print("\n"+"-"*30)
                        print("Outros:", end= "")
                        for i in range(0, divisaoOutros):
                            print("█", end="")
                        print(round(porceGastoOutros,2),"%")
                        print("\n"+"-"*30)
                        numeroOpcao = int(input(mensagemMenuInicial))

                    case 5:
                        numeroOpcao = 5
            
            elif(salarioTotal==None):
                print("\nOPA! PARECE QUE NÃO HÁ UM SALÁRIO CADASTRADO! IREMOS DIRECIONAR VOCÊ PARA ADICIONAR VALORES\n")
                numeroOpcao = 1
            elif(valorDespesaTotal==None):
                print("\nOPA! PARECE QUE NÃO HÁ DESPESAS CADASTRADAS!IREMOS DIRECIONAR VOCÊ PARA O CADASTRO DE DESPESAS\n")
                numeroOpcao = 2
            else:
                numeroOpcao = int(input("\n OPA! PARECE QUE NÃO HÁ SALÁRIO E NEM DESPESAS CADASTRADAS, FAÇA SEU CADASTRO E ADICIONE AS SUAS DESEPESAS: \n1- CADASTRO USUÁRIO\n 2- ADICONAR DESPESAS"))
                while(numeroOpcao<1 or numeroOpcao>2):
                    numeroOpcao = int(input("\n OPÇÃO INVÁLIDA!\nPARECE QUE NÃO HÁ SALÁRIO E NEM DESPESAS CADASTRADAS, FAÇA SEU CADASTRO E ADICIONE AS SUAS DESEPESAS: \n1- CADASTRO USUÁRIO\n 2- ADICONAR DESPESAS"))
        #Retorno Menu inicial
        case 5:
            numeroOpcao = int(input("\nOLÁ! SELECIONE A OPÇÃO DESEJADA: \n1-ADICIONAR SALÁRIO E VALORES\n2-ADICONAR DESPESAS\n3-SALDOS E DESPESAS\n4-ESTATISTICA\n"+"-"*30))
        #Saídas
        case 6:
            print("Foi bom ter você por aqui! Até a próxima! ;)")
            numeroOpcao =0









       

                

                



                    



