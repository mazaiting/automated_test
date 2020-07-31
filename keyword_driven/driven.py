from selenium import webdriver
from time import sleep


class Driven:
    """
    关键字驱动类
    """

    def __init__(self, driver_type):
        """
        初始化方法
        :param driver_type: 驱动类型
        """
        # 根据类型获取driver
        if driver_type == "chrome":
            # 获取 Chrome 驱动
            self.driver = webdriver.Chrome()
        if driver_type == "firefox":
            # 获取 Firefox 驱动
            self.driver = webdriver.Firefox()
        if driver_type == "edge":
            self.driver = webdriver.Edge()
        # 判断是否获取到驱动
        if self.driver is None:
            raise Exception("unknown type.")
        # 最大化窗体
        self.driver.maximize_window()

    def open_browser(self, url):
        """
        打开浏览器
        :param url: 请求地址
        """
        # 打开网页
        self.driver.get(url)
        pass

    def wait(self, time):
        """
        等待
        :param time: 时间
        """
        self.driver.implicitly_wait(time)
        pass

    def input_text(self, element_type, type_str, text):
        """
        输入文本
        :param element_type: 节点类型
        :param type_str: 节点字符串
        :param text: 文本
        :return: 无
        """
        if element_type == "id":
            self.driver.find_element_by_id(type_str).send_keys(text)
        if element_type == "xpath":
            self.driver.find_element_by_xpath(type_str).send_keys(text)
        if element_type == "name":
            self.driver.find_element_by_name(type_str).send_keys(text)
        pass

    def click(self, element_type, type_str):
        """
        点击
        :param element_type: 节点类型
        :param type_str: 节点字符串
        :return: 无
        """
        if element_type == "id":
            self.driver.find_element_by_id(type_str).click()
        if element_type == "xpath":
            self.driver.find_element_by_xpath(type_str).click()
        if element_type == "name":
            self.driver.find_element_by_name(type_str).click()
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
