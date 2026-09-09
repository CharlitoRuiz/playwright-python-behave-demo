# Playwright + Python + Behave Demo

Proyecto de demostración desarrollado para explorar un framework BDD alternativo al stack utilizado previamente con Reqnroll y C#.

## Tecnologías

- Python
- Behave
- Playwright
- Gherkin
- Page Object Model

## Aplicación utilizada

https://homebanking-demo-tests.netlify.app/

## Escenarios implementados

### Inicio de sesión
Validación de inicio de sesión exitoso utilizando credenciales externas.

### Transferencias
Ejecución de una transferencia utilizando escenarios escritos en Gherkin.

## Estructura

- `features/`: escenarios BDD
- `features/steps/`: implementación de Given / When / Then
- `pages/`: Page Objects
- `test_data/`: datos utilizados durante las pruebas

## Instalación

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo e instalar dependencias:

```bash
pip install -r requirements.txt
playwright install firefox
```

## Ejecución

Ejecutar todos los escenarios:
```bash
behave
```

Ejecutar únicamente login:
```bash
behave features/login.feature
```

Ejecutar únicamente transferencias:
```bash
behave features/transfer.feature
```
