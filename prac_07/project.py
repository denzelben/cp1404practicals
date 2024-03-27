class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a project with the provided attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """Determine if this project has a lower priority than another project."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Determine if this project has the same priority as another project."""
        return self.priority == other.priority

    def __repr__(self):
        """Return a string representation of the projects."""
        return str(f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                   f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%")

    def __str__(self):
        """Return a string representation of the project instance."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"