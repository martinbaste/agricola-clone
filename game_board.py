from resources import Resource_storage

def add_res_func(resource, amount=1):
    def res_func(self):
        self.resources.add_resources({resource: amount})
    return res_func


class Game_board_space:
    space_rules = {
        'wood': {
            'refill_func': add_res_func('wood', 3)
        },
        'stones1': {
            'refill_func': add_res_func('stone', 1)
        },
        'stones2': {
            'refill_func': add_res_func('stone', 2)
        }
    }

    def __init__(self, space_type='wood'):
        self.resources = Resource_storage()
        self.name = space_type
        self.rules = self.space_rules.get(space_type, {})
        self._refill_func = self.rules.get('refill_func')

    def refill(self):
        if self._refill_func != None:
            self._refill_func(self)
    
    def status(self):
        return {
            'name': self.name,
            'resources': self.resources.resources
        }


class Game_board:
    space_types = [
        'woodinit',
        'wood',
        'stones1',
        'stones2',
        'fencewood',
        'fencestones',
        'buildres',
        'fenceexpand',
        'buildstall',
        'buildtrough',
        'upgradestall',
        'specialbuild1',
        'specialbuild2',
        'wheat_sheep',
        'pig_sheep',
        'cow_pig',
        'horse_sheep'
    ]

    def __init__(self):
        self.spaces = {
            name: Game_board_space(name) for name in self.space_types
        }

    def status(self):
        return {
            'spaces': [ space.status() for space in self.spaces.values() ]
        }

    def refill(self):
        for space in self.spaces.values():
            space.refill()