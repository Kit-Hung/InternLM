import os

def download_assist_tuner(model_name_or_path):
    # 设置环境变量
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

    # 下载模型
    os.system(
        f'mkdir -p {model_name_or_path} &&  huggingface-cli download --resume-download KitHung/intern_assistant --local-dir {model_name_or_path}')