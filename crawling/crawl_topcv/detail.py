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
    all_items = page.query_selector_all('div.slick-track div.col-sm-6.feature-job.job-ta')
    for item in all_items :
        id=item.get_attribute("data-job-id")
        name_job = item.query_selector('a.title.text_ellipsis')
        link=name_job.get_attribute('href')
        type_link = link.split('/')[3]
        page = context.new_page()
        page.set_default_timeout(0)
        page.goto(link)
        obj = {'Id':id}
        box_item = page.query_selector_all('div.box-main div.box-item')
        for box in box_item:
            name = box.query_selector('div strong').inner_text()
            value =box.query_selector('div span').inner_text()
            if name == 'Mức lương':name = 'salary'
            elif name == 'Số lượng tuyển': name = 'number'
            elif name == 'Hình thức làm việc':name='working'
            elif name == 'Cấp bậc':name='rank'
            elif name == 'Giới tính':name='gender'
            elif name == 'Kinh nghiệm':name='experienced'
            obj[str(name)]=value
        box_address=page.query_selector_all('div.box-address div div')
        obj['address']=''
        for addr in box_address:
            obj['address']+=addr.inner_text()
        if type_link == 'brand':
            obj['deadline'] = page.query_selector('span.deadline').inner_text()
        else:
            if page.query_selector('div.job-deadline') is not None:
                deadline = page.query_selector('div.job-deadline').inner_html()
                deadline = deadline.replace('<i class="fa-regular fa-clock"></i>','')
                deadline = deadline.replace(' Hạn nộp hồ sơ: ','')
                deadline = deadline.replace('\n','')
                obj['deadline']= deadline
        obj['date_at']= time
        obj['link']= link
        print(obj)
        parsed.append(obj)
        page.close()
    field_names = ['id', 'salary', 'number', 'working', 'rank', 'gender', 'experienced', 'address', 'deadline', 'date_at', 'link']
    with open('topcvjobdetail.csv', 'w+', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(parsed)
    
    
    
    
