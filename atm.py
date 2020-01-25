#!/usr/bin/python
#coding bY ilham Zakaria
#Thanks to Roomcode
import os
import getpass
import sys
import time

os.system('clear')

def welcome():
    print (" > > > ATM  MINI < < < ".center(os.get_terminal_size().columns))

def list():
  print ("""
              ✩✩✩  Bank Mini ✩✩✩
   
   [1] >  Tarik Tunai
   [2] >  Cek Saldo
   [3] >  Transfer
   [4] >  Ganti PIN
   [5] >  Keluar
   """)

def main_menu():
 welcome()
#Verifikasi Pin
 pin = ("123456")
 chance = 0
 while (chance < 3):
   login = getpass.getpass("Masukkan Pin Anda  \n".center(os.get_terminal_size().columns))
   if (login == pin):
      True
      break
   else:
      chance +=1
      os.system('clear')
      print ("Anda Salah Memasukkan Pin Selama {0} Kali".center(os.get_terminal_size().columns).format(chance))
      if (chance == 3):
         print ("")
         print ("ATM anda Terblokir !".center(os.get_terminal_size().columns))
         print ("")
         sys.exit(1)
 while True:
   balance =100000
   os.system('clear')
   list()
   menu = input("Silahkan Pilih : ")
   if (menu == '1'):
      print ("")
      wd = input("Masukkan Jumlah : ")
      os.system('clear')
      print ("Menarik Saldo Sebesar Rp {0}".format(wd))
      if (int(wd) > balance):
        os.system('clear')
        print ("")
        print ("Saldo Tidak Mencukupi ! ")
        time.sleep(3)
        continue
      else:
        animation = ("\/-\\")
        print ("Tunggu Sebentar ".center(os.get_terminal_size().columns))
        print ("")
        for i in range(80):
          time.sleep(0.1)
          sys.stdout.write("\r" + animation [i % len(animation)].center(os.get_terminal_size().columns))
          sys.stdout.flush()
        print ("")
        print ("Sukses Gan :v ".center(os.get_terminal_size().columns)) 
        time.sleep(3)
   elif (menu == '2'):
      # Pilhan Nomor 2 Cek saldo
      print ("Sisa Saldo Anda Sebesar  Rp",balance)
      time.sleep(3)
   elif (menu == '5'):
       sys.exit()
main_menu()
