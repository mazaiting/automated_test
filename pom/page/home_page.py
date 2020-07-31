from selenium.webdriver.common.by import By
from pom.base import Base
from time import sleep


class HomePage(Base):
    """
    百度首页
    """
    # 输入框元组
    input_locator = (By.ID, 'kw')
    # 按钮元组
    btn_locator = (By.ID, 'su')
    # 第一条数据
    item_locator = (By.XPATH, '//*[@id="1"]/h3/a')

    def search(self, text):
        """
        搜索
        :param text: 待搜索的文本
        :return: 无
        """
        # 打开浏览器
        self.open_browser('http://www.baidu.com')
        self.wait(20)
        # 输入文本
        self.input_text(*self.input_locator, text=text)
        # 搜索
        self.click(*self.btn_locator)
        sleep(2)
        self.click(*self.item_locator)
        pass

    pass
