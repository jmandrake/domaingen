[![Test](https://github.com/jmandrake/domaingen/actions/workflows/ci.yml/badge.svg)](https://github.com/jmandrake/domaingen/actions/workflows/ci.yml)

# domaingen

Generate domain names from a list of keywords.
Checks domain availability using the Namecheap API.
You can also use a thesaurus to search for alternative keywords and domains.

## Setup

1) Enable API access in your Namecheap account:
https://www.namecheap.com/support/api/intro/

2) Create a file to store the API key and info needed to use the Namecheap API:
Save the file as api_key.json

{
    "api_user": "yournamecheapusername",
    "api_key": "namecheapAPIkey",
    "api_ip": "111.111.111.111"
}

3) Whitelist your IP address in the Namecheap API interface.

4) See sample code below on how to use this package.


## Examples of How To use the DaomainGenerator class to get available domains

Create a domaingen object and input keywords

```python

from domaingen.domains import DomainGenerator

keywords = ["recipe","dinner","cooking","spices","food"] # List of keywords
tlds = ['com'] # List of top level domain extensions (optional, default is com)

domaingen = DomainGenerator(keywords,tlds)
domains = domaingen.get_keyword_combinations(keywords)
available_domains = domaingen.check_domains(domains)
print("Available domains: " + str(len(available_domains)))
for domain in domains:
    print(domain)

```

## How to use the thesaurus function to get available domains

```python

from domaingen.domains import DomainGenerator

keywords = ["recipe","dinner","cooking","spices","food"] # List of keywords
tlds = ['com'] # List of top level domain extensions (optional, default is com)

domaingen = DomainGenerator(keywords,tlds)
domains = domaingen.get_synonym_domains(keywords)
available_domains = domaingen.check_domains(domains)
print("Available domains: " + str(len(available_domains)))
for domain in domains:
    print(domain)
```


## Sample XML response from Namecheap API
```
<?xml version="1.0" encoding="utf-8"?>
<ApiResponse Status="OK" xmlns="http://api.namecheap.com/xml.response">
  <Errors />
  <Warnings />
  <RequestedCommand>namecheap.domains.check</RequestedCommand>
  <CommandResponse Type="namecheap.domains.check">
    <DomainCheckResult Domain="spicesfood.com" Available="false" ErrorNo="0" Description="" IsPremiumName="false" PremiumRegistrationPrice="0" PremiumRenewalPrice="0" PremiumRestorePrice="0" PremiumTransferPrice="0" IcannFee="0" EapFee="0.0" />
    <DomainCheckResult Domain="cookingfood.com" Available="false" ErrorNo="0" Description="" IsPremiumName="false" PremiumRegistrationPrice="0" PremiumRenewalPrice="0" PremiumRestorePrice="0" PremiumTransferPrice="0" IcannFee="0" EapFee="0.0" />
    <DomainCheckResult Domain="dinnercookingspices.com" Available="true" ErrorNo="0" Description="" IsPremiumName="false" PremiumRegistrationPrice="0" PremiumRenewalPrice="0" PremiumRestorePrice="0" PremiumTransferPrice="0" IcannFee="0" EapFee="0.0" />
    <DomainCheckResult Domain="recipespicesfood.com" Available="true" ErrorNo="0" Description="" IsPremiumName="false" PremiumRegistrationPrice="0" PremiumRenewalPrice="0" PremiumRestorePrice="0" PremiumTransferPrice="0" IcannFee="0" EapFee="0.0" />
  </CommandResponse>
  <Server>PHX01APIEXT02</Server>
  <GMTTimeDifference>--5:00</GMTTimeDifference>
  <ExecutionTime>0.318</ExecutionTime>
</ApiResponse>
```

## Sample XML response from API if the IP is not whitelisted

For more information on how to whitelist your IP:
https://www.namecheap.com/support/api/intro/
```
<?xml version="1.0" encoding="utf-8"?>
<ApiResponse Status="ERROR" xmlns="http://api.namecheap.com/xml.response">
  <Errors>
    <Error Number="1011150">Invalid request IP: 34.125.101.153</Error>
  </Errors>
  <Warnings />
  <RequestedCommand />
  <Server>PHX01APIEXT02</Server>
  <GMTTimeDifference>--5:00</GMTTimeDifference>
  <ExecutionTime>0</ExecutionTime>
</ApiResponse>
```

## Thesaurus (English)
This is a json dataset of synonyms for english words.
Source:
https://www.kaggle.com/datasets/behcetsenturk/englishengen-synonyms-json-thesaurus
