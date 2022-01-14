import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f =  open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A_5ySV1hxWi-QMGvXuwbXfFkHG-QJGfPmnn0X7SD_opirPlC8dP5prbrh6bp4n507_ZzWMdQIiGyqCQABe8U1HqIvERdHh4WcWPa6syUNEaLOxn43J_xjOdV5sa9rCcHVMP8j8c'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer :")
    file_to = input("Enter the full path to upload to dropbox :")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")


main()
    