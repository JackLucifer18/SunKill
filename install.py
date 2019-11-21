from os import system,sys
from time import  sleep

Yes = ["y", "yes", "Y", "Yes"]
No = ["n", "N", "No", "no"]

class hias():
	def Jack():
		print ("=========================================================")
		print ("|          github : Jack_Lucifer08@github.com        |")
		print ("|	    					     |")
		print ("|		   JACK LUCIFER TOOLS   		|")
		print ("|	    					     |")
		print ("|            gmail : aldifortuna18@gmail.com         |")
		print ("|	    					     |")
		print ("=========================================================")
	def buy():
		print ("================Beli Untuk Versi Premium=============")
	def instal():
		print ("=====================Proses Install Berjalan=====================")
	def selinst():
		print ("=====================Install Selesai=====================")
	def pembatas ():
		print ('==============================================================')
	def belum_install():
		print ("=============Maaf Silahkan Install Dulu Scriptnya==========°")

#for termux tools
class termux():
	def metas():
		print ("=====================Proses Install Berjalan=====================")
		print ("Mohon Sediakan Kuota dan data penyimpanan 1 GB lebih")
		pilihan =  input("Apakah anda ingin tetap menginstall [y/n] : ")
		if pilihan in  Yes:
			print ("Good Luck °✓°")
			sleep (2)
			system ("pkg update &&pkg upgrade")
			system ("pkg install unstable-repo")
			system ("pkg install metasploit")
			system ("cd /data/data/com.termux/files/usr/opt/metasploit-framework/")
			system ("gem install bundler")
			system ("gem update --system")
			system ("bundle install")
			print ("=====================Install Selesai=====================")
			print ("Untuk Memanggil Metasploit nya bisa ketikan langsung aja seperti msfconsole ataupun msfvenom atau bisa saja nanti saya sediakan")	
			sleep (5)
			system ("clear")
			system ("cd $home")
		else:
			print ('proses dihentikan')
			system("exit")
			system ("cd $home")
	def nmap ():
		hias.instal()
		system("pkg install root-repo")
		hias.Jack()
		hias.buy()
	def Aircrackng():
		hias.instal()
		system("pkg update &&pkg upgrade")
		hias.Jack()
		hias.buy()
		
		
#Proses Berjalan
class Proses():
	#menjalankan tools
	def running():
		hias.pembatas()
		print ('1. Metasploit')
		print ('2. Nmap')
		print ('3. Aircrack-ng')
		hias.pembatas()
		pilih = int(input('Masukan pilihan mu : '))
		if pilih == (1):
			print ("a. msfconsole")
			print ("b. msfvenom")
			pilih1 = str(input("Pilih Opsi : "))
			if pilih1 == ("a"):
				system("msfconsole")
			elif pilih1 == ("b"):
				system("msfvenom")
		elif pilih == (2):
			system("nmap")
		elif pilih == (3):
			print ('a. aircrack-ng')
			print ('b. airmon-ng')
			print ('c. airodump-ng')
			print ('d. aireplay-ng')
			pilih2 = input("Mau Mana Bos Ku : ")
			if pilih2 == ("a"):
				system ("aircrack-ng")
			elif pilih2 == ("b"):
				system ("airmon-ng")
			elif pilih2 == ("c"):
				system ("airodump-ng")
			elif pilih2 == ("d"):
				system ("aireplay-ng")
			else:
				system ("exit")
			
			
	#instalasi
	def install():
		hias.pembatas()
		print ("1. Metasploit")
		print ("2. Nmap")
		print ("3. Aircrack-ng")
		pilih = int(input("Install Mana Bos Ku : "))
		if pilih == (1):
			termux.metas()
		elif pilih == (2):
			termux.nmap()
		elif pilih == (3):
			termux.Aircrack-ng()
		
hias.Jack()
#proses berjalan
print ("1. Install")
print ("2. Menjalankan Tools")
opsi = int(input("Masukan Pilihan Mu : "))
if opsi == (1):
	Proses.install()
elif opsi == (2):
	Proses.running()




