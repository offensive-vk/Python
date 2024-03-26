from abc import ABC, abstractclassmethod, abstractstaticmethod, abstractproperty

class MyClass1(ABC):
    @abstractclassmethod
    def my_abstract_class_method(cls):
        pass

class MyClass2(ABC):
    @abstractstaticmethod
    def my_abstract_static_method():
        pass

class MyClass3(ABC):
    @abstractproperty
    def my_abstract_property(self):
        pass
