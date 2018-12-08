def lulu(a, b):
    return a + b

class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = self.a + self.b
    def addition(self):
        return lulu(self.a, self.b)
    def lul(self):
        return self.a + self.c

class Another_Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        c = Add(self.a, self.b).addition()
        return c

some_variable = Add(3, 4).addition()
some_variablex = Add(3, 4).lul()
some_variables = Another_Add(3,3).addition()
print (some_variablex)
print (some_variables)

dictionary = {'Scene1': 'dark_background', 'Scene2': 'placeholder_bg1', 'Scene3': 'placeholder_green', 'Scene4': 'placeholder_red', 'Scene5': 'placeholder_blue', 'Scene6': 'placeholder_purple'}