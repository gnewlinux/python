from django.shortcuts import render
from .models import DadosPessoais


def portifolio_exibir(request):

	pessoa = DadosPessoais.objects.all()
	context = {'pessoa' : pessoa}
	return render(request, 'portifolios/portifolio_exibir.html', context)