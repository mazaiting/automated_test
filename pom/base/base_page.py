from time import sleep
from selenium.webdriver import Remote


class Base(object):
    """
    POM 基类
    """

    def __init__(self, driver: Remote):
        """
        初始化
        :param driver: 驱动
        """
        self.driver = driver

    def open_browser(self, url):
        """
        打开浏览器
        :param url: 请求地址
        """
        # 最大化窗体
        self.driver.maximize_window()
        # 打开网页
        self.driver.get(url)
        pass

    def wait(self, time):
        """
        等待
        :param driver: 驱动
        :param time: 时间
        """
        self.driver.implicitly_wait(time)
        pass

    def get_element(self, *locator):
        """
        获取节点
        :param locator: 元组, example: (By.ID, 'foo')
        :param text: 输入的内容
        :return: 无
        """
        return self.driver.find_element(*locator)

    def input_text(self, *locator, text):
        """
        输入文本
        :param locator: 元组, example: (By.ID, 'foo')
        :param text: 输入的内容
        :return: 无
        """
        self.get_element(*locator).send_keys(text)
        pass

    def click(self, *locator):
        """
        点击
        :param locator: 元组, example: (By.ID, 'foo')
        :return: 无
        """
        self.get_element(*locator).click()
        pass

    def switch_to_window_and_close_old(self):
        """
        切换窗口, 并关闭之前的窗口
        :return: 无
        """
        # 新打开页面句柄
        handle = self.driver.window_handles[1]
        # 关闭当前页面
        self.driver.close()
        # 切换句柄
        self.driver.switch_to.window(handle)
        pass

    def quit(self):
        """
        关闭窗口
        :return:
        """
        sleep(2)
        self.driver.quit()
        pass
