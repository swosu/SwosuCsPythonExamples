class RaceTime:
    def __init__(self, start_time, end_time, distance, name):
        """
         start_time: Race start time. String w/ format 'hours:minutes'.
         end_time: Race end time. String w/ format 'hours:minutes'.
         distance: Distance of race in miles.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.distance = distance
        self.name = name
    # ...
    def print_time(self):
        #total run time hours was:
        #grab the hours from the start time and end time
        start_hour = int(self.start_time.split(':')[0])
        end_hour = int(self.end_time.split(':')[0])
        elapsed_hours = end_hour - start_hour

        #total run time minutes was:
        #grab the minutes from the start time and end time
        start_minute = int(self.start_time.split(':')[1])
        end_minute = int(self.end_time.split(':')[1])
        elapsed_minutes = end_minute - start_minute

        print(f'{self.name} ran {self.distance:.2f} miles in {elapsed_hours} hours and {elapsed_minutes} minutes.')

# The race times of marathon contestants
time_jason = RaceTime('3:15', '7:45', 26.21875, 'Jason')
time_bobby = RaceTime('3:15', '6:30', 26.21875, 'Bobby')

time_jason.print_time()
time_bobby.print_time()