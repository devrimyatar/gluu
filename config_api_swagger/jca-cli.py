import readline
import time
import sys
import os
import json
import ruamel.yaml
import requests
from pprint import pprint
from functools import partial
from urllib3.exceptions import InsecureRequestWarning

import swagger_client


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

clear = lambda: os.system('clear')


class Menu(object):

    def __init__(self, name, method='', info=''):
        self.name = name
        self.method = method
        self.info = info
        self.children = []
        self.parent = None
    
    def __iter__(self):
        self.current_index = 0
        return self
    
    def __repr__(self):
        return self.name
        self.__print_child(self)

    def tree(self):
        print(self.name)
        self.__print_child(self)

    def __get_parent_number(self, child):
        n = 0
        while True:
            if not child.parent:
                break
            n += 1
            child = child.parent

        return n
    
    def __print_child(self, menu):
        if menu.children:
            for child in menu.children:
                print(' ' * self.__get_parent_number(child)*2, child)
                self.__print_child(child)

    def add_child(self, node):
        assert isinstance(node, Menu)
        node.parent = self
        self.children.append(node)

    def get_child(self, n):
        if len(self.children) > n:
            return self.children[n]

    def __next__(self):
        if self.current_index < len(self.children):
            retVal = self.children[self.current_index]
            self.current_index += 1
            return retVal
            
        else:
            raise StopIteration

    def __contains__(self, child):
        for child_ in self.children:
            if child_.name == child:
                return True
        return False

class JCA_CLI:

    def __init__(self):
        self.host = 'c2.gluu.org'
        self.client_id = 'client_id'
        self.client_secret = 'client_secret'
        
        
        self.swagger_configuration = swagger_client.Configuration()
        self.swagger_configuration.host = 'https://{}'.format(self.host)
        
        self.swagger_configuration.verify_ssl = False
        self.swagger_configuration.debug = False
        if self.swagger_configuration.debug:
            configuration.logger_file='swagger.log'

        self.swagger_yaml_fn = 'myswagger.yaml'
        self.cfg_yml = self.get_yaml()
        self.make_menu()
        self.current_menu = self.menu
    
    
    def get_yaml(self):

        with open(self.swagger_yaml_fn) as f:
            cfg_yml = ruamel.yaml.load(f.read(), ruamel.yaml.RoundTripLoader)
        
        return cfg_yml


    def make_menu(self):

        menu = Menu('Main Menu')
        
        for tag in self.cfg_yml['tags']:
            if tag['name'] != 'developers':
                m = Menu(name=tag['name'])
                menu.add_child(m)
                for path in self.cfg_yml['paths']:
                    for method in self.cfg_yml['paths'][path]:
                        if 'tags' in self.cfg_yml['paths'][path][method] and m.name in self.cfg_yml['paths'][path][method]['tags'] and 'operationId' in self.cfg_yml['paths'][path][method]:
                            sm = Menu(
                                    name=self.cfg_yml['paths'][path][method]['summary'].strip('.'),
                                    method=method,
                                    info=self.cfg_yml['paths'][path][method]
                                    )
                            m.add_child(sm)
        self.menu = menu


    def get_access_token(self, scope):
        print("Getting access token for scope", scope)
        req = requests.post(
                        'https://{}/jans-auth/restv1/token'.format(self.host),
                        auth=(self.client_id, self.client_secret),
                        data={
                            'grant_type': 'client_credentials', 
                            'scope': scope
                            },
                        verify=False
                    )

        try:
            result = req.json()
            if 'access_token' in result:
                self.swagger_configuration.access_token = result['access_token']
            else:
                print("Error while getting access token")
                print(result)
        except:
            print("Error while getting access token")
            print(req.text)
        


    def check_type(self, val, vtype):
        if vtype == 'string':
            return str(val)
        elif vtype == 'integer':
            if isinstance(val, int):
                return val
            if val.isnumeric():
                return int(val)
                
        raise TypeError("Please enter a(n) {} value".format(vtype))

    def get_input(self, values=[], text='Selection', default=None, itype=None):

        if default:
            text += ' [{}]'.format(default)
            if itype=='integer':
                default=int(default)
        text += ': '

        while True:
            selection = input(text)
            selection = selection.strip()

            if default and not selection:
                selection = default
            
            if not itype is None:
                try:
                    selection = self.check_type(selection, itype)
                    break
                except TypeError as e:
                    print(e)

            if values:
                if selection in values:
                    break
                else:
                    print('Invalid Choice. Please enter one of ', ', '.join(values))

            if not values and not selection:
                break

        if 'q' in values and selection == 'q':
            print("Quiting...")
            sys.exit()

        if selection == '_null':
            selection = None
        elif selection == '_q':
            selection = 'q'

        return selection

    def print_underlined(self, text):
        print()
        print(text)
        print('-' * len(text.splitlines()[-1]))


    def obtain_parameters(self, endpoint):
        parameters = {}
        if 'parameters' in endpoint.info:
            for param in endpoint.info['parameters']:
                parameters[param['name']] = self.get_input(
                            text=param['description'].strip('.'), 
                            itype=param['schema']['type'],
                            default = param['schema'].get('default')
                            )

        return parameters

    def get_api_class_name(self, name):
        namle_list = name.replace('-','').split()
        for i, w in enumerate(namle_list[:]):
            if len(w) > 1:
                w = w[0].upper()+w[1:]
            else:
                w = w.upper()
            
            namle_list[i] = w

        return ''.join(namle_list)+'Api'


    def unmap_model(self, model):
        data_unmaped = {}
        data = model.to_dict()

        for key_ in data:
            data_unmaped[model.attribute_map[key_]] = data[key_]

        return data_unmaped

    def process_get(self, endpoint):
        clear()
        title = endpoint.name
        if endpoint.name != endpoint.info['description'].strip('.'):
            title += '\n' + endpoint.info['description']

        self.print_underlined(title)

        client = getattr(swagger_client, self.get_api_class_name(endpoint.parent.name))

        api_instance = client(swagger_client.ApiClient(self.swagger_configuration))

        for security_ in endpoint.info['security']:
            if 'jans-auth' in security_:
                security = security_['jans-auth'][0]
                break

        parameters = self.obtain_parameters(endpoint)
        for param in parameters.copy():
            if not parameters[param]:
                del parameters[param]
        
        self.get_access_token(security)

        if parameters:
            print("Calling Api with parameters:", parameters)

        print("Please wait while retreiving data ...\n")

        api_caller = getattr(api_instance, endpoint.info['operationId'].replace('-','_'))

        #api_response = api_caller(type=type, limit=limit, pattern=pattern)
        api_response = api_caller(**parameters)

        api_response_unmapped = []
        for model in api_response:
            api_response_unmapped.append(self.unmap_model(model))

        print()
        print(json.dumps(api_response_unmapped, indent=2))

        while True:
            selection = self.get_input(['q', 'b', 'w', 'r'])
            if selection == 'b':
                self.display_menu(endpoint.parent)
                break
            elif selection == 'r':
                self.process_get(endpoint)
            elif selection == 'w':
                fn = input('File name: ')
                try:
                    with open(fn, 'w') as w:
                        json.dump(api_response_unmapped, w, indent=2)
                        print("Output was written to", fn)
                except Exception as e:
                    print("An error ocurred while saving data")
                    print(e)

    def process_post(self, endpoint):
        print("GET mehod for '{}' is not implemented yet".format(endpoint))
        selection = self.get_input(['b'])
        if selection == 'b':
            self.display_menu(endpoint.parent)
            
    def process_delete(self, endpoint):
        print("GET mehod for '{}' is not implemented yet".format(endpoint))
        
        selection = self.get_input(['b'])
        if selection == 'b':
            self.display_menu(endpoint.parent)

    def process_patch(self, endpoint):
        print("GET mehod for '{}' is not implemented yet".format(endpoint))
        
        selection = self.get_input(['b'])
        if selection == 'b':
            self.display_menu(endpoint.parent)

    def process_put(self, endpoint):
        print("GET mehod for '{}' is not implemented yet".format(endpoint))
        
        selection = self.get_input(['b'])
        if selection == 'b':
            self.display_menu(endpoint.parent)


    def display_menu(self, menu):
        clear()
        self.current_menu = menu

        self.print_underlined(menu.name)

        selection_values = ['q', 'b']

        for i, item in enumerate(menu):
            print(i+1, item)
            selection_values.append(str(i+1))
        
        selection = self.get_input(selection_values)

        if selection == 'b' and not menu.parent:
            print("Quiting...")
            sys.exit()
        elif selection == 'b':
            self.display_menu(menu.parent)
        elif menu.get_child(int(selection) -1).children:
            self.display_menu(menu.get_child(int(selection) -1))
        else:
            m = menu.get_child(int(selection) -1)
            #endpoint = self.get_endpoint(m)
            getattr(self, 'process_' + m.method)(m)


    def runApp(self):
        clear()
        self.display_menu(self.menu)
            

cliObject = JCA_CLI()
cliObject.runApp()


