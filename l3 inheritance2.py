class father():
    def __init__(self,fname):
        self.fname = fname

    def father_name(self):
        print(f'{self.fname} is father of {self.mname}')

class brother():
    def __init__(self,bname):
        self.bname = bname

    def brother_name(self):
        print(f'{self.bname} is brother of {self.mname}')

class family(father,brother):
    def __init__(self,fname,mname,bname):
        self.mname = mname
        father.__init__(self,fname)
        brother.__init__(self,bname)

    def family_info(self):
        print(f'{self.mname} is son of {self.fname}')

thite = family('U thin','thite','naing lin oo')

thite.family_info()
thite.father_name()
thite.brother_name()

print('this is my family')