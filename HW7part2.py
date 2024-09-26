# בקפיצה לגובה עם מוט )פול וולט( באולימפיאדה, שיא העולם הנוכחי לגברים עומד
# על 6.23 מטרים ,והוא נקבע על ידי ארמנד דופלנטיס (Duplantis Armand (בשנת 2023 .
# תוצאה של מעל 5.80 מטרים נחשבת טובה מאוד בתחרויות ברמה האולימפית, כאשר הזוכים
# לרוב קופצים מעל 6.00 מטרים.
# כתוב תוכנית בפייטון הקולטת תוצאות קפיצה לגובה של 7 מדינות באולימפיאדה .
# אם הגיעה תוצאה מתחת ל - 5.80 התעלם. רמז: continue
# אם הגיעה תוצאה טובה של 5.80 ומעלה ספור אותה
# אם אחת הקפיצות שברה את שיא העולם, קלוט את שם הספורטאי שהשיג את התוצאה

# בסוף הלולאה -
# - הדפס כמה תוצאות טובות היו, ומה הממוצע שלהם
# - הדפס מהי התוצאה הגבוהה ביותר
# - אם אחת הקפיצות שברה את שיא העולם, הדפס את שיא העולם החדש ואת שמו של
# הספורטאי. אחרת הדפס None

# start

good_jumps: float = 0
highest: float = 0
winner: str = None
all_result = 0.0
for i in range(7):
    jump: float = float(input('enter the result: '))
    if jump >= 5.80:
        good_jumps += 1
        all_result += jump
    if jump > highest:
        highest = jump
    if jump > 6.23:
        winner: str = str(input('the name is : '))
    else:
        continue
print(f'the number of good jumps is {good_jumps}')
print(f'the highest jump is {highest}')
print(f'the new world record is {highest} and the name of the winner is {winner}')
avg: float = all_result / good_jumps
print(f'the average of the good jumps is {avg:<2f}')
