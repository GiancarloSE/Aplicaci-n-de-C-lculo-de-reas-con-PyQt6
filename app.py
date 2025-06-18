import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QInputDialog,
    QMessageBox,
)
from src.vista.ui_main import Ui_MainWindow
from src.logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conexión de acciones de menú
        self.ui.actionSalir.triggered.connect(self.close)

        # Submenú "Seleccionar Figura"
        self.ui.actionSeleccionarFigura.triggered.connect(self.seleccionar_figura)
        self.ui.actionCirculo.triggered.connect(self.abrir_dialogo_circulo)
        self.ui.actionTriangulo.triggered.connect(self.abrir_dialogo_triangulo)
        self.ui.actionRectangulo.triggered.connect(self.abrir_dialogo_rectangulo)
        self.ui.actionCuadrado.triggered.connect(self.abrir_dialogo_cuadrado)

    def seleccionar_figura(self):
        """Permite seleccionar una figura desde un diálogo y abre su cálculo."""
        opciones = ("Círculo", "Triángulo", "Rectángulo", "Cuadrado")
        figura, ok = QInputDialog.getItem(
            self,
            "Seleccionar Figura",
            "Selecciona una figura:",
            opciones,
            editable=False
        )
        if ok and figura:
            if figura == "Círculo":
                self.abrir_dialogo_circulo()
            elif figura == "Triángulo":
                self.abrir_dialogo_triangulo()
            elif figura == "Rectángulo":
                self.abrir_dialogo_rectangulo()
            elif figura == "Cuadrado":
                self.abrir_dialogo_cuadrado()


    def abrir_dialogo_circulo(self):
        radio, ok = QInputDialog.getDouble(self, "Círculo", "Radio:", min=0.0)
        if ok:
            figura = Circulo(radio)
            self.mostrar_resultado(figura.calcular_area())

    def abrir_dialogo_triangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Triángulo", "Base:", min=0.0)
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Triángulo", "Altura:", min=0.0)
            if ok2:
                figura = Triangulo(base, altura)
                self.mostrar_resultado(figura.calcular_area())

    def abrir_dialogo_rectangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Rectángulo", "Base:", min=0.0)
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Rectángulo", "Altura:", min=0.0)
            if ok2:
                figura = Rectangulo(base, altura)
                self.mostrar_resultado(figura.calcular_area())

    def abrir_dialogo_cuadrado(self):
        lado, ok = QInputDialog.getDouble(self, "Cuadrado", "Lado:", min=0.0)
        if ok:
            figura = Cuadrado(lado)
            self.mostrar_resultado(figura.calcular_area())

    def mostrar_resultado(self, area):
        QMessageBox.information(self, "Resultado", f"Área: {area:.2f}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
