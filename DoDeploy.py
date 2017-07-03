import digitalocean

api_token = input('Please enter your API token:')

def file():
    f = open("startup.txt","r")
    if f.mode == 'r':
        contents = f.read()
        return contents

droplet = digitalocean.Droplet(token=api_token,
                               name='Test',#name whatever
                               region='nyc1',#set to nyc1,nyc3,sfo1,sfo2,ams2,ams3,sgp1,lon1,fra1,tor1, or blr1
                               image='ubuntu-14-04-x64',
                               size_slug='512mb',
                               user_data=file())

def ask():
    proxies = input("How many proxies?")
    for i in range (int(proxies)):    
        droplet.create()
        continue
    print('You just deployed ' + str(proxies) + ' proxies.')
        
ask()
