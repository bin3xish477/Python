import gc
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value #ctype reference count

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"

class A:
    def __init__(self):
        self.b = B(self)
        print(f"A: self: {hex(id(self))}, B: {hex(id(self.b))}")

class B:
    def __init__(self, a):
        self.a = a
        print(f"B: self: {hex(id(self))}, A: {hex(id(self.a))}")

gc.disable() #disablng gc collector

my_var = A()
print(ref_count(id(my_var)))
print(ref_count(id(my_var.b)))

print(object_by_id(id(my_var)))
print(object_by_id(id(my_var.b)))

a_id = id(my_var)
b_id = id(my_var.b)
my_var = None
print(ref_count(a_id))
print(ref_count(b_id))

gc.collect() #manually enabling garbage collector
#thus removing circular references created
print(object_by_id(a_id))
print(object_by_id(b_id))
