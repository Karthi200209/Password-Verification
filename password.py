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
