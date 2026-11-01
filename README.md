# 🧪 API Test Suite (pytest)

🌐 [Español](#español) | [English](#english) | [Português](#português)

---

## 🇪🇸 Español

Suite de pruebas automatizadas de API REST con **Python + pytest + requests**, ejecutada en CI con **GitHub Actions** en cada push y pull request.

Las pruebas cubren la API pública de demostración [JSONPlaceholder](https://jsonplaceholder.typicode.com):

- ✅ Códigos de estado (200, 201, 404)
- ✅ Validación de esquema de las respuestas JSON
- ✅ Creación de recursos (POST) y eco del cuerpo enviado
- ✅ Integridad de relaciones (álbumes de un usuario)
- ✅ Tiempo de respuesta (< 2 segundos)

### Estructura

```
├── conftest.py          # Fixtures: sesión HTTP y URL base
├── requirements.txt     # Dependencias (pytest, requests)
├── tests/
│   ├── test_posts.py    # Pruebas del recurso /posts
│   └── test_users.py    # Pruebas del recurso /users
└── .github/workflows/
    └── ci.yml           # CI: ejecuta pytest en cada push/PR
```

### Ejecutar localmente

```bash
pip install -r requirements.txt
pytest -v
```

Resultado: **8 pruebas, todas en verde** ✅

---

## 🇬🇧 English

Automated REST API test suite with **Python + pytest + requests**, running in CI with **GitHub Actions** on every push and pull request.

The tests cover the public demo API [JSONPlaceholder](https://jsonplaceholder.typicode.com):

- ✅ Status codes (200, 201, 404)
- ✅ JSON response schema validation
- ✅ Resource creation (POST) with request-body echo
- ✅ Relationship integrity (a user's albums)
- ✅ Response time (< 2 seconds)

### Project layout

```
├── conftest.py          # Fixtures: HTTP session and base URL
├── requirements.txt     # Dependencies (pytest, requests)
├── tests/
│   ├── test_posts.py    # Tests for the /posts resource
│   └── test_users.py    # Tests for the /users resource
└── .github/workflows/
    └── ci.yml           # CI: runs pytest on every push/PR
```

### Run locally

```bash
pip install -r requirements.txt
pytest -v
```

Result: **8 tests, all passing** ✅

---

## 🇧🇷 Português

Suíte de testes automatizados de API REST com **Python + pytest + requests**, executada em CI com **GitHub Actions** a cada push e pull request.

Os testes cobrem a API pública de demonstração [JSONPlaceholder](https://jsonplaceholder.typicode.com):

- ✅ Códigos de status (200, 201, 404)
- ✅ Validação de esquema das respostas JSON
- ✅ Criação de recursos (POST) com eco do corpo enviado
- ✅ Integridade de relacionamentos (álbuns de um usuário)
- ✅ Tempo de resposta (< 2 segundos)

### Estrutura

```
├── conftest.py          # Fixtures: sessão HTTP e URL base
├── requirements.txt     # Dependências (pytest, requests)
├── tests/
│   ├── test_posts.py    # Testes do recurso /posts
│   └── test_users.py    # Testes do recurso /users
└── .github/workflows/
    └── ci.yml           # CI: executa pytest a cada push/PR
```

### Rodar localmente

```bash
pip install -r requirements.txt
pytest -v
```

Resultado: **8 testes, todos passando** ✅
