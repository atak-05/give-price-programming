class FileSettings:
    def fileOpen(self):
        self.dosya = open("userChoices.txt", "a+")
    def fileWrite(self, choice):
        self.fileOpen()
        self.dosya.write(choice + "\n")
        self.dosya.close()
 