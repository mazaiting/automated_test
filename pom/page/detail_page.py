from selenium.webdriver.common.by import By
from pom.base import Base
from time import sleep


class DetailPage(Base):
    """
    详情页
    """
    # 点击鲁迅著述传记
    btn_locator = (By.XPATH, '/html/body/div[3]/div[1]/div[2]/ul/li[2]/a')

    def get_detail(self):
        """
        获取详情
        :return: 无
        """
        sleep(2)
        # 点击鲁迅著述传记
        self.click(*self.btn_locator)
        # 退出
        self.quit()

    pass
