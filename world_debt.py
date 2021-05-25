from selenium import webdriver

url = 'https://www.usdebtclock.org/world-debt-clock.html'


class WorldDebt:
    # United States
    def us_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="X2a5BWRG"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # China
    def cn_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="M2a0923KLS"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Japan
    def jp_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="R2a9163KRX"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Germany
    def de_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="E2a8263KGD"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # United Kingdom
    def uk_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="H2a6763MKJ"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # India
    def in_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="U2a7623KMY"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # France
    def fr_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="E2a9323KMG"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Italy
    def it_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="K2a4563MHD"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Brazil
    def br_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="F2a2923KNS"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Canada
    def ca_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="W2a9223KMJ"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Argentina
    def ar_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="Z2a2823KEC"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Australia
    def au_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="L2a2323KNF"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Belgium
    def be_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="N2a3223KYN"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Greece
    def gr_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="Q2a3263MLB"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Indonesia
    def id_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="A2a6523KLM"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Ireland
    def ie_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="T2a1523KMY"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Korea
    def kr_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="Y2a6423KMG"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Mexico
    def mx_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="P2a8223KMG"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Netherlands
    def nl_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="O2a6523KWB"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Nigeria
    def ng_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="XB2a212KPL"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Norway
    def no_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="C2a6323KLB"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Poland
    def pl_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="V2a2123KRV"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Portugal
    def pt_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="S2a4563KRI"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Russia
    def ru_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="G2a5723KEC"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Saudi Arabia
    def sa_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="D2a8563KWX"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Spain
    def es_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="J2a1463MMJ"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Sweden
    def se_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="P2a9223KEC"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Switzerland
    def ch_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="I2a3123KWT"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Taiwan
    def tw_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="EB2a932KMS"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt

    # Turkey
    def tr_debt():
        driver = webdriver.Firefox()
        driver.get(url)
        raw_elem = driver.find_element_by_xpath('//span[@id="B2a7523KUM"]')
        debt = int(raw_elem.text.replace(',', '').replace('$', ''))
        driver.close()
        return debt
