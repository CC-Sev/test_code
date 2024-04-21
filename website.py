import re

domains = (
    'www.google.com',
    'www.youtube.com',
    'www.instagram.com',
    'https://www.twitch.tv',
    'https://www.ucr.com',
    'https://www.linkedin.com',
    'www.wikipedia.org'
)

def lstrip_funct():
    for i in range(len(domains)):
        domain = (domains[i])
        domain = domain.lstrip('https://')
        print(domain)
# lstrip_funct()

def parse_funct():
    for i in range(len(domains)):
        domain = domains[i].split('www.')
        print(domain[1])
#parse_funct()    


def sub_funct():
    for i in range(len(domains)):
        domain = domains[i]
        domain = re.sub(r'www.', '', domain)
        domain = re.sub(r'https://', '', domain)
        print(domain)
sub_funct()