"""
Author: Theo Bernier
"""
from __future__ import print_function
import pickle
import os.path
import utils.path_config as pc
import mimetypes
import io
from pathlib import Path
from datetime import datetime, timedelta
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
        auth_path=pc.get_auth_path()
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        pickle_path = auth_path.joinpath('token.pickle')
        if pickle_path.exists():
            with open(pickle_path, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    auth_path.joinpath('credentials.json'), self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        service = build('drive', 'v3', credentials=creds)
    def refresh_token(self):
        auth_path = pc.get_auth_path()
        pickle_path = auth_path.joinpath('token.pickle')
        if pickle_path.exists():
            with open(pickle_path, 'rb') as token:
                creds = pickle.load(token)
            if creds and creds.refresh_token:
                creds.refresh(Request())
            else:
                raise Warning("couldn't refresh token!")
        else:
            raise FileExistsError("file 'token.pickle' does not exist, token couldn't be refreshed")
        self.creds = creds

    def list_files(self, pageSize = 10):
        results = self.service.files().list(
            pageSize=pageSize, fields="nextPageToken, files(id, name)").execute()
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

    def get_file_id(self, filename):
        results = self.service.files().list(
            pageSize=1000, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        matches = []
        for item in items:
            if item['name'] == filename:
                matches.append(item['id'])

        return matches


    def download_latest_file(self, filename, destination, days_back=5):
        """
        In Drive, files are named according to "name_year-month-day.extension" at which they were uploaded
        Provide filename as name.extension and this function will automatically download the newest version checking
        back a certain number of days.
        :param filename: filename without date! e.g. RKI_Corona_Landkreise_updated.csv
        :param destination: destination path for downloaded file
        :param days_back: how many days should be checked back into past for latest version

        """
        #path = Path(filename)
        name, extension = os.path.splitext(filename)
        found = False
        # str repr of today's date, precise to the day
        day = datetime.today()
        day_str = day.__str__()[:10]
        day_limit = day - timedelta(days=days_back+1)
        while not found and day > day_limit:
            filename_w_date = name+"_"+day_str+extension
            print(filename_w_date)
            ID = self.get_file_id(filename_w_date)
            if len(ID)==1:
                print("match found for file %s at date %s" % (name, day_str))
                self.download_file(ID[0], destination)
                found = True
            elif len(ID)>1:
                lastID = id[-1]
                print(
                    "Several name matches found with that filename for date %s, taking last id of the list: %s" % (day.__str()[:10], lastID)
                    )
                self.download_file(lastID, destination)
                found = True
            else:
                print("no match found for date %s, checking previous day..." % day_str)
                day = day - timedelta(days=1)
                day_str = day.__str__()[:10]

        if not found:
            print("No match found within %s days of today. Go back further or check filename" % days_back)


    def download_file(self, file_id, download_destination):
        request = self.service.files().get_media(fileId=file_id)
        with open(download_destination, "wb") as fh:
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

    landkreise = pc.get_RKI_landkreise_file()
    landkreiseName = landkreise.name
    drive = Drive()
    # Commented out because given as usage example
    # drive.upload_file(service, path, filename, mimetype)
    # drive.download_latest_file(landkreiseName, landkreise)
    drive.list_files(pageSize = 10) #print list of first 10 files