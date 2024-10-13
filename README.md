# Dados de identificação de Alvo API

Este projeto é uma API simples desenvolvida em Python usando Flask que responde apenas a requisições GET no endpoint `/target`. A API retorna um objeto JSON com as informações de identificação de um alvo (target).

## Funcionalidades

- **Endpoint**: `GET /target`
- **Resposta**: Retorna um objeto JSON contendo o ID e o tipo do alvo.

Exemplo de resposta:
```json
{
  "tgt_id": 10001,
  "tgt_position": {
    "posX": 0,
    "posY": 0
  },
  "tgt_type": "Fragata"
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
## Docker

Este projeto também pode ser executado em um contâiner Docker. Certifique-se de ter o Docker instalado em sua máquina.

### Construindo a imagem Docker

Para construir a imagem Docker, execute o seguinte comando na raiz do projeto:

```bash
docker build -t dados-alvo-api .
```
### Executando a aplicação (Com Docker)
```bash
docker run -p 5000:5000 dados-alvo-api
```

O servidor será iniciado em `http://127.0.0.1:5000/`

## Executando a aplicação (Sem docker)

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
ou 
```
GET http://127.0.0.1:5000/target
```

A resposta será um objeto JSON no seguinte formato:

```json
{
  "tgt_id": 10001,
  "tgt_position": {
    "posX": 0,
    "posY": 0
  },
  "tgt_type": "Fragata"
}
```

## Estrutura do projeto

- **run.py**: Contém o código principal da API.
- **target.py**: É a classe de domínio da aplicação.
- **preconfigured_data.py"**: Contém dados pré-cadastrados ao sistema.
- **dependencias.txt**: Lista todas as dependências necessárias para rodar o projeto.
- **Dockerfile**: Contém as instruções para construir a imagem Docker da aplicação.

## Autores
- [Pedro Magno](https://github.com/pedromagno11)
- [Mixsodaime](https://github.com/Mixsodaime)