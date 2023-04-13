#from ftplib import FTP  
import ftplib
import shutil

ftp = ftplib.FTP("127.0.0.1")
ftp.login("myuser", "change_this_password")
#ftp.prot_p()
file = open("qwer.jpg", "rb")
ftp.storbinary("STOR 1234.jpg", file)
file.close()
ftp.close()

#shutil.move("keyz/1234.jpg", "..")

