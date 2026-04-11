HospitalName = "UNTH ENUGU."
Doctotors_name = 'Dr Henry Okolo Peter,'
Nurse_name = "Nurse Light Rose John "
location = 'N04 odo street'
wards =  '5 wards,'
beds = '40 beds,'
security  = '5 security,'
patients = '100'
checkstr= any(c.isalpha() for c in beds)
checknum = any(c.isdigit() for c in beds)
print(beds.isalnum())
index_of_s =security.find('s')
split_3 =location.split(' ')
print('does bed have number: ',checknum)
print('does bed have alphbert: ',checkstr)
print('does bed contain both number and alphbert:', {checknum==checkstr})

print(location.split(' '))
print(security.find('5'))
print(location.upper())
print(location.count('o'))
print(beds.replace('40','10'))
print(location.startswith('n'))
print('the length of location is ',len(location))
print(wards + ' ' + beds)
print(Doctotors_name + ' ' + Nurse_name)
print(HospitalName + ' '+ Doctotors_name + ' ' + Doctotors_name + ' ' + Nurse_name + ' ' + location + " " + wards + ' ' + beds + ' ' + security + ' ' + patients)