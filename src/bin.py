from math import sqrt


class BinomialVariable:
    def __init__(self, number_of_trials, probability_of_success):
        self.number_of_trials = number_of_trials
        self.probability_of_success = probability_of_success
        if probability_of_success < 0 or probability_of_success > 1 or number_of_trials < 1:
            raise ValueError

    @property
    def mean(self):
        return self.number_of_trials * self.probability_of_success

    @property
    def expected_value_of_x(self):
        return self.mean

    @property
    def variance(self):
        return self.number_of_trials * self.probability_of_success * (1-self.probability_of_success)

    @property
    def stddev(self):
        return sqrt(self.variance)