import unittest
from ddt import ddt, data, unpack


@ddt()
class Test(unittest.TestCase):

    """
    unittest实现:
        1. 继承unittest.TestCase类
        2. setUp函数在测试方法之前执行
        3. tearDown函数在测试方法之后执行
        4. 测试方法必须以test为前缀
        5. 如果想要运行全部的测试方法, 则在main方法中使用unittest.main()执行

    ddt数据驱动使用:
        1. 在类型名上添加ddt装饰器
        2. 在想要传参的方法上添加@data, 并设置数据
        3. 如果传递的参数组为多个, 则需要解参(使用unpack)
    """

    def setUp(self) -> None:
        print('setUp')
        pass

    def tearDown(self) -> None:
        print('tearDown')
        pass

    def test_a(self):
        print('test_a')

    @data('test_b')
    def test_b(self, text):
        print(text)

    @data(['data1', 'test'],
          ['data2', 'unittest'])
    @unpack
    def test_c(self, text, param):
        print('{}-{}'.format(text, param))

    pass


if __name__ == '__main__':
    unittest.main()
