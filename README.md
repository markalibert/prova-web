# Dashboard de CEPs do Brasil

Projeto acadêmico desenvolvido em Django para consulta, filtragem e visualização de dados de CEPs do Brasil.

## Funcionalidades

- Dashboard de Estados com cards de estatísticas e gráfico por estado.
- Dashboard de Cidades com filtro por UF e gráfico dinâmico.
- Dashboard de Bairros e Logradouros com filtros, ordenação e paginação.
- Pesquisa por CEP, cidade, bairro e logradouro.
- Gráficos dinâmicos utilizando Chart.js.
- Navegação lateral entre os dashboards.
- Painel administrativo do Django para gerenciamento dos estados.
- Upload e exibição das imagens dos estados.
- Banco SQLite incluído no repositório para permitir o teste imediato sem importar o CSV novamente.

## Tecnologias

- Python
- Django 5.2.6
- SQLite
- HTML5
- CSS3
- JavaScript
- Chart.js
- Pillow

## Pré-requisitos

É necessário ter instalado:

- Python 3.10, 3.11, 3.12 ou 3.13
- Git
- Acesso à internet para carregar a biblioteca Chart.js pelo CDN.

> O projeto atualmente utiliza Django 5.2.6. Para evitar incompatibilidades com esta versão específica, recomendamos utilizar Python 3.10 a 3.13.

## Como executar no Linux

### 1. Clonar o projeto

```bash
git clone https://github.com/markalibert/prova-web.git
cd prova-web
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

Depois da ativação, o terminal normalmente mostrará:

```text
(.venv)
```

### 4. Atualizar o pip

```bash
python -m pip install --upgrade pip
```

### 5. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 6. Executar o servidor

```bash
python manage.py runserver
```

Depois abra no navegador:

```text
http://127.0.0.1:8000/
```

## Como executar no Windows

### 1. Clonar o projeto

```powershell
git clone https://github.com/markalibert/prova-web.git
cd prova-web
```

### 2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Atualizar o pip

```powershell
python -m pip install --upgrade pip
```

### 5. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 6. Executar o servidor

```powershell
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

## Banco de dados

O projeto utiliza SQLite e o arquivo `db.sqlite3` já está incluído no repositório.

Por isso, para apenas testar o sistema, **não é necessário**:

- instalar PostgreSQL;
- criar um banco manualmente;
- importar novamente o CSV de CEPs.

O banco já contém os dados utilizados pelo projeto.

O arquivo CSV original é mantido fora do versionamento para evitar deixar o repositório desnecessariamente grande.

## Painel administrativo

Para acessar:

```text
http://127.0.0.1:8000/admin/
```

Cada pessoa que baixar o projeto pode criar seu próprio usuário administrador:

```bash
python manage.py createsuperuser
```

No Linux e no Windows, o comando é o mesmo quando o ambiente virtual estiver ativado.

## Estrutura principal

```text
prova-web/
├── app/                    # Configurações principais do projeto Django
├── ceps/                   # Aplicação principal
│   ├── migrations/         # Migrações do banco
│   ├── management/         # Comando para importação dos CEPs
│   ├── admin.py            # Configuração do Django Admin
│   ├── models.py           # Models Endereco e Estado
│   ├── urls.py             # Rotas da aplicação
│   └── views.py            # Lógica das páginas e consultas ORM
├── media/                  # Imagens enviadas pelo Admin
├── static/                 # CSS e JavaScript
├── templates/              # Templates HTML
├── dados/                  # Arquivos de dados utilizados na importação
├── db.sqlite3              # Banco de dados do projeto
├── manage.py               # Utilitário de administração do Django
└── requirements.txt        # Dependências Python
```

## Fluxo básico da aplicação

```text
Navegador
   ↓
URL
   ↓
View
   ↓
ORM do Django
   ↓
SQLite
   ↓
Contexto
   ↓
Template HTML
   ↓
JavaScript + Chart.js
   ↓
Dashboard
```

## Importante

O ambiente virtual `.venv/`, arquivos `.env`, caches do Python e o CSV original não fazem parte do versionamento.

Como o `db.sqlite3` já acompanha o projeto, basta clonar, criar o ambiente virtual, instalar as dependências e executar o servidor para começar a testar.

## Projeto acadêmico

Projeto desenvolvido para a disciplina de Web 1, com foco em Django, ORM, templates, filtros, paginação, administração, banco de dados e visualização de informações.
