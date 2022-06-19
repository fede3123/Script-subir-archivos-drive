from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from time import sleep
import os

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


def uploade(route, id_folder):
    credentials = login()
    file = credentials.CreateFile({'parents': [{'kind': 'drivefilesname', 'id': id_folder}]})
    file['title'] = route.split('/')[-1]
    file.SetContentFile(route)
    file.Upload()

def returnValues(dict, find):
    for i, j in dict.items():
        if i == find:
            return j

dirsDrive = {
    'Aguaclara': '1uuEg0mSHVfjTfnqJTdrAJvKPBx6Pg33_',
    'Devora': '1fpjkX6RO5Hoh_ykMYB1E9Ye-RF67O0y-',
    'Antonia': '1QSJ2eg01b23xXrUuDTnvIhDKKTMmZTVr',
    'Pacifico': '1QH47Po7v_w9vfzQHZXDrJS0OV4PLMSM_',
    'Julia': '16evDklI5sAfrewWUF6XpCyNmeXvbuJI4',
    'SClara': '1ilWonQP63EgFdYN-DEMalefseHYvb8GD',
    'GMartinez': '1xwIni7c-a7cTW3D-vuhwg0uVTOkP6Gvd',
    'Mercantil': '14lWJvzmhYqgPZ4A2J3m9Obd60IvHbaVB',
    'SAntonio': '1H4lruEZ3mJMl_tyItbiYV5picOC1C2eg',
    'Marina': '13xnbh1waVhdyY0gVdGKedjGFCkKwtt9P',
    'Sagrado': '1EQj0iwNScHCUJwL8oWvnvCUWxDf0noj6',
    'Picacho': '1_emNkJYvyi-0oEQEKa9ij1-1cOQNPZ0j',
    'ASantos': '1aGO4PTSArWrt2aFfbDcJvHAxXCzm8aMM',
    'Iberia': '1JM0xneRufEO8k0yJ6ivN6cKkpYqB1icw',
    'CValle': '1EQj0iwNScHCUJwL8oWvnvCUWxDf0noj6',
    'Mateguadua': '1hvScWM85YzPTV_E9PPotQasTqug8LScl',
    'venus': '1-eMPbOg55Rg6psgk3iu4Zi5R8Dm1SEjQ',
    'SLorenzo': '1xI5HiNcdhQO7QlNS9cx2RoKmmIm02qKM',
    'JBeccerra': '1haS8RvsF51FplcNvvyDk98ajhvhTQ1H2',
    'UValle': '1JJrr5SPsKI0erMQLgnM5nlzy30G9yTaT',
    'JMaestro': '1qVqilpwEutTY5hNfS_78Ajpkw_AT3BiT',
    'OColonia': '1BIQUAimNg5j56eYFCvF-aWJDsGgWerua',
    'Censo': '1PhrlIPt5y-KL1ble-D4EJ2uv99kBE9SP',
    'Moralia': '11JonIVsYgPFQHWN7WNC7ToO3Te2hX7Ai',
    'Frazadas': '1hYt2Qgg4PacA9enqt4P1u0EKUkp_ZW9Q',
    'SRafael': '16vcYUpS5VBzWpBVwQjvLL8AT5KqCJY-i',
    'Diadema': '1vM1nHo57H7s3XGu-klaU7INGtPVEqtxh',
    'Monteloro': '1UUvlg9QlSPRKITgq34wVuVQjCWVXCdRy',
    'Jicaramata': '1wGV62apDzu8hPMl8jy1bbzFBNkC59G6M',
    'Retiro': '1FqnKhT3gx9n_qULxMG16744D8r-EVqMI',
    'Quebradagrande': '1gubKeBVEyFwyX7wITBNbG-03lPhk4zaU',
    'Tochecito': '1JcbzxVFU3koveRrZhbP7OsRG-ErwIa6p',
    'Barragan': '1XTTL8bDMei_-u6A2TgAY_QGaCz0XN9ZJ',
    'SLucia': '1weyl26Dv9P9XIsx9zxzBn0GbEy0Bp92w',
    'ANariño': '1SgBBVkIXgmNp9zGNC6SZWTSMcqaT_IuL',
    'JHormoza': '1Fuv7GoGiu4TdRqlSZa2hoycE6u_khcSA',
    'JCorral': '1GYL9_vWg3RZOztrEeI7J6M--ymtRbYsV',
    'Girardot': '1bQWnzfopZGastfjPl3899wUciYquHK-Z',
    'Travesuras': '1Cyaxy6DhPvgEHa21WHeGoAr-bXFndjLJ',
    'Campoalegre': '12RRDt9paSPPcPC8xvKpTPeIC8pr2XP5o',
    'Bocas': '1p-h9Q072lY9P8tRVsB0Pxjmx8mbA_2cF',
    'Cespedes': '1tvubvyDUkZgNZRLTrGpicB5fnw2-mlpS',
    'Occidente': '1GpKHj1EN3FWo3m2UiB6oQ3RQ6bLQOO6j',
    'Davalos': '1CKxrMN2a_GS2KY9EMwqGCSMVNFl169tI',
    'Nariño': '1z6AFqVCU_Fco5-0WixfYbm5hQjAtCZPP',
    'SCarlos': '1rJkFaYXRjrQVjEPnr6ldY0t9DO2W44lg',
    'Palmera': '1YCsvZVyTNXKF3xmnDxmWiu8gw8Z4NEJf',
    'Tresesquinas': '1sKH__hyel1cG4M2z3y2GHvkkYaNZvrFM',
    'Caimos': '18NiEihcPYhx421kAd1g7qrhpaKcB0tgB',
    'Gaitan': '1AewFGPiBg8M1cnfGJrjZw14BRqhI39NK',
    'Pumarejo': '1_5f2Tx3LhlbfPZD2zp2I2EzK8LrrW4r1',
    'Goretty': '1wrdO89wdJnJVibyHbmstC5TzhLLldoPu',
    'Moderna': '1F7GST4Qh0v34XpOyFqv86XQB8io31dMz',
    'AngelZ': '1v-Z0myWKgAaZTOCSGU6EJswmFsz28tIJ',
    'Carcel': '1c44w9KonW1KFRJErRN5JClHmMPQ4Zs6_',
    'Graciela': '1IV6s9h5x89x8FtYBVxKTchP62I_cQXHm'
}

# Create a dict with name and ids of dirs in drive CHECK
# Create func for upload files CHECK
# Create a func for delete all pictures CHECK
if __name__ == "__main__":
    path = "../../../Desktop/Segunda vuelta Petro/Fotos"
    # How many pictures have
    pictures = os.listdir(path)
    # Path dir
    pathDir = returnValues(dirsDrive, 'Aguaclara')
    for path,fichero,archivo in os.walk(path):
        for i in range(len(archivo)):
            pathA = f'{path}\{archivo[i]}'
            #Upload all things
            uploade(pathA, pathDir)

    for path,fichero,archivo in os.walk(path):
        for i in range(len(archivo)):
            pathA = f'{path}\{archivo[i]}'
            #Upload all things
            os.remove(pathA)
