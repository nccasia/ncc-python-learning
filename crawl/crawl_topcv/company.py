from playwright.sync_api import sync_playwright
import csv
from datetime import datetime
time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(0)
    page.goto("https://www.topcv.vn/viec-lam")
    parsed = []
    all_items = page.query_selector_all('div.col-md-4.col-sm-6.feature-job.job-ta')
    for item in all_items:
        id = item.query_selector('div.col-title.cvo-flex-grow a.text-silver.company.text_ellipsis.underline-box-job')
        link = id.get_attribute('href')
        id_company = link.split('/')[-1].split('.')[0]
        code_company = link.split('/')[-2]
        obj={"id":id_company, 'code':'', 'name':id.get_attribute('data-original-title'), 'introduction':'', 'employee':'', 'address':''}
        page = context.new_page()
        page.set_default_timeout(0)
        page.goto(link)
        obj['introduction']=''
        if code_company == 'brand':
            texts = page.query_selector_all('div.intro-content ')
            for text in texts:
                intro = text.inner_text()
                intro = intro.replace('\xa0','')
                intro = intro.replace('\n','')
                intro = intro.replace('&nbsp;',' ')
                obj['introduction'] +=intro
            obj['code'] = id_company
            employee = page.query_selector_all('div.information-section div.box-items')
            if len(employee)>1:
                obj['employee'] = employee[1].query_selector('div div.value-block').inner_text()
            line = page.query_selector_all('div.content-contact div.info-line')
            if len(line)>1:
                obj['address'] = line[-1].query_selector('span').inner_text()
        else:
            texts= page.query_selector_all('div.company-info.box-white div.box-body p')
            for text in texts:
                intro = text.inner_text()
                intro = intro.replace('\xa0','')
                intro = intro.replace('\n','')
                intro = intro.replace('&nbsp;',' ')
                obj['introduction'] +=intro
            obj['code'] = code_company
            if page.query_selector('p.company-size'):
                size = page.query_selector('p.company-size').inner_html()
                size = size.replace('<i class="fa-light fa-building"></i>','')
                size = size.replace('\n','')
                obj['employee'] = size
            if page.query_selector('div.box-body p.text-dark-gray'):
                a = page.query_selector('div.box-body p.text-dark-gray').inner_html()
                a=a.replace('<i class="icons8-map-pin text-highlight"></i>','')
                a=a.replace('\n','')
                obj['address']= a
            obj['date_at']= time
        print(obj)
        parsed.append(obj)
        page.close()
    field_names = ['id', 'code', 'name', 'introduction', 'employee', 'address','date_at']
    with open('topcvcompany.csv', 'w+', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(parsed)

