hospital_name = 'unth enugu'
doctor_name = 'okolo peter henry'
nurse_name = 'light agnes peter'
location = 'n04 bank street'
wards = '5 wards'
beds = '40 beds'
security = '5 security'
patient = "100"
capital_letter = ((hospital_name + ' ' + doctor_name + ' ' + nurse_name + ' ' + location + ' ' + wards + ' ' + beds + ' ' + security + ' ' + patient))
#print(hospital_name + ' ' + doctor_name)
print(hospital_name + ' ' + doctor_name + ' ' + nurse_name + ' ' + location + ' ' + wards + ' ' + beds + ' ' + security + ' ' + patient)
print(capital_letter.upper())
#print(capital_letter.capitalize())
print(location.count('o'))
print(beds.replace('40 beds', '5 beds'))
print(location.split(' '))
print(security.find('s'))
print(location.startswith('N'))
print(beds== 'does beds has num and str')
