import pytest


class TestLogin:
    age = 18
    def test_01_yangdong(self):
        # sleep(3)
        print('测试杨栋')
        # assert 1==2

    @pytest.mark.skipif(age >= 18, reason='已成年')
    @pytest.mark.run(order=2)
    def test_05_yangdong(self):
        # sleep(3)
        print('测试杨栋5')

    @pytest.mark.skip(reason="微微太漂亮")
    @pytest.mark.run(order=3)
    def test_06_yangdong(self):
        # sleep(3)
        print('测试杨栋6')
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_07_yangdong(self):
        # sleep(3)
        print('测试杨栋7')
    def test_08_yangdong(self):
        # sleep(3)
        print('测试杨栋8')
# if __name__ == '__main__':
#     pytest.main(['-vs','./WebUItestcase/test_login.py','-n=2'])
# #     # pytest.main(['-vs','-n=2'])
# #     pytest.main(['-vs','--reruns=2'])
# #     pytest.main(['-vs'])