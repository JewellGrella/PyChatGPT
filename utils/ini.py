import configparser
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)s]- %(levelname)s - %(message)s')


# 获取配置文件中的配置项的字符串
def get_config_string(section, property_name):
    config = configparser.ConfigParser()
    config.read("config\\config.ini", encoding="utf-8")
    try:
        return str(config.get(section, property_name))
    except Exception as e:
        logging.error("获取配置信息字符串出错，错误信息为：{}".format(e))
        return None


# 获取配置文件中的配置项的整数
def get_config_int(section, property_name):
    config = configparser.ConfigParser()
    config.read("config\\config.ini", encoding="utf-8")
    try:
        return int(config.get(section, property_name))
    except Exception as e:
        logging.error("获取配置信息整数出错，错误信息为：{}".format(e))
        return None
