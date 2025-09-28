
## 📄 Documentação da API

### 🔗 URL Base

- **Ambiente Local:**  
  `http://localhost:8000/` ou `http://127.0.0.1:8000/`

### GET `api/v1/exchange-rates/all`

Retorna **todas** as cotações armazenadas.

**Output:**

```json
{
  "data": [
    {
      "id": 1,
      "date": "2025-07-01",
      "base_code": "USD",
      "currency_code": "BRL",
      "value": "5.4278"
    },
    {
      "id": 2,
      "date": "2025-07-01",
      "base_code": "USD",
      "currency_code": "EUR",
      "value": "5.4278"
    }
  ]
}
```

---

### GET `api/v1/exchange-rates/date/`

Consulta todas as cotações registradas para uma data específica.

| Parâmetro     | Tipo        | Obrigatório |
|---------------|-------------|-------------|
| `exchange-date`  | `YYYY-MM-DD`| ✔️ |

**Output:**

```json
{
  "data": [
    {
      "id": 1,
      "date": "2025-07-01",
      "base_code": "USD",
      "currency_code": "JPY",
      "value": "5.4278"
    }
  ]
}
```

---

### GET `api/v1/exchange-rates/exchange-code/`

Consulta o histórico de cotações de uma moeda específica.

| Parâmetro | Tipo                         | Obrigatório |
|-----------|-----------------------------|-------------|
| `currency-code`  | `BRL` \| `EUR` \| `JPY`     | ✔️ |

**Output:**

```json
{
  "data": [
    {
      "id": 1,
      "date": "2025-07-01",
      "base_code": "USD",
      "currency_code": "JPY",
      "value": "5.4278"
    }
  ]
}
```

---

### GET `api/v1/exchange-rates/period/`

Consulta todas as cotações registradas entre duas datas.

| Parâmetro     | Tipo        | Obrigatório |
|---------------|-------------|-------------|
| `start-date`  | `YYYY-MM-DD`| ✔️ |
| `end-date`    | `YYYY-MM-DD`| ✔️ |

**Output:**

```json
{
  "data": [
    {
      "id": 1,
      "date": "2025-07-01",
      "base_code": "USD",
      "currency_code": "BRL",
      "value": "5.4278"
    },
    {
      "id": 2,
      "date": "2025-07-01",
      "base_code": "USD",
      "currency_code": "EUR",
      "value": "5.4278"
    }
  ]
}
```

---

