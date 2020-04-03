from __future__ import print_function
import pickle
import os.path
import utils.path_config as pc
import mimetypes
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload, MediaIoBaseDownload


class Drive():
    def __init__(self):
        self.refresh_token()
        self.service = build('drive', 'v3', credentials=self.creds)
        self.SCOPES = ['https://www.googleapis.com/auth/drive']

    def fetch_token(self):
        """Shows basic usage of the Drive v3 API.
            Prints the names and ids of the first 10 files the user has access to.
            """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        service = build('drive', 'v3', credentials=creds)
    def refresh_token(self):
        try:
            os.path.exists('auth/token.pickle')
            with open('auth/token.pickle', 'rb') as token:
                creds = pickle.load(token)
            if creds and creds.refresh_token:
                creds.refresh(Request())
            else:
                raise Warning("couldn't refresh token!")
        except:
            raise FileExistsError("file 'token.pickle' does not exist, token couldn't be refreshed")
        self.creds = creds

    def list_files(self):
        results = self.service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        return items

    def upload_file(self, service, path, filename, mimetype):
        file_metadata = {'name': filename}
        media = MediaFileUpload(path,
                                mimetype=mimetype,
                                resumable=True, )
        file = service.files().create(body=file_metadata,
                                      media_body=media,
                                      fields='id').execute()
        print('uploaded file with File ID: %s' % file.get('id'))

    def download_file(self,):
        file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print
            "Download %d%%." % int(status.progress() * 100)

if __name__=="__main__":
    drive = Drive()
    path = pc.get_RKI_landkreise_file()
    filename = path.name
    mimetype, encoding = mimetypes.guess_type(path)
    #drive.upload_file(service, path, filename, mimetype)
    drive.list_files()