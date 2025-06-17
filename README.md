# To Do List 📝

Projeto de gerenciador de tarefas construído com [Django](https://www.djangoproject.com/). Feito com ❤️ e café.

## Funcionalidades

- 👥 Cadastro e autenticação de usuários
- ➕ Criação de novas tarefas, exclusão e marcação como concluídas
- 🔍 Filtro e ordenação das tarefas (pendentes ou concluídas)
- 📊 Resumo de quantas tarefas já foram concluídas
- ⚙️ Edição de perfil e alteração de senha

## Tecnologias utilizadas

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-5.0-darkgreen?logo=django)](https://www.djangoproject.com/) 
[![SQLite](https://img.shields.io/badge/SQLite-lightgrey?logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html) 
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-38B2AC?logo=tailwindcss)](https://tailwindcss.com/) 
[![Font Awesome](https://img.shields.io/badge/Font%20Awesome-528DD7?logo=fontawesome)](https://fontawesome.com/) 
[![django-widget-tweaks](https://img.shields.io/badge/django--widget--tweaks-6d6d6d)](https://github.com/jazzband/django-widget-tweaks)

## Como executar

1. Clone o repositório
2. Crie um ambiente virtual e ative-o
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Linux/macOS
   # .\\.venv\\Scripts\\activate   # Windows
   ```
3. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```
4. Aplique as migrações do banco de dados
   ```bash
   python manage.py migrate
   ```
5. (Opcional) crie um superusuário para acessar o admin
   ```bash
   python manage.py createsuperuser
   ```
6. Inicie o servidor de desenvolvimento
   ```bash
   python manage.py runserver
   ```
7. Acesse `http://localhost:8000/` no navegador
