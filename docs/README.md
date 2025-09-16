# Foreign Exchange Rates

Aplicação **Python 3.13** + **Django 5.2.4** para consultar e exibir cotações históricas do **Dólar (USD)** em relação a **Real (BRL)**, **Euro (EUR)** e **Iene (JPY)**.  
Os dados vêm da API pública [VAT Comply](https://www.vatcomply.com/documentation) e são persistidos em banco de dados.

🔗 Acesse agora:(https://historical-exchange-rates.onrender.com)

---

## Funcionalidades

- Consulta de cotações para períodos de até **5 dias úteis**
- Filtro por moedas: **BRL**, **EUR** e **JPY**
- Armazenamento persistente das cotações
- Visualização em gráficos via **Highcharts**
- Testes automatizados com **pytest**

---

## Tecnologias Utilizadas

| Categoria | Ferramenta |
|-----------|------------|
| Linguagem | [Python 3.13](https://www.python.org/) |
| Back-end  | [Django 5.2.4](https://www.djangoproject.com/) |
| Front-end | [Highcharts](https://www.highcharts.com/) |
| Testes    | [pytest](https://pytest.org/) |

---

## Como Executar o Projeto

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrações
python manage.py migrate

# 5. Inicie o servidor
python manage.py runserver
```

> A aplicação será servida em `http://localhost:8000/` por padrão.


## 📄 Documentação da API

### 🔗 URL Base

- **Ambiente de Produção:**  
  `https://historical-exchange-rates.onrender.com/`

- **Ambiente Local:**  
  `http://localhost:8000/`

---

### 📅 GET `api/rates/period/`

Consulta todas as cotações registradas entre duas datas.

| Parâmetro     | Tipo        | Obrigatório |
|---------------|-------------|-------------|
| `start_date`  | `YYYY-MM-DD`| ✔️ |
| `end_date`    | `YYYY-MM-DD`| ✔️ |

**Exemplo:**

```bash
curl --request GET \
  --url 'https://historical-exchange-rates.onrender.com/api/rates/period/?start_date=2025-07-01&end_date=2025-07-05'
```

```json
{
  "data": [
    {
      "id": 157,
      "date": "2025-07-01",
      "base": "USD",
      "currency": "BRL",
      "value": 5.42887383573243
    },
    {
      "id": 158,
      "date": "2025-07-01",
      "base": "USD",
      "currency": "EUR",
      "value": 0.921234561234
    }
  ]
}
```

---

### 📅 GET `api/rates/day/`

Consulta todas as cotações registradas para uma data específica.

| Parâmetro     | Tipo        | Obrigatório |
|---------------|-------------|-------------|
| `start_date`  | `YYYY-MM-DD`| ✔️ |

**Exemplo**

```bash
curl --request GET \
  --url 'https://historical-exchange-rates.onrender.com/api/rates/day/?start_date=2025-07-01'
```

```json
{
  "data": [
    {
      "id": 159,
      "date": "2025-07-01",
      "base": "USD",
      "currency": "JPY",
      "value": 157.90235
    }
  ]
}
```

---

###	🪙 GET `api/rate/`

Consulta o histórico de cotações de uma moeda específica.

| Parâmetro | Tipo                         | Obrigatório |
|-----------|-----------------------------|-------------|
| `target`  | `BRL` \| `EUR` \| `JPY`     | ✔️ |

**Exemplo**


```bash
curl --request GET \
  --url 'https://historical-exchange-rates.onrender.com/api/rate/?target=JPY'
```

```json
{
  "data": [
    {
      "id": 163,
      "date": "2025-07-01",
      "base": "USD",
      "currency": "JPY",
      "value": 157.90235
    }
  ]
}
```

---

### 🪙🪙GET `api/rates/`

Retorna **todas** as cotações armazenadas.

```bash
curl --request GET \
  --url 'https://historical-exchange-rates.onrender.com/api/rates/'
```

```json
{
  "data": [
    {
      "id": 157,
      "date": "2025-07-01",
      "base": "USD",
      "currency": "BRL",
      "value": 5.42887383573243
    },
    {
      "id": 158,
      "date": "2025-07-01",
      "base": "USD",
      "currency": "EUR",
      "value": 0.921234561234
    }
  ]
}
```

---

### ❗ Códigos de Erro

| Código | Descrição                                                     |
|--------|---------------------------------------------------------------|
| `400 Bad Request`   | Parâmetros obrigatórios ausentes ou inválidos   |
| `500 Internal Error`| Erro interno do servidor                         |

---

## Convenção de Commits

Este projeto segue o padrão **Conventional Commits**.

```bash
git commit -m "feat: adicionar filtro por moeda"
git commit -m "fix: corrigir validação de intervalo de datas"
git commit -m "test: adicionar testes para serviço de cotações"
git commit -m "refactor: limpar lógica da view de gráfico"
```

---

## 👤 Autor

Desenvolvido por **Breno Rios**.
