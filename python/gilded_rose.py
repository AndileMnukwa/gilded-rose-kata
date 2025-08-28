# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Skip Sulfuras - it never changes
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
                
            # Decrease sell_in for all items except Sulfuras
            item.sell_in -= 1
            
            # Handle different item types
            if item.name == "Aged Brie":
                self._update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)
            elif item.name == "Conjured Mana Cake":
                self._update_conjured_item(item)
            else:
                self._update_normal_item(item)
    
    def _update_aged_brie(self, item):
        """Aged Brie increases in quality as it ages"""
        if item.quality < 50:
            item.quality += 1
            # After sell date, increases twice as fast
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1
    
    def _update_backstage_passes(self, item):
        """Backstage passes have complex quality rules based on sell_in"""
        if item.sell_in < 0:
            # After concert, passes are worthless
            item.quality = 0
        elif item.quality < 50:
            item.quality += 1  # Base increase
            
            # Additional increases based on days to concert
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1  # 10 days or less: +2 total
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1  # 5 days or less: +3 total
    
    def _update_conjured_item(self, item):
        """Conjured items degrade twice as fast as normal items"""
        degradation = 2
        if item.sell_in < 0:
            degradation = 4  # After sell date, degrade 4x as fast
            
        item.quality = max(0, item.quality - degradation)
    
    def _update_normal_item(self, item):
        """Normal items decrease in quality over time"""
        if item.quality > 0:
            item.quality -= 1
            # After sell date, quality degrades twice as fast
            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)