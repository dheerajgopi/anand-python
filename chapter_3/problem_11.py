import zipfile

def zip_files(zip_name, *files):
    z = zipfile.ZipFile(zip_name, "w")
    for file_name in files:
        z.write(file_name)
    z.close()


zip_files('abc.zip', 'zipfile1.txt', 'zipfile2.txt')
