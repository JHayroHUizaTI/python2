import sys
from tabulate import tabulate 

clients = ['pablo','ricardo']

def create_client(client_name):
	global clients

	if client_name not in clients :
		clients.append(client_name)
	else:
		print ('Client already is in the client\'s list')

def list_clients():
    global clients
    if clients:
        print('Our Clients are :')
        show=[]
        for idx,name in enumerate(clients):
            show.append([idx+1,name])
        print(tabulate(show,headers=['N°','Name'],tablefmt='fancy_grid'))
    else:
        print(' I don´t have Clients in this moment')


def updated_client(client_name, updated_client_name):
	global clients


	if client_name in clients :
		index = clients.index(client_name)
		clients[index] = updated_name
	else:
		print ('Client is no it client\'s list')

def delete_client(client_name):
	global clients

	if client_name in clients:
		clients.remove(client_name)
	else:
		print('Client is not in client\'s list')

def search_client(client_name):

	for client in clients:
		if client != client_name:
			continue
		else:
			return True




def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today ? ')
	print('[C]reate client')
	print('[L]ist client')
	print('[U]pdated client')
	print('[D]elete client')
	print('[S]earch client')
 


def _get_client_name ():
	client_name = None

	while not client_name:
		client_name = str.lower(input('What is the client name ? '))

		if client_name == 'exit':
			client_name = None
			break

	if not client_name:
			sys.exit()

	return client_name

if __name__ == '__main__':

	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'L':
		list_clients()
	elif command == 'U':
		client_name = _get_client_name()
		updated_client_name = str.lower(input ('What is the updated client name ? '))
		updated_client(client_name, updated_client_name)
		list_clients()
	elif command == 'D':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found:
			print('The client is in the client\'s list')
		else:
			print('The client: {} is not in our client\'s list'.format(client_name))


	else:
		print ('Invalid command')