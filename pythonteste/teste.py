#VARIÁVEIS INÍCIO
idade = 18
meses=('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov','Dez')
numMes=0
mes="Jan"
ano= 2000
horasLivre = 720
dinheiro = 0.00
dormir = 50
comida = 50
esporte = 50
comunicacao = 50
lazer = 50
#VARIÁVEIS CARREIRA
cargo = "Nenhum"
salario = 0.0
horasTrabalho = 0
escolaridade = "Médio"
proxEscola = "Graduação"
gastosEscola = 0.0
custoProxEscola = 0.0
horasEscola = 0
anoConclusao = 0
mesConclusao = 0
#INÍCIO
while True:
	if escolaridade=="Médio":
		custoProxEscola = 300
	if 0<=numMes<=11:
		mes = meses[numMes]
	print("-="*26)
	print(f"Idade:{idade}    {mes}/{ano}    {horasLivre}h Livre   R$%.2f\n"%dinheiro)
	print("Dormir:      %d/100	1-Carreira\nComida:      %d/100	2-Negócio\nEsporte:     %d/100	3-Banco\nComunicação: %d/100	4-Gastos\nLazer:       %d/100	5-Lazer             6-Mês-->"%(dormir,comida,esporte,comunicacao,lazer))
	print("-="*26)
	while True:
		op=input("")
#1 CARREIRA
		if op=="1":
			print("-="*26)
			print(f"Cargo:		    {cargo} 1-Procurar um Emprego\nSalário:	    R$%.2f  2-Fazer {proxEscola}\nHoras no Trabalho:  {horasTrabalho}h      3-Subir de Cargo\n\nEscolaridade:  	    {escolaridade}\nCusto:              R$%.2f\nHoras na Faculdade: {horasEscola}h                   4-Voltar"%(salario,gastosEscola))
			print("-="*26)
			op=input("")
#1.1 PROCURAR EMPREGO
			if op=="1":
				if cargo=="Nenhum":
					cargo="Estagiário"
					salario=700.0
					horasTrabalho=180
					horasLivre -= horasTrabalho
					print("-="*26)
					print("\n\n\n  VOCÊ CONSEGUIU ENTRAR NO MERCADO DE TRABALHO!!!\n\n\n					   1-Voltar")
					print("-="*26)
					op=input("")
				else:
					print("-="*26)
					print("\n\n	       VOCÊ JÁ ESTÁ EMPREGADO!\n           Digite '2' para pedir demissão\n\n\n					   1-Voltar")
					print("-="*26)
					op=input("")
					if op=="2":
						cargo="Nenhum"
						salario=0.0
						horasLivre+=horasTrabalho
						horasTrabalho=0
						break
					break
				break
#1.2 FACULDADES
			if op=="2":
				if escolaridade=="Cursando Graduação":
					print("-="*26)
					print(f"\n\n         Você Ainda Está {escolaridade}\n         Digite '2' para trancar a faculdade\n\n\n					   1-Voltar")
					print("-="*26)
					op=input("")
					if op=="2":
						gastosEscola=0
						horasEscola=0
						anoConclusao=0
						mesConclusao=0
						horasLivre+=150
						escolaridade="Médio"
						proxEscola="Graduação"
						break
					break
				if escolaridade=="Cursando Pós-Graduação":
					print("-="*26)
					print(f"\n\n         Você Ainda Está {escolaridade}\n         Digite '2' para trancar a faculdade\n\n\n					   1-Voltar")
					print("-="*26)
					op=input("")
					if op=="2":
						gastosEscola=0
						horasEscola=0
						anoConclusao=0
						mesConclusao=0
						horasLivre+=150
						escolaridade="Graduação"
						proxEscola="Pós-Graduação"
						break
					break
				if escolaridade=="Cursando Mestrado":
					print("-="*26)
					print(f"\n\n         Você Ainda Está {escolaridade}\n         Digite '2' para trancar a faculdade\n\n\n					   1-Voltar")
					print("-="*26)
					op=input("")
					if op=="2":
						gastosEscola=0
						horasEscola=0
						anoConclusao=0
						mesConclusao=0
						horasLivre+=150
						escolaridade="Pós-Graduação"
						proxEscola="Mestrado"
						break
					break
				if escolaridade=="Cursando Doutorado":
					print("-="*26)
					print(f"\n\n         Você Ainda Está {escolaridade}\n         Digite '2' para trancar a faculdade\n\n\n					   1-Voltar")
					print("-="*26)
					op=input("")
					if op=="2":
						gastosEscola=0
						horasEscola=0
						anoConclusao=0
						mesConclusao=0
						horasLivre+=150
						escolaridade="Mestrado"
						proxEscola="Doutorado"
						break
					break
				if escolaridade == "Cursando Pós-Doutorado":
					print("-="*26)
					print(f"\n\n         Você Ainda Está {escolaridade}\n         Digite '2' para trancar a faculdade\n\n\n					   1-Voltar")
					print("-="*26)
					op=input("")
					if op=="2":
						gastosEscola=0
						horasEscola=0
						anoConclusao=0
						mesConclusao=0
						horasLivre+=150
						escolaridade="Doutorado"
						proxEscola="Pós-Doutorado"
						break
					break
				if escolaridade=="Pós-Doutorado":
					print("-="*26)
					print("\n\n	     VOCÊ JÁ FEZ PÓS DOUTORADO!!!\n\n\n\n	         			   1-Voltar")
					print("-="*26)
					op = input("")
					break
			if op=="2":
				print("-="*26)
				print(f"\n\n                     {proxEscola}\n      Custa R$%.2f/mês  4 Anos de Duração\n         Digite '2' para cusar {proxEscola}\n\n			            	    1-Voltar"%custoProxEscola)
				print("-="*26)
				op=input("")
				if op=="2":
					if escolaridade=="Médio":
						escolaridade="Cursando Graduação"
						proxEscola="Pós-Graduação"
						gastosEscola=300
						horasEscola+=150
						horasLivre-=150
						anoConclusao=ano+4
						mesConclusao=numMes
						custoProxEscola=800
					if escolaridade=="Graduação":
						escolaridade="Cursando Pós-Graduação"
						proxEscola="Mestrado"
						gastosEscola=800
						horasEscola+=150
						horasLivre-=150
						anoConclusao=ano+4
						mesConclusao=numMes
						custoProxEscola=1300
					if escolaridade=="Pós-Graduação":
						escolaridade="Cursando Mestrado"
						proxEscola="Doutorado"
						gastosEscola=1300
						horasEscola+=150
						horasLivre-=150
						anoConclusao=ano+4
						mesConclusao=numMes
						custoProxEscola=5000
					if escolaridade=="Mestrado":
						escolaridade="Cursando Doutorado"
						proxEscola="Pós-Doutorado"
						gastosEscola=5000
						horasEscola+=150
						horasLivre-=150
						anoConclusao=ano+4
						mesConclusao=numMes
						custoProxEscola=10000
					if escolaridade=="Doutorado":
							escolaridade="Cursando Pós-Doutorado"
							proxEscola="Pós-Doutorado"
							gastosEscola=10000
							horasEscola+=150
							horasLivre-=150
							anoConclusao=ano+4
							mesConclusao=numMes
							custoProxEscola=10000
							break
					break
				break
#1.3 SUBIR DE CARGO
			if op=="3":
				if cargo=="Nenhum":
					print("-="*26)
					print("\n\n              VOCÊ NÃO ESTÁ EMPREGADO!\n\n\n\n			                   1-Voltar")
					print("-="*26)
					op=input("")
					break
				if cargo=="Estagiário":
					if (escolaridade=="Médio") or (escolaridade=="Cursando Graduação"):
						print("-="*26)
						print("\n\n        VOCÊ AINDA NÃO ESTÁ PRONTO PARA ISSO!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
					else:
						print("-="*26)
						print("\n\n              AGORA VOCÊ É ASSISTENTE!!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
						cargo="Assistente"
						salario=1100
						horasTrabalho=210
						horasLivre+=180
						horasLivre-=horasTrabalho
						break
					break
				if cargo=="Assistente":
					if (escolaridade=="Médio") or (escolaridade=="Cursando Graduação") or (escolaridade=="Graduação") or (escolaridade=="Cursando Pós-Graduação"):
						print("-="*26)
						print("\n\n        VOCÊ AINDA NÃO ESTÁ PRONTO PARA ISSO!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
					else:
						print("-="*26)
						print("\n\n              AGORA VOCÊ É SUPERVISOR!!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
						cargo="Supervisor"
						salario=2500
						horasTrabalho=240
						horasLivre+=210
						horasLivre-=horasTrabalho
						break
					break
				if cargo=="Supervisor":
					if (escolaridade=="Médio") or (escolaridade=="Cursando Graduação") or (escolaridade=="Graduação") or (escolaridade=="Cursando Pós-Graduação") or (escolaridade=="Pós-Graduação") or (escolaridade=="Cursando Mestrado"):
						print("-="*26)
						print("\n\n        VOCÊ AINDA NÃO ESTÁ PRONTO PARA ISSO!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
					else:
						print("-="*26)
						print("\n\n              AGORA VOCÊ É COORDENADOR!!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
						cargo="Coordenador"
						salario=3000
						horasTrabalho=270
						horasLivre+=240
						horasLivre-=horasTrabalho
						break
					break
				if cargo=="Coordenador":
					if (escolaridade=="Médio") or (escolaridade=="Cursando Graduação") or (escolaridade=="Graduação") or (escolaridade=="Cursando Pós-Graduação") or (escolaridade=="Pós-Graduação") or (escolaridade=="Cursando Mestrado") or (escolaridade=="Mestrado") or (escolaridade=="Cursando Doutorado"):
						print("-="*26)
						print("\n\n        VOCÊ AINDA NÃO ESTÁ PRONTO PARA ISSO!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
					else:
						print("-="*26)
						print("\n\n              AGORA VOCÊ É GERENTE!!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
						cargo="Gerente"
						salario=5000
						horasTrabalho=300
						horasLivre+=270
						horasLivre-=horasTrabalho
						break
					break
				if cargo=="Gerente":
					if (escolaridade=="Médio") or (escolaridade=="Cursando Graduação") or (escolaridade=="Graduação") or (escolaridade=="Cursando Pós-Graduação") or (escolaridade=="Pós-Graduação") or (escolaridade=="Cursando Mestrado") or (escolaridade=="Mestrado") or (escolaridade=="Cursando Doutorado") or (escolaridade=="Doutorado") or (escolaridade=="Cursando Pós-Doutorado"):
						print("-="*26)
						print("\n\n        VOCÊ AINDA NÃO ESTÁ PRONTO PARA ISSO!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
					else:
						print("-="*26)
						print("\n\n              AGORA VOCÊ É PRESIDENTE!!\n\n\n\n			                   1-Voltar")
						print("-="*26)
						op=input("")
						cargo="Presidente"
						salario=10000
						horasTrabalho=330
						horasLivre+=300
						horasLivre-=horasTrabalho
						break
					break
				break
#2 NEGÓCIO
		elif op=="2":
			break
#3 BANCO
		elif op=="3":
			break
#4 GASTOS
		elif op=="4":
			break
#5 LAZER
		elif op=="5":
			break
#6 MÊS-->
		elif op=="6":
			numMes+=1
			if numMes==12:
				numMes=0
				ano+=1
				idade+=1
			dinheiro+=salario
			if escolaridade=="Cursando Graduação":
				dinheiro-=300
				if ano==anoConclusao and mesConclusao==numMes:
					escolaridade="Graduação"
					horasLivre+=150
					horasEscola=0
					gastosEscola=0
					anoConclusao=0
					mesConclusao=0
			if escolaridade=="Cursando Pós-Graduação":
				dinheiro-=800
				if ano==anoConclusao and mesConclusao==numMes:
					escolaridade="Pós-Graduação"
					horasLivre+=150
					horasEscola=0
					gastosEscola=0
					anoConclusao=0
					mesConclusao=0
			if escolaridade=="Cursando Mestrado":
				dinheiro-=1300
				if ano==anoConclusao and mesConclusao==numMes:
					escolaridade="Mestrado"
					horasLivre+=150
					horasEscola=0
					gastosEscola=0
					anoConclusao=0
					mesConclusao=0
			if escolaridade=="Cursando Doutorado":
				dinheiro-=5000
				if ano==anoConclusao and mesConclusao==numMes:
					escolaridade="Doutorado"
					horasLivre+=150
					horasEscola=0
					gastosEscola=0
					anoConclusao=0
					mesConclusao=0
			if escolaridade=="Cursando Pós-Doutorado":
				dinheiro-=10000
				if ano==anoConclusao and mesConclusao==numMes:
					escolaridade="Pós-Doutorado"
					horasLivre+=150
					horasEscola=0
					gastosEscola=0
					anoConclusao=0
					mesConclusao=0
			break
		else:
			break