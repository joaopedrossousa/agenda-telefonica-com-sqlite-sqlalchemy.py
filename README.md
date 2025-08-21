# 📞 Agenda Telefônica com Banco de Dados

Projeto simples de **Agenda Telefônica** desenvolvido em **Python** com **SQLAlchemy** e **SQLite**.  
Permite cadastrar, listar e gerenciar contatos utilizando persistência em banco de dados.

---

## 🚀 Tecnologias Utilizadas
- [Python 3.11+](https://www.python.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)

---

## 📂 Estrutura de Pastas
```
agendaTelefonicaComBD/
│── main.py                # Ponto de entrada do programa
│── seed.py                # Funções auxiliares para manipulação do banco
│── db/
│   ├── base.py             # Configuração do banco e sessão
│   ├── banco_de_dados.db   # Banco de dados SQLite
│   └── __init__.py
│── models/
│   ├── contatos.py         # Modelo da tabela de contatos
│   └── __init__.py
```

---

## ⚙️ Como Executar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/agendaTelefonicaComBD.git
   cd agendaTelefonicaComBD
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install sqlalchemy
   ```

4. **Execute o projeto**
   ```bash
   python main.py
   ```

---

## 🗄️ Banco de Dados
- O banco padrão é o **SQLite** e já está incluído no repositório (`db/banco_de_dados.db`).
- Caso queira iniciar um novo banco, basta deletar o arquivo `.db` e rodar novamente o projeto.

---

## ✨ Futuras Melhorias
- Interface gráfica (Tkinter ou PyQt).  
- Opção de exportar contatos em `.csv`.  
- Suporte a outros bancos de dados (MySQL/PostgreSQL).

---


