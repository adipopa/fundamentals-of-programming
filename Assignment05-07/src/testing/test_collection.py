from unittest import TestCase

from structures.collection import *

from domain.student import Student


class TestCollection(TestCase):

    def setUp(self):
        self.__items = [
            {'id': 1, 'name': 'Thomas', 'group': 916},
            {'id': 2, 'name': 'Jack', 'group': 914},
        ]

    def test_add(self):
        student1 = Student(1, "Jerry", 913)
        student2 = Student(2, "Bob", 918)
        student3 = Student(3, "Daniel", 914)

        collection = Collection()
        collection.add(student1)
        collection.add(student2)
        collection.add(student3)

        self.assertEqual(len(collection), 3)

        self.assertEqual(collection[0], student1)
        self.assertEqual(collection[1], student2)
        self.assertEqual(collection[2], student3)

    def test_gnome_sort(self):
        unsorted_items = self.__items[:]
        sorted_items = gnome_sort(self.__items, sort_function=lambda item_a, item_b: item_a['name'] <= item_b['name'])
        self.assertEqual(len(sorted_items), 2)
        self.assertEqual(sorted_items[0], unsorted_items[1])

    def test_filter_items(self):
        filtered_items = filter_items(self.__items, filter_function=lambda item: item['name'] == 'Jack')
        self.assertEqual(len(filtered_items), 1)
        self.assertEqual(filtered_items[0], self.__items[1])
