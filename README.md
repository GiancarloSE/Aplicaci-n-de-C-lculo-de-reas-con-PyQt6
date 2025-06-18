# 🧮 Calculadora de Áreas con PyQt6

Aplicación de escritorio desarrollada en Python utilizando **Programación Orientada a Objetos (POO)** y **PyQt6**, que permite calcular el área de distintas figuras geométricas mediante una interfaz gráfica intuitiva.

---

## 📐 Figuras Disponibles

- Círculo
- Triángulo
- Rectángulo
- Cuadrado

---

## 📦 Requisitos

- Python 3.10 o superior
- PyQt6

---

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/GiancarloSE/Aplicaci-n-de-C-lculo-de-reas-con-PyQt6.git
   cd Aplicaci-n-de-C-lculo-de-reas-con-PyQt6
   ```

2. Instala las dependencias:
   ```bash
   pip install pyqt6
   ```

---

## ▶️ Ejecución

Ejecuta el archivo principal:

```bash
python app.py
```

---

## 🖥️ Estructura del Proyecto

```
proyecto/
├── app.py                  # Archivo principal
├── src/
│   ├── logica/
│   │   └── areas.py        # Clases POO para cada figura
│   └── vista/
│       ├── main_window.ui  # Diseñado con Qt Designer
│       └── ui_main.py      # Convertido con pyuic6
├── README.md
```

---

## 👨‍💻 Desarrolladores

- Antony Munive Ríos
- Giancarlo Marcio Soto Escobar

---

## 📋 Notas Técnicas

- Se siguen buenas prácticas de PEP-8.
- El menú **"Cálculo de Áreas"** permite seleccionar una figura mediante accesos directos o una ventana emergente (`Ctrl+A`).
- La ventana principal se cierra al presionar (`Ctrl+Q`).
- Todos los cálculos son implementados con POO sin uso de métodos estáticos.