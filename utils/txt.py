
def get_txt_content():
    try:
        with open('config\\banner.txt', 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        print('读取banner.txt文件出错，错误信息为：{}'.format(e))
        return None
