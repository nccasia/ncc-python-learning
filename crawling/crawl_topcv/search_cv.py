from playwright.sync_api import sync_playwright
import csv
import json
from datetime import datetime
time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(0)
    page.goto("https://tuyendung.topcv.vn/app/search-cv?url_redirect=%2Fjobs")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("email")
    page.get_by_placeholder("Mật khẩu").click()
    page.get_by_placeholder("Mật khẩu").click()
    page.get_by_placeholder("Mật khẩu").fill("matkhau")
    page.get_by_role("button", name="Đăng nhập").click()
    page.get_by_role("main").get_by_role("link", name="Tìm CV").click()
    page.get_by_text("Tất cả nội dung").click()
    page.wait_for_selector('tbody.ta-impression-container')
    item = page.query_selector_all('div.d-flex.justify-content-center nav ul.pagination li.page-item')
    parsed = []
    active = 0
    link ='https://tuyendung.topcv.vn/app/recruitment-campaigns/1072515/search-cv?page=' + str(active) 
    while  active <= 1 :
      active+=1
      link ='https://tuyendung.topcv.vn/app/recruitment-campaigns/1072515/search-cv?page=' + str(active) 
      page.set_default_timeout(0)
      page.goto(link)
      page.wait_for_selector('tbody.ta-impression-container')
      page.wait_for_selector('div.d-flex.justify-content-center nav ul.pagination')
      employees = page.query_selector_all('tr')
      for em in employees:
          page.wait_for_selector('div')
          viewmore =  page.query_selector_all('div.text-primary.show-more.mt-1')
          fullname = em.query_selector('a.cv-fullname')
          position = em.query_selector_all('div.ml-1 div.d-flex.align-items-start.mt-1.mt-2')
          detail = em.query_selector_all('td.align-top')
          obj = {'id':'','fullname':'','position':'','place':'','experiment':'','educated':'','target':''}
          obj['id']= em.get_attribute('data-ta-cv_id')
          if len(detail)>0:
                  for i in range(len(viewmore)):
                          page.get_by_text("Xem thêm...").first.click()
                  obj['fullname'] = str(fullname.inner_text())
                  if len(position) >= 1:
                    for pos in position:
                        if pos.query_selector('div').inner_html() =='<i class="far fa-briefcase"></i>':
                            obj['position'] = str(pos.query_selector('span').inner_text())
                        elif pos.query_selector('div').inner_html() =='<i class="far fa-map-marker"></i>':
                            obj['place'] = str(pos.query_selector('span').inner_text())
                  mbs = detail[1].query_selector_all('div.mb-3')
                  for mb in mbs:
                      title = mb.query_selector('strong').inner_text()
                      if 'Kinh nghiệm' in str(title):
                          text = ''
                          exp = mb.query_selector_all('div.d-flex.align-items-start.mt-1')
                          for info in exp:
                              text +=' '+ info.query_selector('span').inner_text()
                          obj['experiment']=str(text)
                      elif 'Học vấn' in str(title) :
                          text = ''
                          exp = mb.query_selector_all('div.d-flex.align-items-start.mt-1')
                          for info in exp:
                              text +=' '+ info.query_selector('span').inner_text()
                          obj['educated']=str(text)
                      elif 'Mục tiêu sự nghiệp' in str(title) :
                          obj['target']= str(mb.query_selector('p.mb-0').inner_text())
          parsed.append(obj)
          for ele in parsed:
            if ele['id'] is None:
                parsed.remove(ele)
          print(obj)
# JSON output
    with open("cvs.json", "a", encoding='utf-8') as outfile:
        outfile.write('[')
        for x in range(len(parsed)):
                json_object = json.dumps(parsed[x], indent=4,ensure_ascii=False)
                outfile.write(json_object)
                if x < len(parsed)- 1:
                   outfile.write(",")
        outfile.write(']')
# CVS output
    field_names = ['id','fullname','position','place','experiment','educated','target']
    with open('cvs.csv', 'w+', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(parsed)






