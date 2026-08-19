📱 App Aluno

    Plataforma digital para criação e visualização de Cartões de Identidade Acadêmica no estilo "ficha de personagem".

📌 Sobre o Projeto

Projeto desenvolvido a pedido da coordenação do curso para modernizar a identificação estudantil no ambiente acadêmico. A aplicação substitui a tradicional carteirinha física por um Cartão de Identidade Acadêmica Digital interativo, exibindo o perfil do estudante no estilo "ficha de personagem" com suas informações centrais: Nome, Curso e uma breve Bio.

✨ Funcionalidades

    Cartão de Identidade Digital: Substituição da carteirinha tradicional por um formato digital e moderno.

    Perfil "Ficha de Personagem": Exibição centralizada das informações principais do estudante (Nome, Curso e Bio).

    Painel Administrativo: Interface nativa (Django Admin) para cadastro e gestão ágil dos perfis dos alunos.

🛠️ Tecnologias Utilizadas

    Linguagem: Python

    Framework Web: Django

    Banco de Dados: SQLite (padrão nativo do Django)

    Frontend / Estilização: HTML5, Templates do Django (ajuste caso tenha usado algum framework CSS como Bootstrap)

🚀 Como Executar o Projeto
Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas na sua máquina:

    Python 3.x

    Git

    Django

  Passo a passo

  1- Clone o repositório:
    
    Bash

    git clone https://github.com/LeMinero/App-Aluno.git
    cd App-Aluno

  2- Crie e ative um ambiente virtual (recomendado):

        -Linux/macOS:
        Bash

        python3 -m venv venv
        source venv/bin/activate

        -Windows:
        Bash

        python -m venv venv
        venv\Scripts\activate

  3- Instale as dependências do projeto:
    Bash

    pip install -r requirements.txt

    (Caso não tenha o arquivo requirements.txt, instale o Django manualmente com: pip install django)

  4- Execute as migrações do banco de dados (SQLite):
    
    Bash

    python manage.py migrate

  5- Crie um superusuário para acessar o painel administrativo e cadastrar os alunos:
    
    Bash

    python manage.py createsuperuser

  6- Inicie o servidor de desenvolvimento:
    
    Bash

    python manage.py runserver

  7- Acesse a aplicação:
    Abra no seu navegador o endereço: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    
    
    <img width="1502" height="792" alt="image" src="https://github.com/user-attachments/assets/068e4d1f-40e7-4127-a8c9-72a0d4341c26" />
    

    <img width="1505" height="715" alt="image" src="https://github.com/user-attachments/assets/22bddce2-451c-42e1-be28-a344054a04d7" />
    

    <img width="1502" height="709" alt="image" src="https://github.com/user-attachments/assets/a6e9a8f4-a1f8-4776-99f8-d9b3f66f4b74" />



    
    
    
    Desenvolvido por Gustavo.
    https://github.com/LeMinero
