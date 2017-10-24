import random
from virus import Virus


class Person(object):
    """
    Person objects will populate the simulation.
    _____Attributes______:
    _id: Int.  A unique ID assigned to each person.
    is_vaccinated: Bool.  Determines whether the person object is vaccinated against
        the disease in the simulation.
    is_alive: Bool. All person objects begin alive (value set to true).  Changed
        to false if person object dies from an infection.
    infection:  None/Virus object.  Set to None for people that are not infected.
        If a person is infected, will instead be set to the virus object the person
        is infected with.
    _____Methods_____:
    __init__(self, _id, is_vaccinated, infected=False):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should create a Virus object and set it as the value for
            self.infection.  Otherwise, self.infection should be set to None.
    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infected to None.
    """

    def __init__(self, _id, is_vaccinated, is_infected=False, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.is_infected = is_infected
        self.infection = infection

    def did_survive_infection(self):
        if self.infection is not None:
            print("I'm Infected With: ", self.infection)
            if random.random() < self.infection.mortality_rate:
                self.is_alive = False
                return False

            self.is_vaccinated = True
            self.infection = None
            self.is_infected = False

            return True

    def get_person_id(self):
        return self._id
