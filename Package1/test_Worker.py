from unittest import TestCase
from Worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.jeffrey = Worker("jeffrey", "aizenhaur", 1970, 7, 30, "2 ,dizzengof ,tel aviv", "il")
        self.jeffrey_notborn = Worker("jeffrey", "aizenhaur", 21000, 7, 30, "2 ,dizzengof ,tel aviv", "il")
        self.jeffrey_sameyear = Worker("jeffrey", "aizenhaur", 2022, 7, 30, "2 ,dizzengof ,tel aviv", "il")
        self.jeffrey_future_date = Worker("jeffrey", "aizenhaur", 2022, 4, 14, "2 ,dizzengof ,tel aviv", "il")
        self.jeffrey_future_date1 = Worker("jeffrey", "aizenhaur", 2022, 3, 12, "2 ,dizzengof ,tel aviv", "il")
        self.jeffrey_future_date2 = Worker("jeffrey", "aizenhaur", 2022, 4, 12, "2 ,dizzengof ,tel aviv", "il")
    def test_full_name(self):
        self.assertTrue(self.jeffrey.full_name() == "jeffrey aizenhaur")

    def test_age(self):
        self.assertIn( "52" , self.jeffrey.age() )

    def test_age1(self):
        self.assertFalse(self.jeffrey_notborn.age())

    def test_age2(self):
        self.assertIn("0", self.jeffrey_sameyear.age())


    def test_days_to_birthday(self):
        self.assertIn("1", self.jeffrey_future_date.days_to_birthday())

    def test_days_to_birthday_1(self):
        self.assertIn("333", self.jeffrey_future_date1.days_to_birthday())

    def test_days_to_birthday_2(self):
        self.assertIn()



