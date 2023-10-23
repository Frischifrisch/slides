from ftplib import FTP
ftp = FTP('localhost')
ftp.login("foo", "bar")

print(ftp.retrlines('LIST'))

print('-------')
for f in ftp.nlst():
    print(f"file: {f}")

filename = 'ssh.py'

ftp.storlines(f"STOR {filename}", open(filename))

print('-------')
for f in ftp.nlst():
    print(f"file: {f}")

ftp.delete(filename)

print('-------')
for f in ftp.nlst():
    print(f"file: {f}")


 
