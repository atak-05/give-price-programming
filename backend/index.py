from backend.file import FileSettings
class Main:

    

    products = {
    "kalem": {"renkler": {"mavi": 3, "siyah": 5, "kırmızı": 4}, "fiyat": None},
    "defter": {"renkler": {"sarı": 8, "pembe": 10, "yeşil": 9}, "fiyat": None},
    "kalemlik": {"renkler": {"mor": 6, "turuncu": 7, "beyaz": 8}, "fiyat": None},
    "bardak": {"renkler": {"şeffaf": 2, "mavi": 3, "kırmızı": 4}, "fiyat": None}
}
    def start(self):
        productChoice = self.choiceProduct()
        userProductColor= self.choiceProductColor(productChoice)
        self.choiceProductQuantity(productChoice,userProductColor)
        # 0.adım Login Page
        # 1.adım Ürün tipini seçiniz?
        
        # 2.adım Ürün Rengini Seçiniz?
        # 3.adım Ürün Adedini Seçiniz?
        # 4.Fiyat Al hesaplamaları yapılıp sonuç döndürülecel


    def choiceProduct(self):
        for product in self.products:
            print(product)
        userProduct = input("Lütfen Ürün Tipini Seçiniz!")
        fs =FileSettings()
        fs.fileWrite(userProduct)
        return userProduct
        

    def choiceProductColor(self,userProduct):
       
        for color in self.products[userProduct]['renkler']:
            print(color)
        userProductColor = input("Lütfen Ürün Rengini Seçiniz!")
        fs =FileSettings()
        fs.fileWrite(userProductColor)
        return userProductColor
    def choiceProductQuantity(self,userProduct,userProductColor):
        total = 0
        price = self.products[userProduct]['renkler'][userProductColor]
        userProductQuantity = input("Lütfen Ürün Adedini Sayı Olarak Yazınız")
        if userProductQuantity != None :
            if userProductQuantity != 0:
                total = int(price) * int(userProductQuantity)
                fs =FileSettings()
                fs.fileWrite(str(total))
            elif userProductQuantity == 0 :
                 print("Lütfen 0'dan büyük bir sayı giriniz")
            else :
                print("Lütfen sayı giriniz!!")
        else : 
                print("Lütfen bir sayı giriniz!!")
        print(total)

program = Main()
program.start()
  
    
    