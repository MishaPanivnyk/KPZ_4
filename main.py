class Forest:
    def get_name(self):
        return "On Sand, Pine, Leafed, On swamp, Boron, Shifted, Taiga"


class On_sand(Forest):
    def get_name(self):
        return "This is a sandy forest"


class Pine(Forest):
    def get_name(self):
        return "This is a pine forest"


class Leafed(Forest):
    def get_name(self):
        return "This is a leafed forest"


class On_swamp(Forest):
    def get_name(self):
        return "This is a swamp forest"


class Boron(Forest):
    def get_name(self):
        return "This is a boron forest"


class Shifted(Forest):
    def get_name(self):
        return "This is a shifted forest"


class  Taiga(Forest):
    def get_name(self):
        return "This is a taiga forest"




class Boron(On_sand, Pine):
    pass


class Shifted(Pine, Leafed):
    pass


class Taiga(Leafed, On_swamp):
    pass


boron = Boron()
taiga = Taiga()


print(boron.get_name())        
print(taiga.get_name())