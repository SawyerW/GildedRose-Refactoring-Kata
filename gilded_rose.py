# -*- coding: utf-8 -*-
import logging
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.name == "Aged Brie": self.agedBrie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros": self.sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert": self.backstage(item)
            elif item.name == "Conjured Mana Cake": self.conjured(item)
            else: self.regularItem(item)

    def regularItem(self, item):
        if item.quality > 50:
            logging.warning(f"Product quality of {item.name} is more than 50, pls check.")
        elif item.quality < 0:
            logging.warning(f"Product quality of {item.name} is negative, pls check.")
        elif 50 >= item.quality >= 2:
            if item.sell_in <= 0:
                item.quality -= 2
            else:
                item.quality -= 1
        elif item.quality == 1:
                item.quality = 0
        item.sell_in -= 1

    def agedBrie(self, item):
        if item.quality > 50:
            logging.warning(f"Product quality of {item.name} is more than 50, pls check.")
        elif item.quality < 0:
            logging.warning(f"Product quality of {item.name} is negative, pls check.")
        elif item.quality < 50:
            item.quality += 1
        item.sell_in -= 1

    def sulfuras(self, item):
        if item.quality != 80:
            logging.warning(f"Product quality of {item.name} is not 80, pls check.")
        else:
            pass

    def conjured(self, item):
        if item.quality > 50:
            logging.warning(f"Product quality of {item.name} is more than 50, pls check.")
        elif item.quality < 0:
            logging.warning(f"Product quality of {item.name} is negative, pls check.")
        elif 50 >= item.quality >= 4:
            if item.sell_in <= 0:
                item.quality -= 4
            else:
                item.quality -= 2
        elif item.quality == 3:
            if item.sell_in <= 0:
                item.quality = 0
            else:
                item.quality -= 2
        elif item.quality <= 2:
            item.quality = 0
        item.sell_in -= 1


    def backstage(self, item):
        if item.quality > 50:
            logging.warning(f"Product quality of {item.name} is more than 50, pls check.")
        elif item.quality < 0:
            logging.warning(f"Product quality of {item.name} is negative, pls check.")
        elif item.quality <= 47:
            if item.sell_in > 10:
                item.quality += 1
            elif 10 >= item.sell_in > 5:
                item.quality += 2
            elif 5 >= item.sell_in > 0:
                item.quality += 3
            elif item.sell_in <= 0:
                item.quality = 0
        elif 50 > item.quality >= 48:
            if item.sell_in > 10:
                item.quality += 1
            elif 10 >= item.sell_in > 5:
                item.quality = 50
            elif 5 >= item.sell_in > 0:
                item.quality = 50
            elif item.sell_in <= 0:
                item.quality = 0
        item.sell_in = item.sell_in - 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

