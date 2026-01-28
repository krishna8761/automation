#r = open("C:/Users/ks392/OneDrive/Desktop/New folder/automation/C:/Users/ks392/OneDrive/Desktop/New folder/automation/names.txt")

#print(r.read())
#print(r.readline())
#print(r.readline())

#close the file everytime when you open it 
#r.close()

#now if file doesnt exist so you need to try and exception
#try:
 #   r = open("games.txt")
  #  print(r.read())
#except:
 #   print("file do not exist")
#finally:        
 #   r.close()



#apeend is use to edit or create file
f = open("C:/Users/ks392/OneDrive/Desktop/New folder/automation/names.txt" , "a")
f.write("thor\n")
f.close()

f = open("C:/Users/ks392/OneDrive/Desktop/New folder/automation/names.txt")
print(f.read())
f.close()