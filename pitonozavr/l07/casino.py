# Фейсконтроль (есть ли ты в списках) - просят ваше имя 
# и проверяют в базах.
# Делайте ставки и выбираем поле (красное либо черное)
# Рулетка крутится (random.randint(1, 37), in range())
# Если выиграли, то молодец, ставка х2, иначе лох, деньги идут казино

vip_list = input("Введите список допускаемых гостей: ").split(", ")

while True:
	person = {}
	person["имя"] = input("Представьтесь, молодой человек! ")
	if person["имя"] in vip_list:
		person["ставка"] = int(input("Добро пожаловать! " 
			+ person["имя"] + ". Делайте свою ставку. "))

	else:
		print("Вас погнали поджопниками!")