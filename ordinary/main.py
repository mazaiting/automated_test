from selenium import webdriver
from time import sleep

if __name__ == '__main__':
    """
    普通自动化测试代码编写
    """
    # 获取 Chrome 驱动
    driver = webdriver.Chrome()
    # 最大化窗体
    driver.maximize_window()
    # 打开网页
    driver.get('http://www.baidu.com')
    # 隐式等待
    driver.implicitly_wait(20)
    # 输入搜索文本
    driver.find_element_by_id('kw').send_keys('鲁迅')
    # 点击搜索
    driver.find_element_by_id('su').click()
    # 延时
    sleep(2)
    # 点击第一条
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
    # 延时
    sleep(2)
    # # 点击鲁迅著述传记, 直接调用无效果,需要切换句柄
    # driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/ul/li[2]/a').click()
    # 新打开页面句柄
    handle = driver.window_handles[1]
    # 关闭当前页面
    driver.close()
    # 切换句柄
    driver.switch_to.window(handle)
    # 点击鲁迅著述传记
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/ul/li[2]/a').click()
    # 关闭窗口
    driver.quit()
