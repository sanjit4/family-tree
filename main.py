from datetime import date


class Person:
    def __init__(self, first_name, middle_name = None, last_name = None, other_name = None, date_of_birth = None, date_of_death = None, place_of_birth:str = None, address:str = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.other_name = other_name
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death
        self.place_of_birth = place_of_birth
        self.address = address
        self.relationships = []

    def make_relationship(self, relationship_type:str, other_person = None, start_date = None, end_date = None):
        relationship = {'other_person': other_person, 'relationship_type': relationship_type, 'start_date': start_date, 'end_date': end_date}
        self.relationships.append(relationship)
    
    def view_family(self):
        return self.relationships
    
    def view_relationship(self, other_person):
        for relationship in self.relationships:
            # print(relationship.get(other_person))
            # if relationship.get(other_person) == other_person:
            if relationship.get('other_person') == other_person:
                return relationship
        return None


def main():
    person1 = Person(first_name="John", last_name="Doe", date_of_birth=date(1990, 1, 1))
    person2 = Person(first_name="Jane", last_name="Smith", date_of_birth=date(1992, 2, 2))
    person3 = Person(first_name="Janice", last_name="Doe", date_of_birth=date(2020, 3, 3))

    person1.make_relationship("husband", person2, start_date=date(2010, 1, 1))
    person1.make_relationship("daughter", person3)

    # print(person1.view_close_relationships())
    # print(person1.view_relationship(person2))
    print(person1.view_relationship(person3))


if __name__ == "__main__":
    main()