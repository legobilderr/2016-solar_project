# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star": 
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            if object_type == "planet": 
                planet = Planet()
                parse_planet_parameters(line,planet)
                objects.append(planet)
            else:
                print("Unknown space object",line)

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    list_lines_star=line.split( )
    for i in range (len(list_lines_star)):
        try:
            list_lines_star[i]=float(list_lines_star[i])
        except ValueError:
            pass

    list_values_of_star=list_lines_star
    star.R=list_values_of_star[1]
    star.color=list_values_of_star[2]
    star.m=list_values_of_star[3]
    star.x=list_values_of_star[4]
    star.y=list_values_of_star[5]
    star.Vx=list_values_of_star[6]
    star.Vy=list_values_of_star[7]
    # pass  # FIXME: not done yet

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    list_lines_planet=line.split( )
    for i in range (len(list_lines_planet)):
        try:
            list_lines_planet[i]=float(list_lines_planet[i])
        except ValueError:
            pass

    list_values_of_planet=list_lines_planet
    planet.R=list_values_of_planet[1]
    planet.color=list_values_of_planet[2]
    planet.m=list_values_of_planet[3]
    planet.x=list_values_of_planet[4]
    planet.y=list_values_of_planet[5]
    planet.Vx=list_values_of_planet[6]
    planet.Vy=list_values_of_planet[7]

    # pass  # FIXME: not done yet...


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            list_obj=[str(i) for i in (obj.type,obj.R,obj.color,obj.m,obj.x,obj.y,obj.Vx,obj.Vy)]
            str_obj=' '.join(list_obj)
            out_file.write(str_obj+'\n')
            out_file.write('\n')


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
