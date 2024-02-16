import itertools
import json
from pprint import pprint
from typing import Iterable

with open('compact_catalog_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

big_data: dict = {}

for category, products in data.items():
    big_data.setdefault(category, {})

    for title, attributes in products.items():
        template = attributes.pop('Шаблон')
        single_attrs: dict = {}
        iterable_attrs: dict = {}
        dependent_attrs: dict = {}

        if category == 'Твердопаливні котли' or category == 'Буржуйки':
            for name, value in attributes.items():
                if not isinstance(value, Iterable) or isinstance(value, str):
                    single_attrs.setdefault(name, value)
                    continue
                iterable_attrs.setdefault(name, value)

            if iterable_attrs:
                for values in zip(*iterable_attrs.values()):
                    single_attrs.update({name: value for name, value in zip(iterable_attrs.keys(), values)})

                    big_data[category].setdefault(
                        template.format(title=title, power=single_attrs['Потужність (кВт)']),
                        single_attrs.copy(),
                    )
            else:
                big_data[category].setdefault(
                    template.format(title=title, power=single_attrs['Потужність (кВт)']),
                    single_attrs.copy(),
                )

        else:
            for name, value in attributes.items():
                if not isinstance(value, Iterable) or isinstance(value, str):
                    single_attrs.setdefault(name, value)
                    continue

                if isinstance(value, dict):
                    dependent_attrs.setdefault(name, value)
                    continue

                iterable_attrs.setdefault(name, value)

            for type_ in attributes.get('Тип', ''):
                for key, value in dependent_attrs.items():
                    iterable_attrs.setdefault(key, value[type_])

            mixed_values = list(itertools.product(*iterable_attrs.values()))

            for mixed_values_ in mixed_values:
                single_attrs.update({name: value for name, value in zip(iterable_attrs.keys(), mixed_values_)})

                name_components = {
                    'title': title,
                    'length': single_attrs.get('Довжина (мм)'),
                    'steel': single_attrs.get('Сталь'),
                    'thickness': single_attrs.get('Товщина сталі (мм)'),
                    'diameter': single_attrs.get('Діаметр (мм)'),
                    'corner': single_attrs.get('Кут'),
                }
                name_components = {key: value for key, value in name_components.items() if value is not None}
                big_data[category].setdefault(
                    template.format(**name_components),
                    single_attrs.copy(),
                )

pprint(big_data)
