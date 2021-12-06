# 模仿静态变量的用法

def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1

if __name__ == '__main__':
    for i in range(3):
        varfunc()

print('-----')

class Static():
    static_var = 5
    def varfunc(self):
        self.static_var += 1
        print(self.static_var)

print(Static.static_var)
a = Static()
for i in range(3):
    a.varfunc()