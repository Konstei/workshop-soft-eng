# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            #       1 for normal,       2 for conjured;                         rate doubles if sellout date passes
            rate = (      1       + item.name.startswith("Conjured "))      *    ((item.sell_in <= 0) + 1)

            match item.name:
                case "Aged Brie":
                    item.quality = min(item.quality + 1, 50)
                
                case "Sulfuras, Hand of Ragnaros":
                    item.sell_in += 1 + (item.sell_in < 0)
                
                case "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in <= 0:       # left this one at 0 because tickets are still worth something on the day of the event up until it ends
                        item.quality = 0
                    elif item.sell_in <= 6:     # when 5 days left, aka since the 6th day before the event
                        item.quality += 3
                    elif item.sell_in <= 11:    # when 10 days left, aka since the 11th day before the event
                        item.quality += 2
                    else:
                        item.quality += 1
                
                case _:
                    item.quality = max(0, item.quality - rate)
            # end

            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
