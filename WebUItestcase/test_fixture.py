# import pytest
#
#
# @pytest.fixture(scope='function', params=['成龙', '甄子丹', '李连杰'],ids=['cl','zzd','llj'], name='aaa')
# def my_fixture(request):
#     print('\n前置')
#     yield request.param
#     print('\n后置')
#
#
#
# class TestMashang:
#
#     def test_01_baili(self):
#         print('\n测试百里')
#
#     def test_02_xingyao(self, aaa):
#         print('\n测试星瑶')
#         print('---------'+str(aaa))
