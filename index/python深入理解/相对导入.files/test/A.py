print("------------------------------------------------------")
import importlib
#mod = importlib.import_module("test.pk1-3.B")
__import__("test.pk1-3.B")
import test.pk2

print("我是 A ","name:" ,__name__,"package:" ,__package__)




