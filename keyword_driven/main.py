from selenium import webdriver
from time import sleep
from keyword_driven.driven import Driven

if __name__ == '__main__':
    """
    普通自动化测试代码编写
    """
    # 创建
    driven = Driven('chrome')
    # 打开浏览器
    driven.open_browser('http://www.baidu.com')
    # 等待
    driven.wait(20)
    # 输入搜索文本
    driven.input_text('id', 'kw', '鲁迅')
    # 点击搜索
    driven.click('id', 'su')
    # 延时
    sleep(2)
    # 点击第一条
    driven.click('xpath', '//*[@id="1"]/h3/a')
    # 延时
    sleep(2)
    # 切换窗口并关闭之前的窗口
    driven.switch_to_window_and_close_old()
    # 点击鲁迅著述传记
    driven.click('xpath', '/html/body/div[3]/div[1]/div[2]/ul/li[2]/a')
    # 关闭窗口
    driven.quit()
