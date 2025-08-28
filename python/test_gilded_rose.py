# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    # Add comprehensive tests for all business rules
    def test_normal_item_quality_decreases(self):
        """Normal items should decrease in quality and sell_in by 1 each day"""
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_normal_item_degrades_twice_after_sell_date(self):
        """Normal items should degrade twice as fast after sell date"""
        items = [Item("Normal Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)  # Decreased by 2
        self.assertEqual(-1, items[0].sell_in)

    def test_quality_never_negative(self):
        """Quality should never go below 0"""
        items = [Item("Normal Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_quality(self):
        """Aged Brie should increase in quality as it ages"""
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_aged_brie_increases_twice_after_sell_date(self):
        """Aged Brie should increase twice as fast after sell date"""
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_quality_never_exceeds_50(self):
        """Quality should never exceed 50 for most items"""
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_changes(self):
        """Sulfuras should never change quality or sell_in"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_passes_increase_normally(self):
        """Backstage passes increase by 1 when more than 10 days"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_increase_by_two(self):
        """Backstage passes increase by 2 when 6-10 days"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_passes_increase_by_three(self):
        """Backstage passes increase by 3 when 1-5 days"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_passes_worthless_after_concert(self):
        """Backstage passes should be worthless after concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_items_degrade_twice_as_fast(self):
        """Conjured items should degrade twice as fast as normal items"""
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)  # Decreased by 2

    def test_conjured_items_degrade_four_times_after_sell_date(self):
        """Conjured items should degrade 4x as fast after sell date"""
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)  # Decreased by 4

    def test_conjured_quality_never_negative(self):
        """Conjured items quality should never go below 0"""
        items = [Item("Conjured Mana Cake", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()