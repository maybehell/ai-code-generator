"""
历史记录管理器
"""
import json
import os
from datetime import datetime

class HistoryManager:
    def __init__(self, history_file='data/history.json'):
        self.history_file = history_file
        self.history = self.load()
    
    def load(self):
        """加载历史记录"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save(self):
        """保存历史记录"""
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)
    
    def add_entry(self, entry):
        """添加记录"""
        self.history.insert(0, entry)
        if len(self.history) > 100:
            self.history = self.history[:100]
        self.save()
    
    def get_all(self):
        """获取所有记录"""
        return self.history
    
    def get_by_language(self, language):
        """按语言筛选"""
        return [h for h in self.history if h.get('language') == language]
    
    def search(self, keyword):
        """搜索记录"""
        return [h for h in self.history 
                if keyword.lower() in h.get('prompt', '').lower() 
                or keyword.lower() in h.get('code', '').lower()]
    
    def clear(self):
        """清空历史"""
        self.history = []
        self.save()