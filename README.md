# Easily Crypto API

A API simula uma fintech de compra e venda de criptoativos, com cotação atualizada de diversas criptomoedas. Esta é uma maneira simples e descomplicada para acompanhar e compreender o mercado antes de se arriscar no mundo das moedas em blockchain!

## Funcionalidades

- Criação, edição e deleção de usuários
- Criação, edição e deleção de endereços
- Criação de carteiras (Wallets)
- Cotação de criptomoedas em tempo real
- Simulação de compra e venda para cada carteira criada
- Exibição de extato de cada carteira com suas respectivas transações

## Link da nossa api

[API](https://easily-crypto-api.herokuapp.com/)

## Link da nossa documentação

[DOCUMENTAÇÃO](https://easily-crypto-api.herokuapp.com/api/documentation/)

## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:Easily-Crypto/easily-crypto-backend.git
```

Entre no diretório do projeto

```bash
  cd easily-crypto-backend
```

Crie seu ambiente virtual

```bash
  python -m venv nomeDoSeuAmbiente
```

Entre no seu ambiente virtual

```bash
  source nomeDoSeuAmbiente/bin/activate
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Rode as migrations

```bash
  ./manage.py makemigrations
```

```bash
  ./manage.py migrate
```

Inicie o servidor

```bash
  ./manage.py runserver
```

## Stack utilizada

**Back-end:** Python, Django-rest-framework

## Referência

- [Alpha Vantage API](https://www.alphavantage.co/documentation/)

## Autores

- [@rafhaelMallorga](https://github.com/rafhaelmallorga)
- [@hyanLopes](https://github.com/hyanlopes)
- [@isamimDantas](https://github.com/iasmimd)
- [@tarcilaGarcia](https://github.com/tarcilasg)
- [@gabrielMuniz](https://github.com/dejazz)
- [@richardCandido](https://github.com/rich-dacan)
