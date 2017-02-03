#coding: UTF-8
def foo():
    n = 1
    def bar():
        print n # 引用非全局的外部变量n，构造一个闭包
    n = 2
    return bar

closure = foo()
# print closure.func_closure
# 使用dir()得知cell对象有一个cell_contents属性可以获得值
#print closure.func_closure[0].cell_contents # 2


'''''
查找创建对象
 _cls_name='LoginError'
 _packet_name = 'home.cates.'
'''



def get_cate_obj(_packet_name,_cls_name):
    _module_home = __import__(_packet_name,globals(),locals(),[_cls_name])

    obj =  getattr(_module_home,_cls_name)

    return obj()

# cls = get_cate_obj("reflection.foo","bar")
# print(cls.bar())

print (getattr(closure,"bar"))

# print (callable(getattr(closure,"bar")))