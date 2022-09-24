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
- [X] Subir o servidor e testar o projeto
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

- [X] Registar o app receitas
 ````
abrir o arquivo settings.py que está dentro da pasta PersonalCheffProj
acrescetar em INSTALLED_APPS (linha 33) o seguinte item:
'receitas',
 ````
- [X] Configurar a rota  inicial(index)
 ````
criar dentro da pasta receitas um arquivo chamado urls.py contendo:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
 ````
- [X] Criar a view para a rota inicial
````
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Seja bem Vindo")
````
- [X] Registar a rota inicial
````
Modificar o arquivo urls.py da pasta PersonalCheffProj

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls')),
]
````
- [X] Criar um arquivo index.html
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

-[X] Integrar arquivos estáticos (CSS, JS, IMG)
- Dentro da pasta do projeto (PersonalCheffProj), criar a pasta `static`
- Dentro da pasta `static`, colocar as imagens, os aqurivos css e as arquivos js que for utilizar
- no arquivo `setting.py`realize a importação da biblioteca `os` através do comando `import os` (linha 12)
 - mudar a linha 58 do `setting.py`:
 `'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')],`

 - mudar a linha 122 do `setting.py`:
 `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
  `STATICFILES_DIRS = [`
    `os.path.join(BASE_DIR, 'PersonalCheffProj/static')`
`]`

Executar o comando:
`python manage.py collectstatic`

colocar no inicio da pagina (index.html) conexão com o python
`{% load static %}`

Quando for inserir uma imagem statica tem que colocar:
  `<img src="{% static 'logo.png' %}" alt="">`
  `<link rel="stylesheet" href="{% static 'estilos.css' %}">`

-[X] Utilizando links
- para criar um link para a pagina index, independente de onde você esteja utilize o comando `url`:
`<a href="{% url 'sucodelaranja' %}>Página inicial</a>`

-[X] Criando o base.html
 - na pasta `template` crie o arquivo `base.html`. Esse arquivo contém todo o código de estrutura comum à todas as páginas. Nesse arquivo deve ficar tudo que tiver antes do `body`e tudo que tiver depois do `/body`.
 - neste arquivo deve conter o `{% load static%}`
 - neste arquivo, no local aonde será carregado o conteúdo das outras páginas, deve existir os          
    delimitadores `{% block content%}` e `{% endblock %}`

-[X] Separando em partials
 - criar uma pasta chamada `partials`dentro da pasta `templates`
 - dentro da pasta `templates` crie os arquivos que serão as **partes globais** utilizando no seu projeto como `header.html`, `footer.html`, `menu.html`, `side-bar.html`, etc. No nosso exemplo criamos as partials `header.html` e `footer.html`
 - insira em cada um dos arquivos partials seus códigos correspondentes. Exemplo: no arquivo header.html eu insiro todo o conteúdo que eu quero que seja apresentado no cabeçalho da minha  aplicação. Não se esqueça do comando `{% load static %}`.
 - para incluir as partials nos arquivos de destino utilize o comando `include`da seuinte maneira: `{% include 'partials/header' %}`
 
-[x] Renderizando dados dinamicamente
    - trocar informações fixas no html por informações dinâmicas vindas do arquivo python
    - Quero gerar a lista de receitas de forma dinâmica, vamos fazer isso utilizando o recurso do Django
    que passa uma informação para minhas templates(.html) através da passagem de um parâmetro no comando `render`que está em minha view (.py):
    ```python
        return render(request, 'index.html', 
        {'nome_da_receita': 'suco de laranja'})
    ```
    - Observe que passei atravé do comando `render` um `dicionário` para a template (`index.html`)
    eu posso exibir o conteúdo desse dicionário da seguinte forma:
        ```python
        <td><img src="{% static 'suco.png'%}" class="icone-suco">
        {{nome_da_receita}} </td>
        ```

        falta itens 



-[X] Criando um dicionario com as receitas

{% for chave, uma_receita in lista_receitas.items %}
   <tr>
    <td>
        <img src="{% static 'suco.png' %}" class="icone-suco">       
             {{uma_receita}} 
        </td>
    <td><a href="https://www.youtube.com/watch?v=Nn9140bDPnc">Vídeo da Receita</a></td>
    <td><a href="{% url 'sucodeabacaxi' %}" class="btn btn-info" >Ver receita completa</a></td>
    </tr>
    <tr>
        {% endfor %}


-[] Criando o banco de dados(MySQL/MariaDB)
-[] Instalando o conector do bando de dados MySQL
-[] Criando o modelo da receita
-[] Criando a migration (mapeamento)
-[] Realizando a migration
-[] Registrando um modelo no admin
-[] Criando um usuário para o ambiente administrativo
## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>

