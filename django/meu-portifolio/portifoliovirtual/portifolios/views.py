from django.shortcuts import render

def portifolio_exibir(request):
	return render(request, 'portifolios/portifolio_exibir.html', {})