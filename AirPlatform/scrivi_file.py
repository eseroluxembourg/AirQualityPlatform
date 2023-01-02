import sys

nome_script, nome_file, contenuto = sys.argv


f = open("/home/pi/AirPlatform/" + nome_file, "w")
f.write(contenuto)
f.close()
     
