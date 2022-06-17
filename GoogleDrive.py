from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

dir_credential = 'credentials_module.json'


def login():
    gaut = GoogleAuth()
    gaut.LoadCredentialsFile(dir_credential)
    # Refresh login
    if gaut.access_token_expired:
        gaut.Refresh()
        gaut.SaveCredentials(dir_credential)
    # Login
    else:
        gaut.Authorize()
    return GoogleDrive(gaut)


def upload(route, id_folder):
    credentials = login()
    file = credentials.CreateFile({'parents': [{'kind': 'drivefilesname', 'id': id_folder}]})
    file['title'] = route.split('/')[-1]
    file.SetContentFile(route)
    file.Upload()
