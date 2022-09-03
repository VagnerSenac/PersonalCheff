# PersonalCheff
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<img src="exemplo-image.png" alt="exemplo imagem">

## Descrição
> Uma aplicação web de receitas chamada PersonalCheff desenvolvida durante o curso de Python no Senac Americana. A aplicação listará receitas eclicando em cada nome das receitas você pode ver a receita completa.

### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
- [X] Pré-requisitos
    - [X] Instalar o Python 3.10.6
    - [X] Instalar Visual Studio Code
- [x] Criar e ativar o ambiente virtual
```
python -m venv .\venv\
venv\Scripts\activate
````
- [x] Instalar Djano
````
python -m pip install django==3.2
````
- [x] Criar o projeto PersonalCheff
````
django-admin.py help
django-admin.py startproject PersonalCheffProj
````
- [ ] Subir o servidor e testar o projeto
````
cd PersonalCheffProj
python manage.py runserver
````
- [x] Alterar o idioma do projeto para `pt-br`
````
localizar o arquivo settings.py na pasta do projeto
 mudar para pt-br  ---  linha 106
 ````
- [x] Alterar o timezone do projeto para `America/Sao_Paulo`
 ````
localizar o arquivo settings.py na pasta do projeto
 mudar para America/Sao_Paulo  ---  linha 108
  ````
- [x] Criar o app receitas
 ````
Criar um novo terminal de uso
cd PersonalCheffproj
python manage.py startapp receitas
 ````

- [ ] Registar o app receitas
 ````
abrir o arquivo settings.py que está dentro da pasta PersonalCheffProj
acrescetar em INSTALLED_APPS (linha 33) o seguinte item:
'receitas',
 ````
- [ ] Configurar a rota  inicial(index)
 ````
criar dentro da pasta receitas um arquivo chamado urls.py contendo:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
 ````
- [ ] Criar a view para a rota inicial
````
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Seja bem Vindo")
````
- [ ] Registar a rota inicial
````
Modificar o arquivo urls.py da pasta PersonalCheffProj

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
]
````
- [ ] Criar um arquivo index.html
    - Dentro da pasta receitas(app), crie a pasta 'templates'
	- dentro da pasta templates, crie um arquivo HTMl  -- ---  Index.html
	-editar o arquivo views.py dentro da pasta do app

	``` python
         from django.shortcuts import render
         def index(request):
         return render(request, 'index.html')
	
	```
views.py  --- acrescentar

def sucodelaranja(request):
    return render(request, 'sucodelaranja.html')

Criar um arquivo sucodelaranja.html na pasta template

## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>

