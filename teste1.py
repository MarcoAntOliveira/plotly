import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import plotly.graph_objects as go
from PySide6.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Criando o layout principal da janela
        layout = QVBoxLayout()

        # Criando o gráfico Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='lines', name='Linha 1'))
        fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[14, 15, 16, 17], mode='lines', name='Linha 2'))

        # Salvando o gráfico como um arquivo HTML temporário
        fig.write_html('temp_plotly_graph.html')

        # Criando uma visualização web com QWebEngine
        with open('temp_plotly_graph.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
            webview = QWebEngineView()
            webview.setHtml(html_content)
        
        # Adicionando a visualização web ao layout
        layout.addWidget(webview)

        # Criando um widget central para a janela e definindo o layout principal
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
