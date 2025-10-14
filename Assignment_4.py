class Profile:
    """
        A "Linked-in like" profile. 

        Attributes:
            name - a string
            title - a string
            company - a string
            connections - a list of profiles
            employment_history - a list of tuples of the form
                                 (title, company, start year, finish year)
                                 e.g. ("VP of Engineering", "Ford", 1998, 2010)
            optionally, you could also add an education attribute....
            education - a list of tuples of the form
                        (degree, school, start year, finish year)
                        e.g. ("Bachelors of Science, Computer Science",
                              "Northwestern University",
                              2004,
                              2008)


        Methods:
            self.__init__
                takes 3 strings as input (n, t, c) with default values of ""
                    representing a name, title and company
                creates an instance of a profile with the name title and
                    company that were given as input. Connections and
                    employment_history should be initialized to an empty list
            self.__str__
                returns a string representation of the object including
                    information from all attributes
            self.add_connection
                takes another profile instance as input and adds that
                    profile to the connections attribute. However, only
                    add the profile if its not already included in the
                    connections attribute. That is, we don't want duplicates
                    in the list. 
    """

    def __init__(self, n="", t="", c=""):
        """ Creates an instance of a profile. """
        self.name = n
        self.title = t
        self.company = c
        self.connections = []
        self.employment_history = []
        self.education = []

    def __str__(self):
        """ Returns a string representation of the profile."""
        profile_str = "Profile Information:\n"
        profile_str += f"Name: {self.name if self.name else 'N/A'}\n"
        profile_str += f"Current Title: {self.title if self.title else 'N/A'}\n"
        profile_str += f"Current Company: {self.company if self.company else 'N/A'}\n"

        profile_str += "Connections:\n"
        if self.connections:
            for conn in self.connections:
                profile_str += f"  - {conn.name} ({conn.title} at {conn.company})\n"
        else:
            profile_str += "  None\n"

        profile_str += "Employment History:\n"
        if self.employment_history:
            for job in self.employment_history:
                title, company, start, finish = job
                profile_str += f"  - {title} at {company} ({start} - {finish})\n"
        else:
            profile_str += "  None\n"

        profile_str += "Education:\n"
        if hasattr(self, 'education') and self.education:
            for edu in self.education:
                degree, school, start, finish = edu
                profile_str += f"  - {degree}, {school} ({start} - {finish})\n"
        else:
            profile_str += "  None\n"

        return profile_str

    def add_connection(self, a_profile):
        """if the input profile is not already connected to self,
        connect them."""
        if a_profile not in self.connections:
            self.connections.append(a_profile)
        else:
            return "already connected"


def connect(p1, p2):
    """
    connect takes two profile objects and connects them. That is, adds
    each to the other's list of connections.

    Inputs: Two profile instances.

    Returns: None
    """
    if p1 not in p2.connections and p2 not in p1.connections:
        p1.add_connection(p2)
        p2.add_connection(p1)


def where_did_they_work_together(p1, p2):
    """
    where_did_they_work_together determines whether and where p1 and p2 overlapped
    in their employment history. That is, were they at the same company in
    overlapping years.

    Inputs: Two profile instances.

    Returns: The company name if they worked together. False if they did not.

    Hint: Nested For Loops
    """
    for role, company, start, end in p1.employment_history:
        for role2, company2, start2, end2 in p2.employment_history:
            if company == company2 and start <= end2 and start2 <= end:
                return company
    return False


def shortest_path(p1, p2):
    """
    shortest_path determines the distance (and associated path) between two
    profiles. For example, if p2 appears in p1.connections, the distance is
    1 and the path simply contains p1.name and p2.name. See asserts for more
    examples. 
    
    Inputs: Two profile instances. 

    Returns: The distance and path between the two input profiles. 
             None if no path is found
    """
    visited = []
    q = [(p1, 0, [p1.name])]
    while q != []:
        profile = q.pop(0)
        curr, dist, path = profile
        visited.append(curr)    #add curr to visited
        if curr.name == p2.name:
            return (dist, path)
        else:
            for connection in curr.connections:
                if connection not in visited:
                    new_path = path + [connection.name]
                    q.append((connection, dist + 1, new_path))
    return None









    pass


# EXTENSION #1 - this function would be an extension, but not extra credit
def shortest_path_to_someone_who(p1, predicate):
    """
    shortest_path determines the distance (and associated path) between p1
    and someone who meets the criteria expressed in the predicate. 
    
    Inputs: A profile instance and a predicate (that takes a profile and returns
    a boolean). 

    Returns: The distance and path between the two input profiles. 
             None if no path is found
    """
    pass


# some profiles to work with
sara = Profile("Sara Sood", "Professor of Computer Science", "Northwestern")
peter = Profile("Peter Zhong", "Software Engineer Intern", "Teladoc Health")
milan = Profile("Milan McGraw", "Consultant", "FEV Consulting")
milan.employment_history = [("some role", "some company", 1995, 2001),
                            ("another role", "another company", 2001, 2009),
                            ("yet another role", "yet another company", 2009, 2018)]
masum = Profile("Masum Patel", "Consultant", "Deloitte")
masum.employment_history = [("another role", "another company", 1995, 1996),
                            ("yet another role", "yet another company", 1996, 2010)]
kris = Profile("Kris Hammond", "Professor of Computer Science", "Northwestern")
bob = Profile("Bob", "Northwestern")

connect(sara, peter)
connect(sara, peter)  # adding this to make sure no duplicates in connections
connect(peter, milan)
connect(masum, milan)
connect(masum, kris)
connect(milan, kris)


assert len(sara.connections) == 1, "connect test 1"
assert len(milan.connections) == 3, "connect test 2"
assert milan in kris.connections and kris in milan.connections, "connect test 3"
assert sara not in kris.connections, "connect test 4"
assert where_did_they_work_together(milan, masum) == "yet another company", "where_did_they_work_together test 1"
assert where_did_they_work_together(milan, kris) == False, "where_did_they_work_together test 2"
assert shortest_path(sara, kris) == (3,["Sara Sood", "Peter Zhong", "Milan McGraw", "Kris Hammond"]), "shortest path 1"
assert shortest_path(sara, bob) == None, "shortest path 2"


# uncomment the following two test cases if you decide to complete the optional extension
"""
# find someone connected to sara who works for deloitte
assert shortest_path_to_someone_who(sara,lambda x:
                                         x.company == "Deloitte") == (3,
                                                                      ['Sara Sood',
                                                                       'Peter Zhong',
                                                                       'Milan McGraw',
                                                                       'Masum Patel'])


# find someone connected to sara, who works with sara (but is not herself)
assert shortest_path_to_someone_who(sara,lambda x:
                                         x.company == sara.company
                                         and x.name != sara.name) == (3,
                                                                      ['Sara Sood',
                                                                       'Peter Zhong',
                                                                       'Milan McGraw',
                                                                       'Kris Hammond'])
"""
print("All tests passed!")

