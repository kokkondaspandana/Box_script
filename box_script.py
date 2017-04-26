from __future__ import print_function, unicode_literals
import os
from boxsdk import Client
from boxsdk.exception import BoxAPIException
from boxsdk.object.collaboration import CollaborationRole
from auth import authenticate



def upload_file(client):
    root_folder = client.folder(folder_id='0')
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'file.txt')
    a_file = root_folder.upload(file_path, file_name='i-am-a-file.txt')
    try:
        print('{0} uploaded: '.format(a_file.get()['name']))
	print(a_file.get()['id'])
	temp = client.file(file_id=a_file.get()['id']).content()
	with open("Output.txt", "w") as text_file:
    		text_file.write(temp)
        
    finally:
        print('Delete i-am-a-file.txt succeeded:')


def run_examples(oauth):

    client = Client(oauth)

    
    upload_file(client)
    

def main():
	oauth, _, _ = authenticate()
        run_examples(oauth)
        os._exit(0)

if __name__ == '__main__':
    main()
