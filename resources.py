
class Resource:
    pass

class Building_resource(Resource):
    res_type = 'building'

class Stone(Building_resource):
    name = 'stone'

class Wood(Building_resource):
    name = 'wood'

class Wheat(Building_resource):
    name = 'wheat'


resource_list = [
    Wood,
    Stone,
    Wheat
]

class Resource_storage:
    def __init__(self, initial_resources=None):
        """Any collection of resources, owned by player or tile

        Args:
            initial_resources (dict): key being the resource name and value the amount to start with.
        """
        self.resources = {}
        for resource in resource_list:
            self.resources[resource.name] = 0
        if initial_resources != None:
            self.add_resources(initial_resources)

    def add_resources(self, resource_dict):
        """Adds resources to storage

        Args:
            resource_dict (dict): key being the resource name and value the amount to start with.
        """
        for resource, amount in resource_dict.items():
            self.resources[resource] += amount