import pytest


class Test2:
    def test2(self):
        print('111')
if __name__ == '__main__':
    pytest.main(['-s', './test2.py'])