<<<<<<< HEAD
import getpass
database={"karthi":"2002",
          "keyan":"2003"}
username=input("Enter Your Username :")
password=getpass.getpass("Enter Your Password:")
for i in database.keys():
    if username==1:
        while password!=database.get(i):
            password=getpass.getpass("Enter Password Again:")
        break
print("Verified")
=======
import getpass
database={"karthi.keyan":"123456",
          "keyan.karthi":"654321"}
username=input("Enter Your Username :")
password=getpass.getpass("Enter Your Password:")
for i in database.keys():
    if username==1:
        while password!=database.get(i):
            password=getpass.getpass("Enter Password Again:")
        break
print("Verified")
>>>>>>> af20b6da9f682efbacf020d7bb9f9c33324d38b2
