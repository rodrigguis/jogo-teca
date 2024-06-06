
# Jogo-Teca

Projeto de cadastro de loja de jogos


## Stack utilizada


**Back-end:** Python 3.12, Flash 3.0.0


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`API_KEY`

`ANOTHER_API_KEY`


## Deploy

Para fazer o deploy desse projeto rode

```bash
  npm run deploy
```


## Rodando localmente

Clone o projeto

```bash
  git clone https://link-para-o-projeto
```

Entre no diretório do projeto

```bash
  cd my-project
```

Instale as dependências

```bash
  npm install
```

Inicie o servidor

```bash
  npm run start
```


## Uso/Exemplos

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```


## Suporte

Para suporte, mande um email para fake@fake.com ou entre em nosso canal do Slack.


## Roadmap

- Melhorar o suporte de navegadores

- Adicionar mais integrações


## FAQ

#### Erro na versao flash

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
