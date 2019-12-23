from datetime import datetime

odd = [25, 27, 29, 31]

this_minute = datetime.today().minute

print(this_minute)

if this_minute in odd:
    print("Such an odd minute")
else:
    print("Not so odd")