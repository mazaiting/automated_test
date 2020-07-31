from selenium import webdriver


class Driven(object):
    """
    驱动工具类
    """

    @staticmethod
    def get_driver(driver_type):
        """
        获取驱动类型
        :param driver_type: 驱动类型
        :return: 返回驱动
        """
        # 根据类型获取driver
        driver = None
        if driver_type == "chrome":
            # 获取 Chrome 驱动
            driver = webdriver.Chrome()
        if driver_type == "firefox":
            # 获取 Firefox 驱动
            driver = webdriver.Firefox()
        if driver_type == "edge":
            driver = webdriver.Edge()
        # 判断是否获取到驱动
        if driver is None:
            raise Exception("unknown type.")
        else:
            return driver
