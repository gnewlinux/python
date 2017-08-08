#!/usr/bin/python

alunos = ["Diego","Roger"]

print "Sistema de medias!"
print "Alunos cadastrados:"
print alunos

aluno = raw_input("Digite o nome do aluno: ")
nota1 = input("Digite a nota do aluno: ")
nota2 = input("Digite a segunda nota do aluno: ")
media = (nota1 + nota2) / 2

if aluno == alunos[0]:
	pagamento = False
elif aluno == alunos[1]:
	pagamento = True

if aluno == alunos[0] or aluno == alunos[1]:
	if pagamento is True:
		print "Aluno aceito"
	else:
		print "Pagamento atrazado"
		exit()

	if media >= 5:
		print "Passou de ano! Media %s !"%media
	else:
		print "Aluno reprovado!",media
else:
	print "Aluno nao encontrado..."
