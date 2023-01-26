from domaingen.domains import DomainGenerator


# def test_get_domains_value() -> None:
#     keywords = ["recipe", "dinner", "cooking"]
#     tlds = ["com"]
#     # tlds = ['com','net', 'org']
#     domaingen = DomainGenerator(keywords, tlds)
#     domains = domaingen.get_keyword_combinations()
#     assert "recipecooking.com" in domains


def test_get_domains_set() -> None:
    keywords = ["recipe", "dinner", "cooking"]
    tlds = ["com"]
    # tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords, tlds)
    domains = domaingen.get_keyword_combinations()
    assert type(domains) is list


# def test_get_synonym_domains_value() -> None:
#     keywords = ["recipe", "dinner", "cooking"]
#     tlds = ["com"]
#     # tlds = ['com','net', 'org']
#     domaingen = DomainGenerator(keywords, tlds)
#     domains = domaingen.get_synonym_domains()
#     assert "cookeryformula.com" in domains


def test_get_synonym_domains_set() -> None:
    keywords = ["recipe", "dinner", "cooking"]
    tlds = ["com"]
    # tlds = ['com','net', 'org']
    domaingen = DomainGenerator(keywords, tlds)
    domains = domaingen.get_synonym_domains()
    assert type(domains) is list
