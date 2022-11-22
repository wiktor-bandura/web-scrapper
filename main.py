import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.pl/dp/B08C7KG5LP/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=025e3bd28bdb53a692eedafbaa9e30fd&content-id=amzn1.sym.818d4ba5-9099-487d-af4a-233d33d05a75%3Aamzn1.sym.818d4ba5-9099-487d-af4a-233d33d05a75&hsa_cr_id=0&pd_rd_plhdr=t&pd_rd_r=e2977f10-83db-4276-8a97-34305f12cc95&pd_rd_w=BoIUl&pd_rd_wg=aTGsV&qid=1669156281&ref_=sbx_be_s_sparkle_lsi4d_asin_2_img&sr=1-3-e0fa1fdd-d857-4087-adda-5bd576b25987'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0"
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
