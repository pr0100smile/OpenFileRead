#---Задача №1---

from pprint import pprint
import json

with open('recipes.txt', 'rt', encoding='utf-8') as rec:
  cook_book = {}
  for dish in rec:
    dish_count = int(rec.readline())
    dish_list = []
    for i in range(dish_count):
      ingredient, quantity, measure = rec.readline().strip().split(' | ')
      dish_list.append({
        'ingredient_name': ingredient,
        'quantity': quantity,
        'measure': measure
      })
    rec.readline()
    cook_book[dish.strip()] = dish_list

  # pprint(cook_book)
  res = json.dumps(cook_book, ensure_ascii=False, indent=2)
  # print(res)

#---Задача №2---
def get_shop_list_by_dishes(dishes, person_count):
  ingredients = {}
  for dish in dishes:
    for meal in cook_book[dish]:
      if ingredients.get(meal['ingredient_name']):
        ingredients[meal['ingredient_name']]['quantity'] += int(
          meal['quantity']) * person_count
      else:
        ingredients[meal['ingredient_name']] = {
          'measure': meal['measure'],
          'quantity': int(meal['quantity']) * person_count
        }

  return ingredients

pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))

#---Задача №3---

with open("1.txt", encoding='utf-8') as f1:
    content1 = f1.readlines()
with open("2.txt", encoding='utf-8') as f2:
    content2 = f2.readlines()
with open("3.txt", encoding='utf-8') as f3:
    content3 = f3.readlines()


files = [('1.txt', len(content1)), ('2.txt', len(content2)), ('3.txt', len(content3))]

files_sorted = sorted(files, key=lambda x: x[1])

with open("res_4.txt", "w") as f:
  for file_info in files_sorted:
    f.write(file_info[0] + '\n')
    f.write(str(file_info[1]) + '\n')
    if file_info[0] == '1.txt':
      f.writelines(content1)
      f.write('\n')
    elif file_info[0] == '2.txt':
      f.writelines(content2)
      f.write('\n')
    elif file_info[0] == '3.txt':
      f.writelines(content3)
      f.write('\n')