from utils import ini

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}


# 获取chatGPT对象
def get_chatbot(is_proxy, i):
    key = ini.get_config_string("chatgpt", "key" + str(i))
    if key is None:
        return None
    else:
        from revChatGPT.V3 import Chatbot
        chatbot = Chatbot(api_key=key)
    if is_proxy:
        chatbot.proxy = proxies
    else:
        chatbot.proxy = None
    return chatbot


# 获取配置生成文档的线程数，默认值为2
def get_chat_thread_number():
    thread_no = ini.get_config_int("chatgpt", "thread_number")+1
    if thread_no is None:
        return 3
    else:
        return thread_no
