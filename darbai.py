class NuomosPunktas:
    def __init__(self,adresas, automobiliai):
        self.adresas = adresas
        self.automobiliai = automobiliai


class Autombilis:
    def __init__(self,nuomosPunktas, kaina, arIsnuomuotas ):
        self.nuomosPunktas = nuomosPunktas
        self.kaina = kaina
        self.arIsnuomuotas = arIsnuomuotas

    def isnuomuoti(self):
        if self.arIsnuomuotas == True:
            print(f'Automobilis isnuomuotas')
        else:
            print('Automobilis neisnuomuotas')        

car1 = Autombilis('pirmasis', 500 , True)

# car1.isnuomuoti()

class Klientas(Autombilis):
    def __init__(self, nuomosPunktas, kaina, arIsnuomuotas, vardas , pavarde , nuolaida):
        super().__init__(nuomosPunktas, kaina, arIsnuomuotas)
        self.vardas = vardas
        self.pavarde = pavarde
        self.nuolaida = nuolaida

    def __str__(self):
        return f'{self.nuomosPunktas} {self.kaina}, {self.arIsnuomuotas}, {self.vardas}, {self.pavarde}, {self.nuolaida}'    
    
    def grazinti_automobili(self):
        if self.arIsnuomuotas:
            self.arIsnuomuotas = False
            print(f"{self.vardas} {self.pavarde} sėkmingai grąžino automobilį.")
        else:
            print("Automobilis jau grąžintas.")
            

    def atnaujinti_duomenis(self, vardas, pavarde, nuolaida):
        self.vardas = vardas
        self.pavarde = pavarde
        self.nuolaida = nuolaida
        print("Kliento duomenys atnaujinti sėkmingai.")

    def automobiliu_istorija(self):
        print(f"{self.vardas} {self.pavarde} automobilių nuomos istorija:")

client1 = Klientas('antras', 300, True, 'Vardenis', 'Pavardenis', '20%')
 
# print(client1)

# client1.isnuomuoti()


 


class Filmas:
    def __init__(self, filmo_id, pavadinimas, rezisierius, metai, zanras, reitingas ):
        self.filmo_id = filmo_id 
        self.pavadinimas = pavadinimas
        self.rezisierius = rezisierius
        self.metai = metai
        self.zanras = zanras
        self.reitingas = reitingas
       
    
    def __str__(self): 
        return f'ID:{self.filmo_id}  Pavadinimas:{self.pavadinimas}, Rezisiserius:{self.rezisierius}, Metai:{self.metai}, Zanras:{self.zanras},  Reitingas:{self.reitingas} '
    



class FilmuDuomenuBaze:
    def __init__ (self):
        self.filmu_list = []
    
    def prideti_filma(self,filmas):
        self.filmu_list.append(filmas)
    
    def filmu_sarasas(self):
     for filmas in self.filmu_list:
         print(filmas)


    def surasti_pagal(self, paieskos_zodis):
        print(f"Surandami filmai pagal pavadinimą, rezisierių arba žanrą, kuriuose yra: {paieskos_zodis}")
        rasti_filmai = []
        for filmas in self.filmu_list:
            if paieskos_zodis.lower() in filmas.pavadinimas.lower() or paieskos_zodis.lower() in filmas.rezisierius.lower() or paieskos_zodis.lower() in filmas.zanras.lower():
                rasti_filmai.append(filmas)
        if rasti_filmai:
            print("Rasti filmai:")
            for filmas in rasti_filmai:
                print(filmas)
        else:
     
            print("Filmai pagal paiešką nerasti.")

    def atnaujinti_filma(self, filmo_id, naujas_pavadinimas, naujas_rezisierius, nauji_metai, naujas_zanras, naujas_reitingas):
        for filmas in self.filmu_list:
            if filmas.filmo_id == filmo_id:
                filmas.pavadinimas = naujas_pavadinimas
                filmas.rezisierius = naujas_rezisierius
                filmas.metai = nauji_metai
                filmas.zanras = naujas_zanras
                filmas.reitingas = naujas_reitingas
                print(f"Filmas su ID {filmo_id} atnaujintas sėkmingai.")
                return
        print(f"Filmas su ID {filmo_id} nerastas.")             

    def salinti_filma(self, filmo_id):
        for filmas in self.filmu_list:
            if filmas.filmo_id == filmo_id:
                self.filmu_list.remove(filmas)
                print(f"Filmas su ID {filmo_id} pašalintas iš duomenų bazės.")
                return
        print(f"Filmas su ID {filmo_id} nerastas duomenų bazėje.")
 


film1 = Filmas(1,'Scarface', 'Damato', 1984, 'Kriminalinis', 9.4, )
film2 = Filmas(2,'The Godfather', 'Coppola', 1972, 'Kriminalinis', 9.2, )
 

# print(film1)

# filmu_baze = FilmuDuomenuBaze()

# filmu_baze.prideti_filma(film1)
# filmu_baze.prideti_filma(film2)
# filmu_baze.prideti_filma(film3)

# filmu_baze.filmu_sarasas()

# filmu_baze.salinti_filma(3)

# filmu_baze.filmu_sarasas()



 
class Receptas:
    def __init__(self, recepto_id, pavadinimas, ingrendientai, instrukcijos ):
        self.recepto_id = recepto_id
        self.pavadinimas = pavadinimas
        self.ingredientai = ingrendientai
        self.instrukcijos = instrukcijos

    def __str__(self):
        return f'Recepto_id {self.recepto_id},  Pavadinimas: {self.pavadinimas}, Ingredientai: {self.ingredientai}, Instrukcijos: {self.instrukcijos}'



 

class ReceptuKnyga:
    def __init__(self):
         self.receptu_list = []


    def prideti_recepta(self, pavadinimas):
        self.receptu_list.append(pavadinimas)

    def receptu_sarasas(self,):
        for pavadinimas in self.receptu_list:
            print(pavadinimas)

    def surasti_pagal_pavadinima_ingredientus(self, paieskos_zodis):
        print(f"Surandami receptai pagal pavadinimą arba ingredientus, kurių pavadinime ar ingredientuose yra: {paieskos_zodis}")
        rasti_receptai = []
        for receptas in self.receptu_list:
            if paieskos_zodis.lower() in receptas.pavadinimas.lower() or paieskos_zodis.lower() in receptas.ingredientai.lower():
                rasti_receptai.append(receptas)
        if rasti_receptai:
            print("Rasti receptai:")
            for receptas in rasti_receptai:
                print(receptas)
        else:
            print("Receptų pagal paiešką nerasta.")

    def atnaujinti_recepta(self, recepto_id, naujas_pavadinimas, nauji_ingredientai, naujos_instrukcijos):
        for receptas in self.receptu_list:
            if receptas.recepto_id == recepto_id:
                receptas.pavadinimas = naujas_pavadinimas
                receptas.ingredientai = nauji_ingredientai
                receptas.instrukcijos = naujos_instrukcijos
                print(f"Receptas su ID {recepto_id} atnaujintas sėkmingai.")
                return
        print(f"Receptas su ID {recepto_id} nerastas")  

    def pateikti_statistika(self):
        print("Receptų statistika:")
        print(f"Viso receptų: {len(self.receptu_list)}")
                          

    def salinti_recepta(self, recepto_id):
        for pavadinimas in self.receptu_list:
            if pavadinimas.recepto_id == recepto_id:
                self.receptu_list.remove(pavadinimas)
                print(f"Receptas su ID {recepto_id} pašalintas iš duomenų bazės.")
                return
        print(f"Filmas su ID {recepto_id} nerastas duomenų bazėje.")
 






receptas1 = Receptas( 1,'Obuoliu pyragas', 'obuoliai, tesla, miltai', '....')
receptas2 = Receptas( 2,'Obuoliu pyragas', 'obuoliai, tesla, miltai', '....')
receptas3 = Receptas( 3,'Obuoliu pyragas', 'obuoliai, tesla, miltai', '....')
receptas4 = Receptas( 4,'Obuoliu pyragas', 'obuoliai, tesla, miltai', '....')

# print(receptas1, receptas2,receptas3, receptas4)


receptu_knyga = ReceptuKnyga()

receptu_knyga.prideti_recepta(receptas1)

# receptu_knyga.receptu_sarasas()


 

class Restoranas:
    def __init__(self):
        self.pinigai = 0
        self.arbatpinigiai = 0

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.pinigai += suma
            print(f"Pridėta {suma} pinigų. Dabar restorane yra {self.pinigai} pinigų.")
        else:
            print("Negalima pridėti neigiamos sumos pinigų.")

    def prideti_arbatpinigius(self, suma):
        if suma > 0:
            self.arbatpinigiai += suma
            print(f"Pridėta {suma} arbatpinigių. Dabar restorane yra {self.arbatpinigiai} arbatpinigių.")
        else:
            print("Negalima pridėti neigiamos sumos arbatpinigių.")

    def gauti_pajamas(self, suma):
        if suma > 0:
            self.pinigai += suma
            print(f"Gauta {suma} pinigų. Dabar restorane yra {self.pinigai} pinigų.")
        else:
            print("Negalima gauti neigiamos sumos pinigų.")


    def prideti_patiekala(self, patiekalas):
        self.patiekalai.append(patiekalas)
        print(f"Patiekalas {patiekalas} pridėtas prie meniu.")

    def pasalinti_patiekala(self, pavadinimas):
        for patiekalas in self.patiekalai:
            if patiekalas.pavadinimas == pavadinimas:
                self.patiekalai.remove(patiekalas)
                print(f"Patiekalas {pavadinimas} pašalintas iš meniu.")
                return
        print(f"Patiekalas {pavadinimas} nerastas meniu.")

    def keisti_patiekalo_kaina(self, pavadinimas, nauja_kaina):
        for patiekalas in self.patiekalai:
            if patiekalas.pavadinimas == pavadinimas:
                patiekalas.kaina = nauja_kaina
                print(f"Patiekalo {pavadinimas} kaina pakeista į {nauja_kaina}.")
                return
        print(f"Patiekalas {pavadinimas} nerastas meniu.")
 

    def apmoketi_uz_uzsakyma(self, suma):
        if suma <= self.pinigai:
            self.pinigai -= suma
            print(f"Apmokėta {suma} už užsakymą. Dabar restorane yra {self.pinigai} pinigų.")
        else:
            print("Nepakanka pinigų apmokėti už užsakymą.")

    def patikrinti_arbatpinigius(self, suma):
        if suma <= self.arbatpinigiai:
            self.arbatpinigiai -= suma
            print(f"Sumokėta {suma} arbatpinigių. Dabar restorane yra {self.arbatpinigiai} arbatpinigių.")
        else:
            print("Nepakanka arbatpinigių sumokėti už užsakymą.")        

class Meniu:
    def __init__(self, patiekalai):
        self.patiekalai = patiekalai

    def rodyti_meniu(self):
        print("Meniu:")
        for patiekalas in self.patiekalai:
            print(patiekalas)

class Patiekalas:
    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    def __str__(self):
        return f"Pavadinimas: {self.pavadinimas}, Kaina: {self.kaina}"

 
patiekalai = [Patiekalas("Cezario salotos", 10),
              Patiekalas("Juodoji sriuba", 8),
              Patiekalas("Karbonadas", 15),
              Patiekalas("Obuolių pyragas", 6)]

meniu = Meniu(patiekalai)

 
restoranas = Restoranas()

 
meniu.rodyti_meniu()
restoranas.prideti_pinigus(100)
restoranas.prideti_arbatpinigius(50)
restoranas.gauti_pajamas(80)


class Augalas:
    def __init__(self, veislė, sodinimo_laikas):
        self.veislė = veislė
        self.sodinimo_laikas = sodinimo_laikas

class Daržas:
    def __init__(self):
        self.augalai = []

    def sodinti_augalą(self, augalas):
        self.augalai.append(augalas)

    def iškasti_augalą(self, veislė):
        for augalas in self.augalai:
            if augalas.veislė == veislė:
                self.augalai.remove(augalas)
                print(f"{veislė} iškastas iš daržo.")
                return
        print(f"{veislė} nerastas darže.")

    def laistyti_augalus(self):
        print("Laistome augalus...")
        for augalas in self.augalai:
            print(f"{augalas.veislė} laistomas.")

    def tręšti_augalus(self):
        print("Tręšiame augalus...")
        for augalas in self.augalai:
            print(f"{augalas.veislė} tręšiamas.")

    def patikrinti_augalų_būklę(self):
        print("Patikriname augalų būklę...")
        for augalas in self.augalai:
            print(f"{augalas.veislė} būklė patikrinta.")

    def skinti_derlių(self):
        print("Skinti derlių...")
        for augalas in self.augalai:
            if augalas.būsena == 'brandus':
                print(f"{augalas.veislė} yra pasiruošęs derliui ir yra nukirptas.")
                self.augalai.remove(augalas)

    def sekti_augalų_būseną(self):
        print("Sekame augalų būseną...")
        for augalas in self.augalai:
            print(f"{augalas.veislė} būsena sekiama.")

    def nurpinti_piktžoles(self):
        print("Nurpiname piktžoles...")
        print("Piktžolės nurpintos.")        

    def priežiūros_darbai(self):
        for augalas in self.augalai:
           
            print(f"Priežiūros darbai su {augalas.veislė} augalu")

 
daržas = Daržas()

 
ag1 = Augalas("Pomidoras", "2024-02-25")
ag2 = Augalas("Agurkas", "2024-03-10")

 
daržas.sodinti_augalą(ag1)
daržas.sodinti_augalą(ag2)
 
daržas.priežiūros_darbai()