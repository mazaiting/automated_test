# automated_test
Automated Test By Python

#### 基础工具
- 语言: Python
- 驱动: WebDriver
- 框架: Selenium(WebUI自动化)、Appium(APP UI 自动化)、Requests(接口自动化)
- 编码规范(设计模式): POM、 关键字驱动
- 测试数据管理: PyMySQL、 txt/csv、 Excel(xlrd/openpyxl)、 Yaml(pyyaml)数据管理
- 测试用例管理: UnitTest、Excel
- 测试报告: HTMLTestRunner、Allure
- 异常处理: 截屏
- 邮件系统: SMTP
- 自动化: Jenkins

#### Install

1. [Python3.8](https://www.python.org/downloads/)
2. [WebDriver](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/third_party_drivers_and_plugins/) (存放路径为:`python38/chromedriver.exe`)
3. [Nox 模拟器](https://www.yeshen.com/) 

**注: 下载WebDriver时注意下载与自己浏览器对应版本的驱动** 

#### Framework

| Name        | Version           | Description  |
| ------------- |:-------------:| -----:|
| [selenium](https://www.selenium.dev/)      | 3.141.0 | 网页自动化测试工具 |
| [ddt](https://github.com/datadriventests/ddt)      | 1.4.1 | 数据驱动 |
| [requests](https://requests.readthedocs.io/en/master/)      | 2.24 | 网络请求工具 |
| [openpyxl](https://openpyxl.readthedocs.io/en/stable/)      | 3.0.4 | excel 处理工具 |
| [PyInstaller](http://www.pyinstaller.org/)      | 3.6 | 打包工具 |

#### 代码含义
- ordinary: 自动化普通写法
    - main.py 主程序
- keyword_driven: 关键字驱动写法
    - main.py 主程序(改进自动化普通写法)
    - driven.py 关键字驱动类
- pom: (POM + 关键字驱动)设计模式写法
    - base: 页面基类
        - base_page.py 测试页面基类
    - page: 页面
        - detail_page.py 详情页
        - home_page.py 首页
    - util: 工具类
        - driven.py 驱动工具类
    - main.py 主程序(根据自动化普通写法)
- unit_test: 单元测试 + 数据驱动(ddt)
    - main.py 单元测试主程序

#### 教程
1. [Appium 教程](https://www.jianshu.com/p/4e20838cbf70)
    
#### 文档
1. [Selenium 文档](https://www.selenium.dev/documentation/en/)
2. [requests 文档](https://requests.readthedocs.io/zh_CN/latest/)
