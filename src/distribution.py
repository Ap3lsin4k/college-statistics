from math import sqrt


class Distribution:
    def __init__(self, mean, standard_deviation):
        self.std_dev = standard_deviation
        self.mean = mean

    def __add__(self, other):
        return Distribution(self.mean + other.mean, sqrt(self.std_dev**2 + other.std_dev**2))

    def __sub__(self, other):
        return Distribution(self.mean-other.mean, sqrt(self.std_dev**2 + other.std_dev**2))

    def z(self, other_mean=0):
        return (other_mean - self.mean) / self.std_dev

    @classmethod
    def from_table(cls, *args):
        one_hundred_percents = sum(event.probability for event in args)
        if one_hundred_percents != 1:
            raise ValueError("overall probability must be 100%")

        # weighted average
        mean = sum(event.event_value*event.probability for event in args)

        variance = sum((mean - event.event_value)**2*event.probability for event in args)
        return Distribution(
            mean=mean,
            standard_deviation=sqrt(variance))
