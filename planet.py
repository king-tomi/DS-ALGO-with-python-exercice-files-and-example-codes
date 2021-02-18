from weakref import WeakKeyDictionary

class Positive:  
    """
        A Descriptor to wrap properties

        Args:
            self (undefined):

        """


    def __init__(self):
        self._instance_data = WeakKeyDictionary()

    def __get__(self,instance,owner):
        return self._instance_data[instance]

    def __set__(self,instance,value):
        if value <= 0:
            raise ValueError(f"Value {value} is not positive")
        self._instance_data[instance] = value

    def __delete__(self,instance):
        raise AttributeError("Cannot delete attribute")

class Planet:

    """
        Implementation class for planets

        Attribute:
            name (str): name of planet
            radius (int): radius of planet in meters
            orbital_period (int): the time taking to complete one orbit around the Sun in seconds
            surface_temprature (int): the surface temperature in Kelvin
            mass (int): the mass of the planet in kilogram
    
    """

    def __init__(self,name: str,radius: int,orbital_period: int,surface_temprature: int,mass: int):
        self.name = name
        self.radius = radius
        self.orbitl_period = orbital_period
        self.surface_temperature = surface_temprature
        self.mass = mass

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self,value: str):
        if not value:
            raise ValueError("cannot set empty planet name")
        self._name = value

    radius = Positive()
    orbitl_period = Positive()
    surface_temperature = Positive()
    mass = Positive()