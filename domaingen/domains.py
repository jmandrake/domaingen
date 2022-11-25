
from itertools import combinations
import zipfile
import json
import whois
import threading
#install_requires=['python-whois', 'py-thesaurus', 'random-proxies'],
#https://pypi.org/project/py-thesaurus/
#https://pypi.org/project/random-proxies/

class DomainGenerator:

    def __init__(self, domain_keywords, tlds=["com"]):
        self.__domain_keywords = domain_keywords # Input: list of domains
        self.__tlds = tlds
                
    def get_domains(self, domain_keywords=None):
        domains = set()
        if domain_keywords is None:
            domain_keywords = self.__domain_keywords
        for tld in self.__tlds:
            for i in range(2,len(domain_keywords)):
                for j in combinations(domain_keywords,i):
                    domains.add(''.join(j) + '.' + tld)
        return domains
        
    def get_synonym_domains(self):
        self.__synonym_domain_keywords = set()
        jdict = dict() # Load the thesaurus from zip json file        
        with zipfile.ZipFile('eng_synonyms.json.zip') as myzip:
            jc = myzip.open('eng_synonyms.json')
            jdict = json.load(jc)
        for k in self.__domain_keywords:
            #print(jdict[k])
            if jdict:
                self.__synonym_domain_keywords.add(jdict[k].pop(0).replace(' ',''))
        return self.get_domains(self.__synonym_domain_keywords)


def main():
    keywords = ["recipe","dinner","cooking","best"]
    tlds = ['com']
    #tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords,tlds)
    
    domains = domaingen.get_domains()
    for domain in domains:
        print(domain)
    
    domains = domaingen.get_synonym_domains()
    for domain in domains:
        print(domain)
    
if __name__=="__main__":
    main()