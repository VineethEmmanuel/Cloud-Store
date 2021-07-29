import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

           
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                   
                local_path = os.path.join(root, filename)

                   
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A1h5ofJ71ol8WGOrN68M1c6_3-YcqJoK8dL3jQnMFE4L6XJKkAA0hnQ-IEKkXPeUw8v55JJcgDEXd4JZs7A5NMdndIvc9hqUkniTLwt0Tsn928F_bErnyTq2NlKAITcPRsxItkDo'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the path of the file to be transferred: "))
    file_to = input("enter the folder in dropbox where the file should be uploaded ")  

    transferData.upload_file(file_from,file_to)
    print("file is now uploaded to dropbox! Enjoy :)")

main()