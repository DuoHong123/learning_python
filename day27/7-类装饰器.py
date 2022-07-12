# 作者: 王道 龙哥
# 2022年06月29日11时44分54秒

class Test:
    def __init__(self,func):
        self.func=func
    def __call__(self, *args, **kwargs):
        print('这个是什么验证')
        return self.func(*args, **kwargs)


@Test   # 相当于test = Test(test)
def test():
    print("----test---")

test()