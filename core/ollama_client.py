"""
Ollama API 客户端
"""
import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        self.model = "qwen2.5:3b"
    
    def test_connection(self):
        """测试连接"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def generate_code(self, prompt, language="Python", temperature=0.7):
        """生成代码"""
        system_prompt = f"""
        你是一个专业的 {language} 代码生成助手。
        请根据用户的需求生成高质量、可运行的代码。
        要求：
        1. 代码要有适当的注释
        2. 遵循最佳实践和代码规范
        3. 只返回代码，不要有额外的解释
        4. 代码要完整且可以直接运行
        """
        
        full_prompt = f"{system_prompt}\n\n用户需求: {prompt}\n\n请生成 {language} 代码:"
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": temperature,
                        "top_p": 0.9,
                        "top_k": 40
                    }
                },
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                code = result.get('response', '')
                code = code.replace('```python', '').replace('```', '').strip()
                return code
            else:
                raise Exception(f"API 错误: {response.status_code}")
                
        except requests.exceptions.Timeout:
            raise Exception("请求超时，请检查网络或 Ollama 服务")
        except requests.exceptions.ConnectionError:
            raise Exception("无法连接到 Ollama 服务，请确认服务已启动")
        except Exception as e:
            raise Exception(f"生成失败: {str(e)}")
    
    def optimize_code(self, code, language="Python", temperature=0.5):
        """优化代码"""
        prompt = f"请优化以下 {language} 代码，提高性能和可读性。只返回优化后的代码:\n\n{code}"
        return self.generate_code(prompt, language, temperature)
    
    def explain_code(self, code, language="Python"):
        """解释代码"""
        messages = [
            {"role": "user", "content": f"请详细解释以下 {language} 代码的功能和实现原理:\n\n{code}"}
        ]
        return self.chat(messages, 0.3)
    
    def chat(self, messages, temperature=0.7):
        """聊天接口"""
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": False,
                    "options": {
                        "temperature": temperature
                    }
                },
                timeout=120
            )
            
            if response.status_code == 200:
                return response.json()['message']['content']
            else:
                raise Exception(f"API 错误: {response.status_code}")
        except Exception as e:
            raise Exception(f"聊天失败: {str(e)}")
