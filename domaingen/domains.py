from itertools import combinations
import zipfile
import json
import os
import requests


class DomainGenerator:
    def __init__(self, domain_keywords: list[str], tlds: list[str] = ["com"]):
        self.__domain_keywords = domain_keywords  # Input: list of domains
        self.__tlds = tlds

    def get_keyword_combinations(self, new_keywords: list[str] = None) -> list[str]:
        """function to generate all possible keyword combinations from a list of keywords
        with a maximum of 3 keywords, non-repeating keywords, and non-repeating
        combinations of keywords. If the list contains 6 keywords, the function will
        return 15 two-word combinations, and 20 three-word combinations.
        No repeating keywords."""
        domains = set()
        domain_keywords = self.__domain_keywords
        if new_keywords:
            domain_keywords = new_keywords
        for tld in self.__tlds:
            for i in range(2, len(domain_keywords) + 1):
                for j in combinations(domain_keywords, i):
                    domains.add("".join(j) + "." + tld)
        return list(domains)

    def check_domains(self, domains: list[str]) -> list[str]:
        """Check if domains are available for registration using Namecheap API.
        Return a list of available domains."""
        api_info = dict()
        # if file exists, load it
        if os.path.isfile("api_key.json"):
            with open("api_key.json", "r") as f:
                api_info = json.load(f)
        if len(api_info.keys()) < 3:

            api_info["api_user"] = input("Enter your Namecheap API username: ")
            api_info["api_key"] = input("Enter your Namecheap API key: ")
            api_info["api_ip"] = input("Enter your IP address: ")

        if len(api_info.keys()) == 3:
            if api_info["api_user"] and api_info["api_key"] and api_info["api_ip"]:
                # open API URL to fetch available domains
                response = requests.get(
                    f"https://api.namecheap.com/xml.response?ApiUser={api_info['api_user']}\
                        &ApiKey={api_info['api_key']}&UserName={api_info['api_user']}\
                        &Command=namecheap.domains.check&ClientIp={api_info['api_ip']}\
                        &DomainList={','.join(domains)}",
                    timeout=10,
                )
                # parse XML response
                xml = response.text
                print(xml)
                # extract available domains
                available_domains = []
                for i in range(len(domains)):
                    if xml.find(f'Domain="{domains[i]}" Available="true"') > 0:
                        available_domains.append(domains[i])

                return available_domains
        else:
            print("Error: API info not found.")
        return []

    def get_synonym_domains(self):
        self.__synonym_domain_keywords = set()
        jdict = dict()  # Load the thesaurus from zip json file
        with zipfile.ZipFile("eng_synonyms.json.zip") as myzip:
            jc = myzip.open("eng_synonyms.json")
            jdict = json.load(jc)
        for k in self.__domain_keywords:
            # print(jdict[k])
            if jdict:
                self.__synonym_domain_keywords.add(jdict[k].pop(0).replace(" ", ""))
        return self.get_keyword_combinations(self.__synonym_domain_keywords)


def main():
    # Test the DomainGenerator class with dummy keywords
    keywords = ["recipe", "dinner", "cooking", "spices", "food"]
    tlds = ["com"]
    # tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords, tlds)

    domains = domaingen.get_keyword_combinations(keywords)
    # for domain in domains:
    #     print(domain)

    available_domains = domaingen.check_domains(domains)
    print("Available domains: " + str(len(available_domains)))
    for domain in domains:
        print(domain)

    return available_domains


if __name__ == "__main__":
    main()
