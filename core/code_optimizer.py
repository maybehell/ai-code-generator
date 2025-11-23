"""
代码优化器
"""

class CodeOptimizer:
    def __init__(self, ollama_client):
        self.client = ollama_client
    
    def optimize(self, code, language, focus='all'):
        """
        优化代码
        focus: 'performance', 'readability', 'security', 'all'
        """
        prompts = {
            'performance': f"请优化以下 {language} 代码的性能，提高运行效率：",
            'readability': f"请优化以下 {language} 代码的可读性，使其更易理解：",
            'security': f"请检查并优化以下 {language} 代码的安全性：",
            'all': f"请全面优化以下 {language} 代码，包括性能、可读性和安全性："
        }
        
        prompt = prompts.get(focus, prompts['all'])
        full_prompt = f"{prompt}\n\n```{language.lower()}\n{code}\n```\n\n请只返回优化后的代码，不要有额外说明。"
        
        return self.client.generate_code(full_prompt, language, 0.5)