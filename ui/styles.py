"""
现代化 UI 样式表
"""

def get_stylesheet():
    return """
    /* 主窗口 */
    QMainWindow {
        background-color: #1e1e1e;
    }
    
    /* 通用部件 */
    QWidget {
        background-color: #1e1e1e;
        color: #d4d4d4;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    
    /* 分组框 */
    QGroupBox {
        border: 2px solid #3c3c3c;
        border-radius: 8px;
        margin-top: 10px;
        padding-top: 15px;
        font-weight: bold;
        color: #61dafb;
        background-color: #252526;
    }
    
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 15px;
        padding: 0 5px;
    }
    
    /* 标签 */
    QLabel {
        color: #d4d4d4;
        background-color: transparent;
    }
    
    /* 输入框 */
    QLineEdit {
        background-color: #2d2d30;
        border: 2px solid #3c3c3c;
        border-radius: 5px;
        padding: 8px;
        color: #d4d4d4;
        font-size: 11pt;
    }
    
    QLineEdit:focus {
        border: 2px solid #007acc;
    }
    
    /* 文本编辑框 */
    QTextEdit {
        background-color: #1e1e1e;
        border: 2px solid #3c3c3c;
        border-radius: 8px;
        padding: 10px;
        color: #d4d4d4;
        selection-background-color: #264f78;
    }
    
    QTextEdit:focus {
        border: 2px solid #007acc;
    }
    
    /* 下拉框 */
    QComboBox {
        background-color: #2d2d30;
        border: 2px solid #3c3c3c;
        border-radius: 5px;
        padding: 6px 10px;
        color: #d4d4d4;
        min-width: 100px;
    }
    
    QComboBox:hover {
        border: 2px solid #007acc;
    }
    
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    
    QComboBox QAbstractItemView {
        background-color: #2d2d30;
        border: 2px solid #007acc;
        selection-background-color: #094771;
        color: #d4d4d4;
    }
    
    /* 按钮 */
    QPushButton {
        background-color: #0e639c;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 10px 20px;
        font-size: 11pt;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #1177bb;
    }
    
    QPushButton:pressed {
        background-color: #005a9e;
    }
    
    QPushButton:disabled {
        background-color: #3c3c3c;
        color: #666666;
    }
    
    /* 选项卡 */
    QTabWidget::pane {
        border: 2px solid #3c3c3c;
        border-radius: 5px;
        background-color: #252526;
        top: -2px;
    }
    
    QTabBar::tab {
        background-color: #2d2d30;
        color: #969696;
        padding: 10px 20px;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        margin-right: 5px;
    }
    
    QTabBar::tab:selected {
        background-color: #252526;
        color: #61dafb;
        border-bottom: 3px solid #61dafb;
    }
    
    QTabBar::tab:hover {
        background-color: #3c3c3c;
        color: #d4d4d4;
    }
    
    /* 进度条 */
    QProgressBar {
        border: 2px solid #3c3c3c;
        border-radius: 5px;
        background-color: #2d2d30;
        height: 20px;
        text-align: center;
    }
    
    QProgressBar::chunk {
        background-color: qlineargradient(
            x1:0, y1:0, x2:1, y2:0,
            stop:0 #007acc, stop:1 #61dafb
        );
        border-radius: 3px;
    }
    
    /* 状态栏 */
    QStatusBar {
        background-color: #007acc;
        color: white;
        font-weight: bold;
        padding: 5px;
    }
    
    /* 分割器 */
    QSplitter::handle {
        background-color: #3c3c3c;
        width: 2px;
    }
    
    QSplitter::handle:hover {
        background-color: #007acc;
    }
    """