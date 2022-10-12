views_years=int(input( "годы, затраченные на просмотр экспонатов " ))
print( "Количество просмотренных экспонатов: " ,views_years*365*8*60//5)
exh =int(input( "количество экспонатов "))
time= exh*5
days=time//480
time -= days*480
years = days // 365
days %= 365
print("years ", years, "days ", days, "min ", time)

