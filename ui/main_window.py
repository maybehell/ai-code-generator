import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AI Code Generator')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet('background-color: #1e1e1e; color: #ffffff;')
        self.initUI()

    def initUI(self):
        tabs = QTabWidget(self)

        # Code Generation Tab
        code_gen_tab = QWidget()
        code_gen_layout = QVBoxLayout()
        code_gen_label = QLabel('Code Generation')
        code_gen_textedit = QTextEdit(self)
        code_gen_button = QPushButton('Generate Code', self)
        code_gen_layout.addWidget(code_gen_label)
        code_gen_layout.addWidget(code_gen_textedit)
        code_gen_layout.addWidget(code_gen_button)
        code_gen_tab.setLayout(code_gen_layout)

        # Optimization Tab
        optimization_tab = QWidget()
        optimization_layout = QVBoxLayout()
        optimization_label = QLabel('Optimization')
        optimization_textedit = QTextEdit(self)
        optimization_button = QPushButton('Optimize Code', self)
        optimization_layout.addWidget(optimization_label)
        optimization_layout.addWidget(optimization_textedit)
        optimization_layout.addWidget(optimization_button)
        optimization_tab.setLayout(optimization_layout)

        # Explanation Tab
        explanation_tab = QWidget()
        explanation_layout = QVBoxLayout()
        explanation_label = QLabel('Explanation')
        explanation_textedit = QTextEdit(self)
        explanation_button = QPushButton('Explain Code', self)
        explanation_layout.addWidget(explanation_label)
        explanation_layout.addWidget(explanation_textedit)
        explanation_layout.addWidget(explanation_button)
        explanation_tab.setLayout(explanation_layout)

        tabs.addTab(code_gen_tab, 'Code Generation')
        tabs.addTab(optimization_tab, 'Optimization')
        tabs.addTab(explanation_tab, 'Explanation')

        self.setCentralWidget(tabs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())