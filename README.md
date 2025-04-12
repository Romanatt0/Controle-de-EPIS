# Projeto-EPIS
Atividade Senai

Seja bem-vindo! Esse texto permite explicar as funcionalidades do programa.

Para instalar o Django, você pode seguir os passos abaixo. Vou te guiar com o processo básico, usando o pip, que é o gerenciador de pacotes do Python.

Passo 1: Instalar o Python
Se você ainda não tem o Python instalado, primeiro baixe e instale a versão mais recente do Python. Quando instalar, certifique-se de marcar a opção "Add Python to PATH".

Você pode verificar se o Python foi instalado corretamente digitando o seguinte comando no terminal ou prompt de comando:

python --version
Ou, se o seu sistema usa o Python 3 como padrão, talvez precise usar:

python3 --version
Passo 2: Criar um ambiente virtual (opcional, mas recomendado)
É uma boa prática usar um ambiente virtual para gerenciar as dependências do projeto. Para criar um ambiente virtual, basta rodar os seguintes comandos:

Navegue até a pasta onde você quer criar o seu projeto.
Crie o ambiente virtual com o comando:
python -m venv nome_do_ambiente
Ou, caso precise usar o Python 3:

python3 -m venv nome_do_ambiente
Ative o ambiente virtual:

Windows:
nome_do_ambiente\Scripts\activate
Linux/macOS:
source nome_do_ambiente/bin/activate
Quando o ambiente virtual estiver ativo, o nome do ambiente aparecerá no início da linha de comando.

Passo 3: Instalar o Django
Com o ambiente virtual ativo, você pode instalar o Django com o pip:

pip install django
Passo 4: Verificar a instalação
Para garantir que o Django foi instalado corretamente, execute:

django-admin --version
Isso deve exibir a versão do Django que foi instalada.

Passo 5: Criar um novo projeto Django
Agora, você pode criar um novo projeto Django com o seguinte comando:

django-admin startproject nome_do_projeto
Isso criará uma nova pasta chamada nome_do_projeto com a estrutura básica de arquivos do Django.

Passo 6: Rodar o servidor de desenvolvimento
Para rodar o servidor de desenvolvimento, entre na pasta do seu projeto:

cd nome_do_projeto
E depois, execute o seguinte comando:

python manage.py runserver
Ou, se for necessário usar o Python 3:

python3 manage.py runserver
Agora, você pode acessar o servidor Django no seu navegador, indo até http://127.0.0.1:8000/.

E pronto! Você tem o Django instalado e funcionando no seu ambiente local. Se precisar de mais alguma coisa, é só avisar!

{Tela base} Ao clicar na imagem/nome, deve abrir as opções de configurações do usuário. Nessa fase, se cadastre. Ao clicar em uma opção, deve abrir outros botões. Equipamentos, Controle de EPI, Colaborador.

{Equipamentos} Quando apertado, apareçam duas opções: cadastrar equipamento, editar equipamento. Quando entrar em uma das duas opções, caso não tenha se cadastrado/logado, aparecerá uma aba com a opção de cadastro/login.

{Cadastrar equipamento} Após fazer login, aparecerá a opção de cadastrar equipamento. Caso seja cadastrado, aparecerá “Equipamento cadastrado com sucesso!” Caso não, o equipamento não foi “cadastrado! Preencher o campo: "

{Editar equipamento} Quando não tiver dados no banco ou não for encontrada informação na pesquisa. Exibir a mensagem “Desculpe, mas não encontramos dados correspondentes à sua busca.“

Remover/Deletar. Ao clicar no botão de remover, deve aparecer um model/alert para realizar a confirmação.

Editar. Ao clicar no botão de editar, deve aparecer a tela de editar, que deve conter os mesmos elementos da tela de cadastrar. Porém, ao editar, deve mostrar os valores dos equipamentos nos campos.
