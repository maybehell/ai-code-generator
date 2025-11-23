"""
代码生成核心逻辑
"""

class CodeGenerator:
    def __init__(self, ollama_client):
        self.client = ollama_client
    
    def generate(self, description, language, options=None):
        """生成代码主方法"""
        options = options or {}
        temperature = options.get('temperature', 0.7)
        
        return self.client.generate_code(description, language, temperature)
    
    def optimize_code(self, code, language):
        """优化代码"""
        return self.client.optimize_code(code, language)
    
    def add_comments(self, code, language):
        """添加注释"""
        prompt = f"请为以下 {language} 代码添加详细的中文注释:\n\n{code}"
        return self.client.generate_code(prompt, language)
    
    def explain_code(self, code, language):
        """解释代码"""
        return self.client.explain_code(code, language)
