from domaingen.domains import DomainGenerator

def test_get_domains_value() -> None:
    keywords = ["recipe","dinner","cooking"]
    tlds = ['com']
    #tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords,tlds)
    domains = domaingen.get_domains()
    assert "recipecooking.com" in domains 
    
def test_get_domains_set() -> list:
    keywords = ["recipe","dinner","cooking"]
    tlds = ['com']
    #tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords,tlds)
    domains = domaingen.get_domains()
    assert type(domains) is set
    