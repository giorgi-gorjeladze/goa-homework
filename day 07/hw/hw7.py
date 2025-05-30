num2 = int(input())
for i in range(1,num2):
    if num2 % i == 0:
        print(i)

# for ციკლს ვიყენებთ, როცა ვიცით რამდენი იდენტაცია არის საჭირო
# ხოლო while ციკლი, როცა არ ვიცით, რამდენი იდენტაცია არის საჭირო

#(T and F) or (T and T) and (F or F)
#T and F == F T and T == T F and F == F
# F or T or F == T

# FOR LOOP
# for ციკლის მეშვეობით შეგვიძლია კოდის გაშვება იმდენჯერ, რამდენჯერაც გვინდა.
# for ციკლში შეგვიძლია გამოვყოთ როგორც ინტეჯერები range ფუნქციის გამოყენებით, ისევე სტრინგები.
# i ცვლადი, რომელიც ლუპის დასაწყისში იქმნება არის counter ცვლადი.
# range ფუნქციაში პირველ ადგილზე მდგომი ციფრი აღნიშნავს საწყის წერტილს, მეორე დასასრულის წერტილს, მესამე კი ინტერვალს, რომლითაც მივდივართ პირველიდან მეორე ციფრამდე.
# default პირველი ციფრი არის 0, ხოლო default მესამე არის 1.
# ათვლის უკუღმა საწარმოებლად range-ს უკან ვუწერთ reversed ფუნქციას
# როცა ციკლში მოექცა სტრინგი, მაშინ i-ს სტრინგის თითოეული ასო და სიმბოლო გამოაქვს.
# ასევე გვაქვს 2 ფუნქცია, რომელთა გამოყენება ორივე ციკლში შეიძლება: continue and break
# continue მითითებულ ნაბიჯს გამოტოვებს, ხოლო break-ი ფუნქციას მოცემულ ნაბიჯზე წყვეტს

#WHILE LOOP
# while ციკლი ასრულებს მოცემულ დავალებას მანამ, სანამ მოცენული პირობა არის ჭეშმარიტი.
# როცა ციკლის პირობა გახდება მცდარი, კომპაილერი წყვეტს while ციკლს და გადადის შემდეგ კოდზე.
# თუ ციკლის პირობა ყოველთვის ჭეშმარიტია, მაშინ იქმნება infinite loop.
# იმისთვის, რომ ეს არ მოხდეს, გვჭირდებს counter ოპერაცია, მაგ: პირობის თავიდან შეყვანა.
# ციკლში შეგვიძლია გამოვიყენოთ ლოგიკური ოპერატორები: not და or
# or ოპერატორი ძირითადად გამოიყენება boolean-ებთან. იმისათვის, რომ კოდი გაეშვას ორივე პირობა უნდა იქნას შესრულებული
# not ოპერატორი გამოხატავს უარყოფას. მაგ: not true == false. not 5 == any number other than 5.
