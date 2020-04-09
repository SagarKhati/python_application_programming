############### Descriptor ####################################################################################


# EmpNameDescriptor is defined to manage empname attribute.
class EmpNameDescriptor:
    def __get__(self, obj, owner):
        return self.__empname
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value
# EmpIdDescriptor is defined to manage empid attribute.
class EmpIdDescriptor:
    def __get__(self, obj, owner):
        return self.__empid
    def __set__(self, obj, value):
        if hasattr(obj, 'empid'):
            raise ValueError("'empid' is read only attribute")
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value
        
class Employee:
    empid = EmpIdDescriptor()           
    empname = EmpNameDescriptor()       
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
        
e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # --> 123456 - John
e1.empname = 'Williams'             
print(e1.empid, '-', e1.empname)    # --> 123456 - Williams
#e1.empid = 76347322                 # --> ValueError: 'empid' is read only attribute


############### Properties ##################################################################################


class Employee:
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
    def getEmpID(self):
        return self.__empid
    def setEmpID(self, value):
       if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
       self.__empid = value
    empid = property(getEmpID, setEmpID)      # empid attribute created using property.
    def getEmpName(self):
        return self.__empname
    def setEmpName(self, value):
        if not isinstance(value, str):
            raise TypeError("empname' must be a string.")
        self.__empname = value
    def delEmpName(self):
        del self.__empname
    empname = property(getEmpName, setEmpName, delEmpName)  # empname attribute created using property. It is deleted when delEmpName method is called.
    
e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # --> '123456 - John'
del e1.empname                      # --> Deletes 'empname'
#print(e1.empname)                  # --> AttributeError: 'Employee' object has no attribute '_Employee__empname'


############### Property - Decorator ########################################################################


class Employee:
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, value):
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value
    @property
    def empname(self):
        return self.__empname
    @empname.setter
    def empname(self, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value
    @empname.deleter
    def empname(self):
        del self.__empname
e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # --> '123456 - John'
del e1.empname                      # --> Deletes 'empname'
#print(e1.empname)                  # --> AttributeError: 'Employee' object has no attribute '_Employee__empname'


#############################################################################################

# Convert Fahrenheit to Celsius and Celsius to Fahrenheit
class Celsius:
    def __get__(self, obj, owner):
        return (obj.fahrenheit - 32) / 1.8
    def __set__(self, obj, value):
        obj.fahrenheit = value * 1.8 + 32
class Temperature:
    celsius = Celsius()
    def __init__(self, value):
        self.fahrenheit = value
res_lst = list()
t1 = Temperature(int(input()))
res_lst.append((t1.fahrenheit, t1.celsius))
t1.celsius = int(input())
res_lst.append((t1.fahrenheit, t1.celsius))
print("{}\n{}".format(*res_lst))