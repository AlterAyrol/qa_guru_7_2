import zipfile


with zipfile.ZipFile('tests/resources/hello.zip') as hellozip:
    hellozip.extract('Hello.txt')
    print(hellozip.namelist())
    text = hellozip.read('Hello.txt')
    print(text)