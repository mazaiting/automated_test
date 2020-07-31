from pom.page import HomePage, DetailPage
from pom.util import Driven

if __name__ == '__main__':
    # 获取驱动
    driver = Driven.get_driver('chrome')
    # 创建首页
    home_page = HomePage(driver)
    # 搜索鲁迅
    home_page.search('鲁迅')
    # 切换页面
    home_page.switch_to_window_and_close_old()
    # 详情页点击
    detail_page = DetailPage(driver)
    # 点击鲁迅著述传记
    detail_page.get_detail()
    pass
