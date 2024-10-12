# Dados de identificação de Alvo API

Este projeto é uma API simples desenvolvida em Python usando Flask que responde apenas a requisições GET no endpoint `/target`. A API retorna um objeto JSON com as informações de identificação de um alvo (target).

## Funcionalidades

- **Endpoint**: `GET /target`
- **Resposta**: Retorna um objeto JSON contendo o ID e o tipo do alvo.

Exemplo de resposta:
```json
{
  "tgt_id": 10003,
  "tgt_type": "Destroyer"
}
```

## Pré-requisitos

Antes de executar a aplicação, certifique-se de que tem as seguintes ferramentas instaladas:

- Python 3.x
- Pip (Python package manager)

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/PedroMagno11/Dados-Identificacao-de-Alvos-API.git DadosIdentificacaoDeAlvosAPI

cd DadosIdentidicacaoDeAlvosAPI
```

2. Instale as dependências listadas no arquivo `dependencias.txt`:

```bash
pip install -r dependencias.txt
```

## Executando a aplicação

Para iniciar o servidor Flask, execute o seguinte comando:

```bash
python run.py
```

O servidor será iniciado em `http://localhost:5000`.

## Como usar

Faça uma requisição GET para o seguinte endpoint:

```bash
GET http://localhost:5000/target
```

A resposta será um objeto JSON no seguinte formato:

```json
{
  "tgt_id": 10003,
  "tgt_type": "Destroyer"
}
```

## Estrutura do projeto

- **run.py**: Contém o código principal da API.
- **target.py**: É a classe de domínio da aplicação.
- **preconfigured_data.py"**: Contém dados pré-cadastrados ao sistema.
- **dependencias.txt**: Lista todas as dependências necessárias para rodar o projeto.

## Autores
- [Pedro Magno](https://github.com/pedromagno11)
- [Mixsodaime](https://github.com/Mixsodaime)