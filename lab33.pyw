import re
text = r'dasd@mail.ru sadw eqrfgs dagfeatvgrs 3232@mail.ru adsada a 3da@yandex.ru 312323@312 425235 asfw4 '
finder = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,6}\b", re.IGNORECASE)
print(re.findall(finder, text))
