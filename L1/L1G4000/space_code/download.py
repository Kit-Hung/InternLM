import os


def prepare_data():
    os.system('mkdir -p /home/user/model')
    download_sentence_transformer()
    download_paraphrase_multilingual_MiniLM_L12_v2()
    download_NLTK()
    download_xtuner()


def download_sentence_transformer():
    # 设置环境变量
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

    # 下载模型
    os.system(
        'huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir ~/model/sentence-transformer')


def download_paraphrase_multilingual_MiniLM_L12_v2():
    os.system(
        'cd /home/user/model && git clone https://www.modelscope.cn/Ceceliachenen/paraphrase-multilingual-MiniLM-L12-v2.git && cd /home/user/model/paraphrase-multilingual-MiniLM-L12-v2 && git lfs install && git lfs pull ')


def download_NLTK():
    os.system(
        'cd /home/user && git clone https://gitee.com/yzy0612/nltk_data.git  --branch gh-pages && cd /home/user/nltk_data && mv /home/user/nltk_data/packages/*  /home/user/nltk_data && cd /home/user/nltk_data/tokenizers && unzip punkt.zip && cd /home/user/nltk_data/taggers && unzip averaged_perceptron_tagger.zip')


def download_xtuner():
    os.system(
        'mkdir /home/user/data && cd /home/user/data && git clone https://github.com/InternLM/xtuner.git && mv /home/user/data/xtuner/README_zh-CN.md /home/user/data')
