from playwright.sync_api import  sync_playwright
import csv
from datetime import datetime
time = datetime.now().strftime("%y-%m-%d %H:%M:%S")
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(0)
    page.goto("https://www.facebook.com/pagechuithue/photos/a.790795034349306/5750219131740180/")
    page.get_by_placeholder("Email or phone").click()
    page.get_by_placeholder("Email or phone").fill("0965634186")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("optimustprame")
    page.get_by_role("button", name="Accessible login button").click()
    page.get_by_role("button", name="Comment").nth(1).click()
    parsed = []
    page.get_by_role("button", name="Most relevant").click()
    page.get_by_text("All comments").first.click()
    page.wait_for_selector('div.x1jx94hy ul')
    like = page.query_selector('span.x16hj40l').inner_text()
    comment = page.query_selector('div.x6s0dn4.x78zum5.x2lah0s.x17rw0jw').query_selector_all('div.xnfveip')[0].query_selector('span span').inner_text()
    share =  page.query_selector('div.x6s0dn4.x78zum5.x2lah0s.x17rw0jw').query_selector_all('div.xnfveip')[1].query_selector('span span').inner_text()
    print(like,comment,share)
    while page.query_selector_all('div.x78zum5.x13a6bvl.xdj266r.xktsk01.xat24cr.x1d52u69')[2].inner_html() != '':
        view = page.query_selector_all('div.x78zum5.x13a6bvl.xdj266r.xktsk01.xat24cr.x1d52u69')[2].query_selector('span span').inner_text()
        print(view)
        page.get_by_role("button", name=view).click()
    all_comments= page.query_selector_all('div.x1jx94hy ul > li > div.x1n2onr6 > div.x1n2onr6.x4uap5.x18d9i69.x1swvt13.x1iorvi4.x78zum5.x1q0g3np.x1a2a7pz')
    for comment in all_comments:
        obj={}
        author = comment.get_attribute('aria-label')
        author = author.replace('Comment by ','')
        obj['author']=author
        cmts = comment.query_selector_all('div.x1lliihq.xjkvuk6.x1iorvi4 div.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs.xdj266r div')
        stri = ''
        for cmt in cmts:
            stri+=cmt.inner_text()
        obj['cmt']=stri
        obj['date_at']= time
        parsed.append(obj)
        print(author,stri)
    field_names = ['author','cmt','date_at']
    with open('commentpost.csv', 'w+', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(parsed)
    context.close()
    browser.close()
   











