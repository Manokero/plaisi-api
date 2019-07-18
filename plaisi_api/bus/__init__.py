
class EnumProvincesDominicanRepublic():
    SD = 'SD'
    SC = 'SC'
    SA = 'SA'

    @classmethod
    def as_tuple(cls):

        CITIES_DOMINICAN_REPUBLIC = [
            (cls.SD, 'Santo Domingo'),
            (cls.SC, 'San Cristobal'),
            (cls.SA, 'Santiago'),
        ]
    
    @classmethod
    def get_default(cls):
        return cls.SD