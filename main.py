from Part import Part
from Minifigure import Minifigure
from Set import Set
from LegoStorage import Storage
from flask import Flask, render_template, request
from BrickLink_thief import thief

app = Flask(__name__, template_folder='template')

S1 = Storage("Trash", 1, 1)

S2 = Storage("Minifigurki", 1, 2)

b1 = Part('Torso Shirt with Dark Bluish Gray Neck and Wrinkles Pattern / Medium Tan Arms / Medium Tan Hands',
          '973pb4832c01', 8.91, 1,
          'https://www.bricklink.com/v2/catalog/catalogitem.page?P=973pb4832c01&idColor=11#T=S&C=11&O={"color":11,"rpp":"500","iconly":0}',
          'https://img.bricklink.com/ItemImage/PN/11/973pb4832c01.png', 'Torso', 'Black')
b2 = Part('Hips and Legs Plain', '970c00', 0.05, 1, 'https://www.bricklink.com/v2/catalog/catalogitem.page?P=970c00&idColor=85#T=S&C=85&O={"color":85,"rpp":"500","iconly":0}', 'https://img.bricklink.com/ItemImage/PN/85/970c00.png', 'Legs', 'Dark Bluish Gray')
b3 = Part('Minifigure, Head Black Eyebrows, Dark Orange Eye Shadow and Chin Dimple, Nougat Cheek Lines, Neutral Pattern - Hollow Stud', '3626cpb3066', 5.53, 1, 'https://www.bricklink.com/v2/catalog/catalogitem.page?P=3626cpb3066&idColor=241#T=S&C=241&O={"color":241,"rpp":"500","iconly":0}', 'https://img.bricklink.com/ItemImage/PN/241/3626cpb3066.png', 'Head', 'Medium Tan')

#S2.add(Minifigure("Dominic Toretto", "sc103", 20, 1,
#                  'https://www.bricklink.com/v2/catalog/catalogitem.page?M=sc103&#T=S&O={"ss":"PL","loc":"PL","rpp":"500","iconly":0}',
#                  'https://img.bricklink.com/ItemImage/MN/0/sc103.png', [b1, b2, b3]))

#S2.add(Minifigure("Dominic Toretto", "sc103", 20, 2,
#                  'https://www.bricklink.com/v2/catalog/catalogitem.page?M=sc103&#T=S&O={"ss":"PL","loc":"PL","rpp":"500","iconly":0}',
#                  'https://img.bricklink.com/ItemImage/MN/0/sc103.png', [b1, b2, b3]))

#S2.add(Minifigure("Dominic Toretto", "sc1033", 20, 2,
#                  'https://www.bricklink.com/v2/catalog/catalogitem.page?M=sc103&#T=S&O={"ss":"PL","loc":"PL","rpp":"500","iconly":0}',
#                  'https://img.bricklink.com/ItemImage/MN/0/sc103.png', [b1, b2, b3]))

#S2.add(Minifigure("Dodrg", "serg", 20, 2,
#                  'https://www.bricklink.com/v2/catalog/catalogitem.page?M=sc103&#T=S&O={"ss":"PL","loc":"PL","rpp":"500","iconly":0}',
#                  'https://img.bricklink.com/ItemImage/MN/0/sc103.png', [b1, b2, b3]))

#S2.save()

list_of_Storages = [S1, S2]


@app.route('/', methods=['GET', 'POST'])
def index():
    for st in list_of_Storages:
        st.read()
    if request.method == 'POST':
        for s in list_of_Storages:
            for i in range(0, len(s.collection)):
                if 'delete'+s.name + str(i) in request.form:
                    s.del_item(i)
                    s.save()
                    s.read()
            if "add_elof_"+s.name in request.form:
                brick = []
                for each in request.form:
                    brick.append(request.form[each])
                if s.content == "Parts":
                    el = thief(brick[0])
                    s.add(Part(el.get_name(), el.get_id(), float(el.get_price()), int(brick[1]), brick[0], el.get_img(), el.get_type(), brick[3]))
                elif s.content == "Minifigures":
                    s.add(Minifigure(brick[0], brick[1], float(brick[2]), int(brick[3]), brick[4], brick[5], [Part(brick[6], brick[6], float(brick[6]), int(brick[6]), brick[6], brick[6], brick[6], brick[6])]))
                elif s.content == "Sets":
                    pass
                s.save()
    return render_template('index.html', Storages=list_of_Storages)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0")
