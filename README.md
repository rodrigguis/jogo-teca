
# Jogo-Teca

Projeto de cadastro de loja de jogos


## Stack utilizada


**Back-end:** Python 3.12, Flash 3.0.0


## Deploy

Para fazer o deploy desse projeto rode

```bash
  npm run deploy
```


## Rodando localmente

Rode o docker-compose para habilitar o banco de dados.

Clone o projeto

```bash
  git clone https://link-para-o-projeto
```

Acesse o diretorio projeto 

```bash
  cd joto-teca
```


Habilite o banco de dados

```bash
docker-compose up
```

Instale as dependências

```bash
  pip install requirements.txt
```

Inicie o servidor

```bash
  python app.py
```


## Roadmap

- Melhorar o suporte de navegadores

- Adicionar mais integrações


## FAQ

#### Erro na versao flash 2.xx

Instalar a versao atual

#### Erro ImportError: cannot import name '_app_ctx_stack' from 'flask'

O erro ImportError: cannot import name '_app_ctx_stack' from 'flask' geralmente indica que o Flask-SQLAlchemy está tentando acessar uma parte do Flask que pode ter sido movida ou renomeada em versões mais recentes.

###### Verifique as versoes instaladas

```bash
pip show flask
pip show flask-sqlalchemy
```

###### Atualize as bibliotecas: Se as versões parecerem desatualizadas

```bash
pip install --upgrade flask
pip install --upgrade flask-sqlalchemy
```

###### Se nao resolver, reinstale as bibliotecas
```bash
pip uninstall flask flask-sqlalchemy
pip install flask flask-sqlalchemy
```

#### Erro ImportError: cannot import name ´url_quote' from ´werkzeug.url´ 

O erro ocorre devido a incompatibilidades entre as versoes do Flask 2.2.2 e Werkzeug 3.0.0 

###### Solution

Equalize as versoes do Flask e Werkzeug (2.2.2)

