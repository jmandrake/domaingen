from domaingen.domains import DomainGenerator
"""
pytest

"""

def test_get_domains_value() -> None:
    keywords = ["recipe","dinner","cooking"]
    tlds = ['com']
    #tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords,tlds)
    domains = domaingen.get_domains()
    assert "recipecooking.com" in domains 
    
def test_get_domains_set() -> None:
    keywords = ["recipe","dinner","cooking"]
    tlds = ['com']
    #tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords,tlds)
    domains = domaingen.get_domains()
    assert type(domains) is set
    
    
def test_get_synonym_domains_value() -> None:
    keywords = ["recipe","dinner","cooking"]
    tlds = ['com']
    #tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords,tlds)
    domains = domaingen.get_synonym_domains()
    assert "cookeryformula.com" in domains 
    
def test_get_synonym_domains_set() -> None:
    keywords = ["recipe","dinner","cooking"]
    tlds = ['com']
    #tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords,tlds)
    domains = domaingen.get_synonym_domains()
    assert type(domains) is set