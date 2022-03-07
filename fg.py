shutdown = input("Szeretnéd kitakarítani a cache mappát, hogy felgyorsítsd a számítógépedet? (igen / nem): ")
  
if shutdown == 'nem':
    os.system("shutdown /s /t 1")
else:
    os.system("shutdown /s /t 1")