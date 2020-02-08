import os

### List files from path
print('### List files from path')
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myFiles:
    print(os.path.join('usr', 'bin', 'spam', filename))

### current folder
print('### current folder')
print(os.getcwd())

### creating folders
print('### creating folders')
os.makedirs('/home/carlos/testei/testei1/teste2')

# clean folders from example
print('# clean folders from example')
os.rmdir('/home/carlos/testei/testei1/teste2')
os.rmdir('/home/carlos/testei/testei1')
os.rmdir('/home/carlos/testei')

### split dir from basename
print('### split dir from basename')
calcFilePath = '/Windows/System32/calc.exe'
print(os.path.split(calcFilePath))

# tuple dir and basename
print('# tuple dir and basename')
print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))

# split dir
print('# split dir')
print('/usr/bin'.split(os.path.sep))

### file size
print('### file size')
print('timedatectl file size '+str(os.path.getsize('/usr/bin/timedatectl')))

### lists dir
print('### lists dir')
print(os.listdir('/usr/src'))

## total size
print('## total size')
totalSize = 0
for filename in os.listdir('/usr/src'):
    totalSize = totalSize + os.path.getsize(os.path.join('/usr/src', filename))

print(totalSize)
