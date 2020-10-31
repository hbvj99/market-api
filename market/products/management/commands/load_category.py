from django.core.management import BaseCommand

from ...models import Category

CATEGORIES_TYPE = [
    {"Apparels & Accessories": "aa"},
    {"Automobiles ": "a"},
    {"Beauty & Health": "ah"},
    {"Books & Learning": "bl"},
    {"Business & Industrial": "bi"},
    {"Computer & Peripherals": "cp"},
    {"Electronics": "e"},
    {"Events & Happenings": "eh"},
    {"Home, Furnishing & Appliances ": "hfa"},
    {"Mobile & Accessories ": "ma"},
    {"Music Instrument": "mi"},
    {"Pets & Pet Care": "ppc"},
    {"Real Estate ": "re"},
    {"Services": "s"},
    {"Sports & Fitness": "sf"},
    {"Toys & Video Games": "tvg"},
    {"Travel, Tour & Packages": "ttp"},
    {"Others": "o"}
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for category in CATEGORIES_TYPE:
            for name in category:
                Category.objects.get_or_create(name=name, code=category.get(name))
        print('Successfully loaded Category!')
