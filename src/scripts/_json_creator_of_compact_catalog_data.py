import json

SINGLE_WALL = 'Одностінний'
DOUBLE_WALL = 'Двостінний'
types = [SINGLE_WALL, DOUBLE_WALL]
thicknesses = [0.5, 0.8, 1]
steels = {
    SINGLE_WALL: ['Нержавіюча сталь', 'Оцинкована сталь'],
    DOUBLE_WALL: ['Нержавіюча сталь/Нержавіюча сталь', 'Нержавіюча сталь/Оцинкована сталь'],
}
diameters = {
    SINGLE_WALL: [
        100,
        110,
        120,
        125,
        130,
        140,
        150,
        160,
        170,
        180,
        190,
        200,
        210,
        220,
        230,
        240,
        250,
        260,
        280,
        300,
        310,
        320,
        360,
    ],
    DOUBLE_WALL: [
        '100/160',
        '110/180',
        '120/180',
        '125/200',
        '130/200',
        '140/200',
        '150/220',
        '160/220',
        '180/250',
        '200/260',
        '220/280',
        '230/300',
        '250/320',
        '300/360',
    ],
}

stovepipes_detail = {
    'Димарі': [
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Труба',
            'template_title': '{title} {length}мм {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'length': 'Довжина (мм)',
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': types,
                'Тип:Сталь': steels,
                'Товщина сталі (мм)': thicknesses,
                'Довжина (мм)': [250, 300, 500, 1000],
                'Тип:Діаметр (мм)': diameters,
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Коліно',
            'template_title': '{name} {corner}° {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'corner': 'Кут',
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specification': {
                'Тип': types,
                'Тип:Сталь': steels,
                'Товщина сталі (мм)': thicknesses,
                'Тип:Діаметр (мм)': diameters,
                'Кут': [45, 90],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Трійник',
            'template_title': '{title} {corner}° {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'corner': 'Кут',
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specification': {
                'Тип': types,
                'Тип:Сталь': steels,
                'Товщина сталі (мм)': thicknesses,
                'Тип:Діаметр (мм)': diameters,
                'Кут': [45, 87],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Ревізія',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': types,
                'Тип:Сталь': steels,
                'Товщина сталі (мм)': thicknesses,
                'Тип:Діаметр (мм)': diameters,
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Грибок',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': types,
                'Тип:Сталь': steels,
                'Товщина сталі (мм)': [thicknesses[0]],
                'Тип:Діаметр (мм)': diameters,
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Іскрогасник',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': SINGLE_WALL,
                'Сталь': steels[SINGLE_WALL],
                'Товщина сталі (мм)': thicknesses[0],
                'Діаметр (мм)': diameters[SINGLE_WALL],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Флюгер',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': SINGLE_WALL,
                'Сталь': steels[SINGLE_WALL],
                'Товщина сталі (мм)': thicknesses[0],
                'Діаметр (мм)': diameters[SINGLE_WALL],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Дека',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': SINGLE_WALL,
                'Сталь': steels[SINGLE_WALL],
                'Товщина сталі (мм)': thicknesses[0],
                'Діаметр (мм)': diameters[SINGLE_WALL],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Перехідник',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': SINGLE_WALL,
                'Сталь': steels[SINGLE_WALL],
                'Товщина сталі (мм)': thicknesses,
                'Діаметр (мм)': diameters[SINGLE_WALL],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': '',
            'prices': 1000,
            'title': 'Скоба',
            'template_title': '{title} {steel} Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {},
                'description_kwargs': {},
            },
            'specifications': {
                'Сталь': steels[SINGLE_WALL][0],
                'Діаметр (мм)': diameters[SINGLE_WALL],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Конус',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': DOUBLE_WALL,
                'Сталь': steels[DOUBLE_WALL],
                'Товщина сталі (мм)': thicknesses[0],
                'Діаметр (мм)': diameters[DOUBLE_WALL],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Стакан',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': DOUBLE_WALL,
                'Сталь': steels[DOUBLE_WALL],
                'Товщина сталі (мм)': thicknesses[0],
                'Діаметр (мм)': diameters[DOUBLE_WALL],
            },
        },
        {
            'mixing_type': 'mixed',
            'typing_specification_name': 'Тип',
            'prices': 1000,
            'title': 'Конденсатозбірники',
            'template_title': '{title} {steel} {thickness}мм Ø{diameter}мм',
            'template_description': '',
            'template_kwargs': {
                'title_kwargs': {
                    'steel': 'Сталь',
                    'thickness': 'Товщина сталі (мм)',
                    'diameter': 'Діаметр (мм)',
                },
                'description_kwargs': {},
            },
            'specifications': {
                'Тип': SINGLE_WALL,
                'Сталь': steels[SINGLE_WALL],
                'Товщина сталі (мм)': thicknesses[0],
                'Діаметр (мм)': diameters[SINGLE_WALL],
            },
        },
    ]
}

type_ = 'Двоконтурний'
fuel_types = 'Дрова, Брикети, Тирса, Вугілля'
work_pressure = 0.15

boilers = {
    'Твердопаливні котли': [
        {
            'mixing_type': 'equal',
            'typing_specification_name': 'Тип котла',
            'prices': [25000, 27000, 29000, 38500],
            'title': 'К',
            'template_title': 'Твердопаливний котел МАРС {title}-{power}',
            'template_description': '',
            'template_kwargs': {'title_kwargs': {'power': 'Потужність (кВт)'}, 'description_kwargs': {}},
            'specifications': {
                'Тип котла': type_,
                'Типи палива': fuel_types,
                'Тип завантаження': 'Верхне',
                'Тривалість робочого циклу': '4-8',
                'Робочій тиск в системі опалення': work_pressure,
                'Потужність (кВт)': [12, 15, 18, 25],
                'Площа опалювання (м кв)': [120, 150, 180, 250],
                "Об'єм камери завантаження (л)": [53, 70, 85, 160],
                'Вага нетто (кг)': [120, 140, 160, 230],
                'Габарити ВхШхД (мм)': ['950х340х760', '950х410х760', '950х480х760', '1150х480х830'],
                'Мінімальна висота димаря (м)': [6, 6, 6, 7],
                'Розмір патрубку відводу продуктів згоряння (мм)': [127, 127, 159, 159],
                'Розмір приєднувальних патрубків': ['G1-B', 'G1-B', 'G2-B', 'G2-B'],
            },
        },
        {
            'mixing_type': 'equal',
            'typing_specification_name': 'Тип котла',
            'prices': [15400, 15900, 16300, 16700],
            'title': 'КТК',
            'template_title': 'Твердопаливний котел МАРС {title}-{power}',
            'template_description': '',
            'template_kwargs': {'title_kwargs': {'power': 'Потужність (кВт)'}, 'description_kwargs': {}},
            'specifications': {
                'Тип котла': type_,
                'Типи палива': fuel_types,
                'Тип завантаження': 'Фронтальне',
                'Тривалість робочого циклу': 4,
                'Робочій тиск в системі опалення': work_pressure,
                'Потужність (кВт)': [10, 12, 14, 16],
                'Площа опалювання (м кв)': [100, 120, 140, 160],
                "Об'єм камери завантаження (л)": [26, 34, 40, 46],
                'Вага нетто (кг)': [95, 100, 105, 115],
                'Габарити ВхШхД (мм)': ['850x450x650', '925x450x650', '1000x450x650', '1075x450x650'],
                'Мінімальна висота димаря (м)': 6,
                'Розмір патрубку відводу продуктів згоряння (мм)': 127,
                'Розмір приєднувальних патрубків': 'G2',
            },
        },
    ]
}

potbelly_stove = {
    'Буржуйки': [
        {
            'mixing_type': 'equal',
            'typing_specification_name': 'Тип котла',
            'prices': 7800,
            'title': 'Буржуйка',
            'template_title': '{title} МАРС {power}кВт',
            'template_description': '',
            'template_kwargs': {'title_kwargs': {'power': 'Потужність (кВт)'}, 'description_kwargs': {}},
            'specifications': {
                'Тип палива': fuel_types,
                'Тип топки': 'Відкрита',
                'Потужність (кВт)': 7,
                'Площа обігріву (м.кв)': 70,
                'Камера подвійного згоряння': 'Так',
                'Підключення до димаря': 'Верхнє',
                'Розташування печі-камін': 'Окремо',
                'Габаритні розміри ВхШхГ (мм)': '708х332х570',
                'Розмір патрубку відводу продуктів згоряння (мм)': 108,
                'Вага нетто (кг)': 50,
            },
        }
    ]
}


def create_compact_catalog_data():
    data = {**boilers, **potbelly_stove, **stovepipes_detail}
    with open('compact_catalog_data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    create_compact_catalog_data()
