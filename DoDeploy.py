import digitalocean



api_token = input('Please enter your API token:')




def file():
    f = open("startup.txt","r")
    if f.mode == 'r':
        contents = f.read()
        return contents



droplet = digitalocean.Droplet(token=api_token,
                               name='Test',
                               region='nyc1',
                               image='ubuntu-14-04-x64',
                               size_slug='512mb',
                               user_data=file())

def ask():
    proxies = input("How many proxies?")
    for i in range (int(proxies)):    
        droplet.create()


ask()

