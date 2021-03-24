####### Class Patient ######## 
class Patient:
    def __init__(self,name=None,age=None,strand=None,has_condition=[]):
        self.name=name
        self.age=age
        self.strand=strand
        self.has_condition=[]