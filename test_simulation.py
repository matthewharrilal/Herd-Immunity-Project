import pytest
from simulation import Simulation


def setup_for_test():
    simulation = Simulation(100, 0.90, "Ebola", 0.70, 0.25, 10)
    return simulation


def test_setup_population():
    simulation = setup_for_test()

    assert len(simulation.population) == 100
    assert simulation.total_infected == 10
