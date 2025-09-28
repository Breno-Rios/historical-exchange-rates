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
