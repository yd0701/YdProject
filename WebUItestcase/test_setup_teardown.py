# class TestMashang:
# #这个在所有的用例之前只执行一次
#     def setup_class(self):
#         print('\n在每个类执行前的初始化的工作：比如：创建日志对象，创建数据库的连接，创建 接口的请求对象。')
# #在每个用例之前执行一次
#     def setup(self):
#         print('\n在执行测试用例之前初始化的代码：打开浏览器，加载网页')
#     def test_01_baili(self):
#         print('\n测试百里')
#     def test_02_xingyao(self):
#         print('\n测试星瑶')
#     def teardown(self):
#         print('\n在执行测试用例之后的扫尾的代码：关闭浏览器')
#     def teardown_class(self):
#         print('在每个类执行后的扫尾的工作：比如：销毁日志对象，销毁数据库的连接，销毁 接口的请求对象。')