
import datetime
class Osztaly:
    uj_osztaly = 0
    regi_osztaly = 0
    def __init__(self, nev, kor, szul_ev):
        self.nev = nev
        self.kor = kor
        self.kov_szerviz = kov_szerviz
        self.szul_ev = szul_ev
        if ossz_km < 100000:
            type(self).uj_osztaly += 1
        else:
            type(self).regi_osztaly += 1
    def vissza_km(self):
          return round(self.tank_l / self.fogyasztas * 100 - self.szakasz_km)
    def szerviz(self):
        return self.kov_szerviz - datetime.datetime.now().year
    @classmethod
    def flotta_db(cls):
        return cls.uj_osztaly + cls.regi_osztaly
    @staticmethod
    def flotta_info():
        return 'Alfa Osztaly mindíg az élen!\nTelefonszám: ...'
    
osztaly_01 = Osztaly('ABA-125', 120000, 2023, 300, 5.8, 39)
osztaly_02 = Osztaly('ABB-125', 12000, 2025, 200, 5.7, 41)
osztaly_02 = Osztaly('ACB-125', 120060, 2125, 299, 6.7, 61)
print(osztaly_01.vissza_km())
print(Osztaly.regi_osztaly)
print(Osztaly.uj_osztaly)
print(Osztaly.flotta_db)
print(Osztaly.flotta_db())
