import digitalocean

api_token = input('Enter your API token:')
location = input('Enter where you want your proxies located[NY1 or NY2, SanFran1 or SanFran2, Amsterdam1 or Amsterdam2, Singapore, UK, Germany, Canada, Bangalore]:')
numOfProxies = input('Enter number of proxies you want to deploy:')

if location == 'NY1':
        locale = 'nyc1'
elif location == 'NY2':
        locale = 'nyc2'	
elif location == 'SanFran1':
        locale = 'sfo1'
elif location == 'SanFran2':
        locale = 'sfo2'
elif location == 'Amsterdam1':
        locale = 'ams2'
elif location == 'Amsterdam2':
        locale = 'ams3'
elif location == 'Singapore':
        locale = 'sgp1'
elif location == 'UK':
        locale = 'lon1'
elif location == 'Germany':
        locale = 'fra1'
elif location == 'Canada':
        locale = 'tor1'
elif location == 'Bangalore':
        locale = 'blr1'
        

f = open("startup.txt","r")
if f.mode == 'r':
    contents = f.read()
    

droplet = digitalocean.Droplet(token=api_token,
                               name='Test',
                               region=locale,
                               image='ubuntu-14-04-x64',
                               size_slug='512mb',
                               user_data=contents)
    
  
for i in range(int(numOfProxies)):
        droplet.create()
        continue
print('You just deployed ' + str(numOfProxies) + ' proxies.')

