

############################################################
##    OGRENCI ADI  : GIZEM TUNCER                         ##
##    OGRENCI NO :                                        ##
##    BÖLÜM :YAZILIM MUHENDISLIGI TESSIZ YUKSEK LISANS    ##
############################################################

#########################################################################################################################
# Step 1: Install required libraries() / you can look for them where information.txt ####################################                      
# Step 2: Run main.py                                                                ####################################                    
# Step 3/1: And username = "admin"and password ="1234"                               ####################################    
# Step 3/2: Or you can create new account and username/password = your create username and password        ##############                                        ####################################      
# Step 4: Choose product type                                                        ####################################       
# Step 5: Choose product color                                                       ####################################      
# Step 6: Choose product number                                                      ####################################       
# Finally, You can see the sum price of product                                      ####################################       
# Notes: You want to select the back , you should make to click the back button      ####################################      
#########################################################################################################################




from PyQt5.QtWidgets import QApplication
from pages.login import LoginPage
app = QApplication([])

pencere = LoginPage()
pencere.show()
app.exec_()