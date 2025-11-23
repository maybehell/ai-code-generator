"""
代码解释器
"""

class CodeExplainer:
    def __init__(self, ollama_client):
        self.client = ollama_client
    
    def explain(self, code, language, level='detailed'):
        """
        解释代码
        level: 'simple', 'detailed', 'expert'
        """
        prompts = {
            'simple': "请用简单易懂的语言解释这段代码的功能：",
            'detailed': "请详细解释这段代码的功能、实现原理和关键逻辑：",
            'expert': "请从专业角度深入分析这段代码，包括设计模式、时间复杂度、潜在问题等："
        }
        
        prompt = prompts.get(level, prompts['detailed'])
        full_prompt = f"{prompt}\n\n```{language.lower()}\n{code}\n```"
        
        messages = [{"role": "user", "content": full_prompt}]
        return self.client.chat(messages, 0.3)