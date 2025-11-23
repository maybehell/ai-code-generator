"""
AI 代码生成器 - 主程序入口
基于 Ollama Qwen3:8b
作者: maybehell
日期: 2025-11-23
"""
import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from ui.main_window import MainWindow

def main():
    # 启用高 DPI 支持
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    app = QApplication(sys.argv)
    app.setApplicationName("AI Code Generator")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("maybehell")
    app.setStyle('Fusion')
    
    # 创建必要的目录
    os.makedirs('data', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()