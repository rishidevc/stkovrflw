from __future__ import print_function
"""
{
CLIENT ID:
	699722485782-unamio1371bem4cjlqlp2a1muv7trist.apps.googleusercontent.com


CLIENT SECRET:
	v2jihBiqckyZhNozq32-6VK_
}
"""

"""
Shows basic usage of the Drive v3 API.

Creates a Drive v3 API service and prints the names and ids of the last 10 files
the user has access to.
"""

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))

# Call the Drive v3 API
results = service.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])
if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print('{0} ({1})'.format(item['name'], item['id']))