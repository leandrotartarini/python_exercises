measure = float(input('Type a measure in meters: '))
cm = measure * 100
mm = measure * 1000
dm = measure * 10
dam = measure / 10
hm = measure / 100
km = measure / 1000
print(f'The measure of {measure} meters is equal to \n{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm')