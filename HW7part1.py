# ק לוט 10 מספרים מהמשתמש באמצעות לולאה.
# אם הוכנס מספר גדול מ1000- או קטן ממינוס ,1000 התעלם מהמספר . רמז: continue
# אם הוכנס מינוס ,9999 צא מהלולאה ואל תדפיס את הסטטיסטיקות
# במידה ולא נקלט מינוס 999 הדפס את הסטטיסטיקות הבאות:
# - כמה מספרים חיוביים נקלטו?
# - כמה מספרים שליליים נקלטו ?
# - כמה פעמים הוכנס המספר 0?
# - כמה מספרים המתחלקים ב- 7 ללא שארית נקלטו?
# - מה היה המספר החיובי האחרון שהוכנס? אם לא היה כזה, הדפס None
# - מה היה המספר השלילי האחרון שהוכנס? אם לא היה כזה, הדפס None
# )כדאי להשתמש בלולאה עם else- כדי לטפל במקרה שבו המספרים הוזנו בהצלחה ולא יצאת
# מוקדם עם break בעקבות קלט של מינוס 999(

# start

pos_num: int = 0
neg_num: int = 0
zeroes: int = 0
div_by7: int = 0
last_pos: int = None
last_neg: int = None
number: int = 0

for i in range(5):
    number: int = int(input("enter the number: "))
    if number > 1000 or number < -1000:
        continue
    if number == -999:
        print('')
        break
    if number == 0:
        zeroes += 1
    if number & 7 == 0:
        div_by7 += 1
    if number > 0:
        pos_num += 1
        last_pos = number
    elif number < 0:
        neg_num += 1
        last_neg = number

print(f'{zeroes=}\n{pos_num=}\n{neg_num=}\n{last_neg=}\n{last_pos=}\n{div_by7=}')









