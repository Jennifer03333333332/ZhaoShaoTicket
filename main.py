def info_flight():
    ticket_search = wd.find_element_by_css_selector('.ticket_search') #class
    # 点击下拉框
    endsite_fisrt = wd.find_element_by_css_selector('#endsite_fisrt') #id


    endsite_fisrt.click()


    xpath_toplace = "//*[@id='endsite_dd']/p[9]"
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_toplace)))
    wd.find_element_by_xpath(xpath_toplace).click()
    #target = wd.find_element_by_xpath("//p[@data-site='HKA']")

    # 出发日期
    to_date = wd.find_element_by_id('to_date')
    to_date.click()


    #print(to_date.text)


    target1Table = wd.find_elements_by_xpath("//div[@class='xdsoft_datetimepicker xdsoft_noselect ']")
    #target1 = wd.find_element_by_xpath("//div[@class='xdsoft_datetimepicker xdsoft_noselect '][contains(@style,'display = block')]")


    rubbish = 0


    for targettest in target1Table:


        if rubbish == 1:
            target1 = targettest
            break
        rubbish = 1
    #弹出的日历
    mounthpicker = target1.find_element_by_class_name('xdsoft_mounthpicker')


    sleep(2)
    # 点击6月
    mounthpicker.find_element_by_class_name('xdsoft_month').click()


    xpath_august = "/html/body/div[4]/div[1]/div[1]/div[1]/div/div[1]/div[8]"
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_august)))
    wd.find_element_by_xpath(xpath_august).click()




    calendar = target1.find_element_by_class_name('xdsoft_calendar')
    #date = calendar.find_element_by_xpath("//td[@data-date ='20']")#("//td[@data-value='7' and @data-date ='20']")


    #wd.execute_script("arguments[0].click();", date)
    sleep(2)
    xpath_20 = "/html/body/div[4]/div[1]/div[2]/table/tbody/tr[3]/td[6]/div"
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_20)))
    wd.find_element_by_xpath(xpath_20).click()




    sleep(5)
    # 航空 第一个
    aircompany = ticket_search.find_element_by_xpath("//input[@class='full_width autocomplete ui-autocomplete-input']")
    aircompany.click()
    ac = ticket_search.find_element_by_xpath("//p[@class='airLineName'][@data-id='4'][@data-code='AC']")
    ac.click()
    # flightNo
    flightNo = ticket_search.find_element_by_id('flightNo')
    flightNo.send_keys('AC016')


    flight_time_elements = ticket_search.find_elements_by_css_selector('select set_out time')



    #起飞hours
    wd.find_element_by_xpath("//*[@id='flightHours']").click()


    xpath_flightHours = "//*[@id='scroll']/div[2]/div/div[2]/div[6]/div[2]/dl[1]/dd/p[14]"
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_flightHours)))
    wd.find_element_by_xpath(xpath_flightHours).click()
    #分钟
    wd.find_element_by_xpath("//*[@id='flightMinute']").click()


    xpath_flightMinutes = "//*[@id='scroll']/div[2]/div/div[2]/div[6]/div[2]/dl[2]/dd/p[56]"
    WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_flightMinutes)))
    wd.find_element_by_xpath(xpath_flightMinutes).click()

    sure_btn = ticket_search.find_element_by_id('sure')
    sure_btn.click()