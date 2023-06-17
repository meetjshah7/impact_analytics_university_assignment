class University:
    """
    University Class used for calculating valid ways to attend the college
    and the chances of missing the graduation ceremony

    The approach for the solution is discussed in README.md 
    """
    def __init__(self, n: int) -> None:
        self.days = n
        self.number_of_ways_to_attend_classes = self.valid_ways_to_attend_classes()
        self.number_of_ways_to_miss_graduation_ceremony = self.ways_to_miss_graduation_ceremony()

    def valid_ways_to_attend_classes(self):
        """Calculates the valid ways to attend classes 

        Args:
            N (int): Total number of days

        Returns:
            int: No. of valid ways to attend the classes
        """

        if self.days < 4:
            return 2 ** self.days
        if self.days == 4:
            return 15

        # Initial data for N=5
        prev1 = 2
        prev2 = 4
        prev3 = 8
        prev4 = 15

        for _ in range(5, self.days + 1):
            current = prev1 + prev2 + prev3 + prev4
            # Update the initial data for next iteration
            prev1, prev2, prev3, prev4 = prev2, prev3, prev4, current

        return current
        
    def ways_to_miss_graduation_ceremony(self):
        """Calculates the no. of ways in which you would miss the graduation ceremony 

        Args:
            N (int): Total number of days

        Returns:
            int: No. of ways in which you would miss the graduation ceremony
        """

        if self.days < 4:
            return 2 ** (self.days-1)
        if self.days == 4:
            return 7

        # Base data for N=5
        prev1 = 1
        prev2 = 2
        prev3 = 4
        prev4 = 7

        for _ in range(5, self.days + 1):
            current = prev1 + prev2 + prev3 + prev4
            # Update initial data for next iteration
            prev1, prev2, prev3, prev4 = prev2, prev3, prev4, current

        return current
