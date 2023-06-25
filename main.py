# 这是一个爬取汽车参数并保存为word文档的python脚本程序。
import logging
import threading
from utils import ini, txt, chatgpt, file, word
from params import gen

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)s] - %(levelname)s - %(message)s')


class MyThread(threading.Thread):
    def __init__(self, src_dir, gpt, dist_dirs, src_file_names):
        threading.Thread.__init__(self)
        self.src_dir = src_dir
        self.chatbot = gpt
        self.dist_dirs = dist_dirs
        self.src_file_names = src_file_names

    def run(self):
        try:
            dist_dirs = self.dist_dirs
            src_file_names = self.src_file_names
            for dir in dist_dirs:
                for file_name in src_file_names:
                    logging.info('开始生成{}文件'.format(file_name))
                    word.save(self.src_dir, self.chatbot, dir, file_name)
                    logging.info('生成{}文件完成'.format(file_name))
            # print(self.chatbot.ask('python保存日志文件'))
        except Exception as e:
            logging.error('线程出错，错误信息为：{}'.format(e))


if __name__ == '__main__':
    # 程序相关初始化
    logging.info('欢迎使用由Johnson大神写的程序《{}》'.format(ini.get_config_string("project", "app_name")))
    logging.info('作者：{}'.format(ini.get_config_string("project", "author")))
    logging.info('版本：{}'.format(ini.get_config_string("project", "version")))
    # 读取banner文件
    if None != txt.get_txt_content():
        logging.info("\n" + txt.get_txt_content())
    else:
        logging.error('读取banner.txt文件出错！')
        print('程序已退出！')
        exit(1)
    gen.gen()
    # 处理相关的文件夹,如果存在则清空，不存在则创建
    # 稿子源目录
    src_dir = ini.get_config_string("chatgpt", "src_dir")
    if src_dir is None:
        logging.error('配置文件中没有配置源目录！')
        print('程序已退出！')
        exit(1)
    src_file_names = file.read_file(cur_dir=src_dir, suffix='docx')
    if src_file_names is None:
        logging.error('源目录中没有docx格式的word文件！')
        print('程序已退出！')
        exit(1)
    logging.info('源目录中的docx后缀的word文件有：{}'.format(src_file_names))
    # 目标目录
    dist_dir = ini.get_config_string("chatgpt", "dist_dir")
    if dist_dir is None:
        logging.error('配置文件中没有配置目标目录！')
        print('程序已退出！')
        exit(1)
    dist_dir_number = ini.get_config_int("chatgpt", "dist_dir_number")
    if dist_dir_number is None:
        logging.error('配置文件中没有配置目标目录的数量！')
        print('程序已退出！')
        exit(1)
    dist_file_name_prefix = ini.get_config_string("chatgpt", "dist_file_name_prefix")
    if dist_file_name_prefix is None:
        logging.error('配置文件中没有配置目标文件的前缀！')
        print('程序已退出！')
        exit(1)
    dist_dirs = []
    for n in range(1, dist_dir_number + 1):
        logging.info('已清空并创建目录：' + dist_dir + '\\' + dist_file_name_prefix + str(n))
        file.create_dir(dist_dir + '\\' + dist_file_name_prefix + str(n))
        dist_dirs.append(dist_dir + '\\' + dist_file_name_prefix + str(n))

    # 程序相关初始化结束
    threads = []
    thread_number = chatgpt.get_chat_thread_number() + 1
    for i in range(1, thread_number):
        chatbot = chatgpt.get_chatbot(True, i)
        if chatbot is None:
            logging.error('获取chatGPT对象出错！')
            print('程序已退出！')
            exit(1)
        else:
            logging.info('获取chatGPT对象{}成功！'.format(i))
        thread = MyThread(src_dir, chatbot, dist_dirs, src_file_names)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print('程序已结束！')
