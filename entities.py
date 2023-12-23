from collections import UserDict
from datetime import date, datetime


class Field:
    mandatory = False

    def __init__(self, value):
        self.__value = value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, ind):
        self.__value = ind

class Name(Field):
    mandatory = True


class Phone(Field):

    def __init__(self, value):
        # super().__init__(value)
        self.phone_validate(value)
        self.__value = value


    def phone_validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Not correct No')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, ind):
        self.phone_validate(ind)
        self.__value = ind

class Birthday(Field):

    def __init__(self, birth_date):
        self.__value = self.birth_validate(birth_date)

    def birth_validate(self, birth_date):
        try:
            result = datetime.strptime(birth_date, '%d.%m.%Y')
            return result
        except ValueError:
            raise ValueError('Not correct format of birth date. Should be like: 16.02.1990')


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, birth_date):
        self.__value = self.birth_validate(birth_date)


class Record:

    def __init__(self, name, birth_date=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birth_date
        if birth_date:
            self.birthday = Birthday(birth_date)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError('We dont have such No in the record')


    def remove_phone(self, phone_to_del):
        for phone in self.phones:
            if phone.value == phone_to_del:
                self.phones.remove(phone)


    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return Phone(phone_to_find)  #  this A-book method returns Record inst

    def days_to_birthday(self):
        try:
            if self.birthday.value:
                today = date.today()
                next_birthday = date(year=today.year, month=self.birthday.value.month, day=self.birthday.value.day)

                if today > next_birthday: # if we already had bday this year
                    next_birthday = date(today.year + 1, self.birthday.value.month, self.birthday.value.day)

                days_left = (next_birthday - today).days
                return days_left
        except:
            return 'This Record does not have Information on birthday'

    def __str__(self):
        result_str = 'Record name: '+ self.name.value + ' '
        if self.phones:
            phones_list = 'Phones_list: '
            for phone in self.phones:
                phones_list += phone.value + ' '
            result_str += phones_list
        if self.birthday:
            birthday_val = 'Birthday: '
            birthday_val += str(self.birthday.value)
            result_str += birthday_val

        return result_str

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)


    def delete(self, name_to_del):
        self.data = {n: rec for n, rec in self.data.items() if n != name_to_del}

    def print_rec(self, lines_per_time=2):
        iter_address_book = iter(self.items())
        while True:
            try:
                for _ in range(lines_per_time):
                    line = next(iter_address_book)
                    name, rec = line  # in name we store name of the record in str format(not object) in rec- Record obj
                    print(rec)
                print()
            except StopIteration:
                break


# rec1 = Record('rec1_1')
# rec2 = Record('rec2_2', '01.03.1988')
# rec3 = Record('rec3_3')
# rec4 = Record('rec4_4', '01.05.1996')
# rec5 = Record('rec5_5', '01.02.2000')
#
# rec1.add_phone('5555555555')
# rec1.add_phone('1234567890')
#
# rec4.add_phone('1234567890')
# rec4.add_phone('0987654321')
# rec4.add_phone('7777777777')
#
# a_book = AddressBook()
#
# rec_list = [rec1, rec2, rec3, rec4, rec5]
# for i in rec_list:
#     a_book.add_record(i)
#
# print(rec4.days_to_birthday())
# a_book.print_rec(2)




