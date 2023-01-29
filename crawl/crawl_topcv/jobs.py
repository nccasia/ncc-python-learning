from playwright.sync_api import sync_playwright
import csv
from datetime import datetime
time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.topcv.vn/viec-lam")
    parsed = []
    all_items = page.query_selector_all('div.col-md-4.col-sm-6.feature-job.job-ta')
    for item in all_items:
        id = item.query_selector('div.col-title.cvo-flex-grow a.text-silver.company.text_ellipsis.underline-box-job')
        link = id.get_attribute('href')
        company_id = link.split('/')[-1].split('.')[0]
        code_company = link.split('/')[-2]
        parsed.append({
              "id":item.get_attribute("data-job-id"),
              "job": item.query_selector('a.title.text_ellipsis strong.transform-job-title').inner_text(),
              "company": item.query_selector('a.text-silver.company.text_ellipsis').inner_text(),
              "company_id":company_id,
              "salary": item.query_selector('div.salary.text_ellipsis').inner_text(),
              "address": item.query_selector('div.address.text_ellipsis').inner_text(),
              "date_at":time
        })
    field_names = ['id', 'job', 'company', 'company_id', 'salary', 'address', 'date_at']
    with open('topcvjob.csv', 'w+', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(parsed)
    
   
   