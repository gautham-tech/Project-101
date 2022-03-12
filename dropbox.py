import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BCcicOYFi1pHcGIAT08wcj3fd082uIEasjzFy0yrhk3gm0XTCDM_I_ck4VB8ONsYQOFlgZNPaaikpWDd7k5xmmJhvs2GXdhu6ixE34sGRVyDluW75Ge16_dwjuyybC8oybGA_Tc'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to be transfered: ")
    file_to = input("Enter the full path to upload to Dropbox: ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

if __name__ == '__main__':
    main()