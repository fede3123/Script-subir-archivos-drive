from pydrive2.auth import GoogleAuth

#yaml save all auth for just did a one time
if __name__ == '__main__':
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
