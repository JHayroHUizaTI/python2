from re import U
import sys


class Client():

    def __init__(self, client_name: str = None, client_company: str = None, client_email: str = None, client_position: str = None):
        self.name = client_name
        self.company = client_company
        self.email = client_email
        self.position = client_position

    def _set_name(self, client_name):
        client_name =_get_client_attribute('name',client_name)
        self.name=client_name

    def _set_company(self, client_company):
        client_company =_get_client_attribute('company',client_company)
        self.company = client_company

    def _set_email(self, client_email):
        client_email =_get_client_attribute('email',client_email)
        self.email = client_email

    def _set_position(self, client_position):
        client_position =_get_client_attribute('position',client_position)
        self.position = client_position


clients = []
clients.append(Client('Manuel','TecM','manuel@tecm.edu','Mprofessor'))
clients.append(Client('Briones','TecB','briones@tecb.edu','Bprofessor'))

def create_client(client_name):
    global clients
    
    found,client_f,idx = search_client(client_name)
    if not found:
        new_client=Client()
        new_client._set_name(client_name)
        new_client._set_company(None)
        new_client._set_email(None)
        new_client._set_position(None)
        clients.append(new_client)
    else:
        _client_exists(client_f.name)

def list_clients(to_print: bool = True):
    global clients
    for idx, client in enumerate(clients):
        print(f'El cliente {idx} es {client.name}, trabaja en {client.company} como {client.position}')

def delete_client(client_name):
    global clients
    found,client_f,idx = search_client(client_name)
    if found:
        clients.pop(idx)
    else:
        _client_doesnt_exists(client_name)


def update_client(client_name, new_client_name,new_client_company,new_client_email,new_client_position):
    global clients
    found,client_f,idx = search_client(client_name)
    if found:
        if new_client_name != 'Nc':
            clients[idx]._set_name(new_client_name)
        if new_client_company != 'Nc':
            clients[idx]._set_company(new_client_company)
        if new_client_email != 'Nc':
            clients[idx]._set_email(new_client_email)
        if new_client_position != 'Nc':
            clients[idx]._set_position(new_client_position)
    else:
        _client_doesnt_exists(client_name)


def search_client(client_name):
    global clients
    found = False
    for idx,client in enumerate(clients):
        if client_name == client.name:
            found = True
            return found, client,idx
        else:
            continue
    return found, None,None

def _get_client_attribute(attribute, client_attribute: str = None):
    while not client_attribute:
        client_attribute = input(f'Client {attribute}: ').lower().title()
        if client_attribute == 'exit':
            client_attribute = None
            break
    if not client_attribute:
        sys.exit()

    return(client_attribute)


def _client_exists(client_name):
    return print(f'{client_name} is in client\'s list')

def _client_doesnt_exists(client_name):
    return print(f'{client_name} is not in client\'s list')


def _print_welcome():
    print('Welcome to Platzi Ventas')
    print('*'*50)
    print('What would you like to do today? ')
    print('[C]reate client ')
    print('[D]elete client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[S]earch client')


def main():
    _print_welcome()
    command = input().lower()

    if command == 'l':
        pass
    else:
        client_name=_get_client_attribute('name')
        if command == 'c':
            create_client(client_name)
        elif command == 'd':
            delete_client(client_name)
        elif command == 'u':
            print('\'Nc\' for no change')
            new_client_name = _get_client_attribute('new name')
            new_client_company = _get_client_attribute('new company')
            new_client_email = _get_client_attribute('new email')
            new_client_position = _get_client_attribute('new position')
            update_client(client_name, new_client_name,new_client_company,new_client_email,new_client_position)
        elif command == 's':
            found = search_client(client_name)
            if isinstance(found,int):
                _client_exists(client_name)
            else:
                _client_doesnt_exists(client_name)
    list_clients()


    

if __name__ == '__main__':
    main()