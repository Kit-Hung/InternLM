from openai import OpenAI
import json


def internlm_gen(prompt,client):
    '''
    LLM生成函数
    Param prompt: prompt string
    Param client: OpenAI client
    '''
    response = client.chat.completions.create(
        model="internlm2.5-latest",
        messages=[
            {"role": "user", "content": prompt},
      ],
        stream=False
    )
    return response.choices[0].message.content

api_key = 'eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDA1NDg5NiIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTczMDM4MzE2NiwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTMyNjY4NDU4ODIiLCJ1dWlkIjoiMTU1ZTEzNDQtOTIwOS00NzkyLTkyMzUtMmFlMzgxM2QyMDA5IiwiZW1haWwiOiIiLCJleHAiOjE3NDU5MzUxNjZ9.AG80vxIiiAXgvs7R18ChdaXmwad3jx0SEKMq3mgRfhciontUVPWSwLcax9FMKcItml7wDZDIcUy5yaej1TN8Ww'
client = OpenAI(base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",api_key=api_key)

content = """
书生浦语InternLM2.5是上海人工智能实验室于2024年7月推出的新一代大语言模型，提供1.8B、7B和20B三种参数版本，以适应不同需求。
该模型在复杂场景下的推理能力得到全面增强，支持1M超长上下文，能自主进行互联网搜索并整合信息。
"""
prompt = f"""
请帮我从以下``内的这段模型介绍文字中提取关于该模型的信息，要求包含模型名字、开发机构、提供参数版本、上下文长度四个内容，以json格式返回。
`{content}`
"""
res = internlm_gen(prompt,client)
res = res.strip('```json\n').strip('\n```')
res_json = json.loads(res)
print(res_json)