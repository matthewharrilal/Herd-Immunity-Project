 # ‘’'
 #   Virus objects will infect persons
 #
 #   _____Attributes______:
 #
 #   name: String: Contains virus name.
 #
 #   infection_rate: Int. The chance that the virus spreads to a new human.
 #
 #   kill_rate: The chance that the virus kills the host.
 #
 #   _____Methods_____:
 #
 #   __init__(self, name, infection_rate, kill_rate)
 #       -All parameters should be set to the passed value.
 #   ‘’'

class Virus(object):

    def __init__(self, virus_name, mortality_rate, basic_repro_num):
        self.name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repo_num = basic_repro_num
