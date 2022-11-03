import os
class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    kontrol7 = siteURL[:7]  #http
    kontrol8 = siteURL[:8]  #https
    http = "http://"
    https = "https://"
    if kontrol7 == http or kontrol8 == https:
        dataOpen.write(siteURL + "\n")
        dataOpen.close()
        print("Url kaydedildi.")
    else:
        print("Lütfen url'nin ön ekini (/'https://' veya 'http://') giriniz.")

  def dataRead(self):
      dataOpen = open(self.dataFile, 'r')
      if os.stat(self.dataFile).st_size==0:
          print("Henüz kaydedilmiş adres yok!")
      else:
            for dataShow in dataOpen:
                print(dataShow)
      dataOpen.close()
