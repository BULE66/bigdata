import yaml,os
class YamlRead:
    def __init__(self,yamlfile):
        '''如果第一次调用，读取yaml，否则返回之前读取的数据'''
        if os.path.exists(yamlfile):
            self.yamlfile=yamlfile
        else:
            raise FileNotFoundError('读取的yaml文件不存在')
        self.datas=None

    @property #方法变成一个属性来调用
    def data(self):
        with open(self.yamlfile,mode='rb') as f:
            self.datas=yaml.load(f)
        return self.datas
class Config:
    '''os.path.dirname:某个文件所在的路径
    BasePath：一定是框架的base目录'''
    BasePath=os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
    config_path=BasePath+'\config\config.yaml'
    chrome_driver_path=BasePath+'\lib\chromedriver.exe'
    firefox_driver_path=BasePath+'\lib\geckodriver.exe'
    picturePath=BasePath+'\picture'
    logger_path=BasePath+'\log'

    def __init__(self,config=config_path):
        self.config=YamlRead(config).data
    @property #方法变成一个属性来调用
    def ui(self):
        '''
        :return: config.yaml里面的ui的数据
        '''
        return self.config['ui']

    @property #方法变成一个属性来调用
    def browser(self):
        '''
        :return: config.yaml里面的ui的数据
        '''
        return self.config['browser']

    @property #方法变成一个属性来调用
    def database(self):
        '''
        :return: config.yaml里面的ui的数据
        '''
        return self.config['database']
baseConfig=Config()  #变量，整个配置，路径

if __name__ == '__main__':

    print(Config())

