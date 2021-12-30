from game_board import Game_board

class Land_board:
    '''
    Can be farm board (starter) or expansion
    '''
    def __init__(self, land_type='starter'):
        self.land_type = land_type
        if land_type == 'starter':
            self.spaces = [[None, None], [None, None], ['C', None]] # 2 cols, 3 rows.
        else:
            self.spaces = [[None], [None], [None]] # 1 col, 3 rows.
        self.width = len(self.spaces[0])


class Player_land:
    '''
    Manager class to handle land for a player. What land plates they own and what they contain.
    '''
    def __init__(self):
        self.farm_boards = [Land_board()]

    def spaces_array(self):
        '''
        We have to transpose it twice to attach it left to right 
        (as boards are in farm_boards), but then return spaces by rows, top to bottom.
        '''
        spaces = []
        for l in self.farm_boards:
            spaces.extend(list(zip(*l.spaces)))
        return list(zip(*spaces))
    
    def status(self):
        return {
            'boards': [ l.land_type for l in self.farm_boards ],
            'spaces': self.spaces_array()
        }

class Player:
    def __init__(self, initiative=False):
        self.initiative = initiative
        self.build_res = {
            'stone': 0,
            'wood': 0,
            'wheat': 0
        }
        self.land = Player_land()

    def set_initiative(self, init):
        self.initiative = init
    
    def status(self):
        return {
            'initiative': self.initiative,
            'building_resources': self.build_res,
            'land': self.land.status()
        }



class Game_engine:
    def __init__(self):
        self._new_game()
    
    def _new_game(self):
        self.p1 = Player(initiative=True)
        self.p2 = Player()
        self.game_board = Game_board()


    def status(self):
        pass

    def refill_game_board(self):
        self.game_board.refill()


class Term_game:
    '''
    Wrapper around Game to make it playable through the terminal.
    '''
    def __init__(self, game=None):
        if game == None:
            self.game = Game_engine()
        else:
            self.game = game
    
    def start(self):
        '''
        Handles the main input loop
        '''
        inp = ''
        while inp != 'q':
            if inp == 'r':
                self.game.refill_game_board()
            self.display_status()
            #self.display_menu()
            inp = input('>>>')
    
    def display_status(self):
        self.display_player(self.game.p2)
        self.display_player(self.game.p1)
        self.display_game_board(self.game.game_board)

    def display_player(self, p):
        p_s = p.status() # Status in dict form
        # First we print land
        print("Land:")
        print('='* 30)
        for row in p_s['land']['spaces']:
            spaces_str_arr = []
            for space in row:
                if space == None:
                    spaces_str_arr.append('    ')
                else:
                    spaces_str_arr.append(space + '   ')
            print('|' + '|'.join(spaces_str_arr) + '|')
            print('-'*30)
        type_str_arr = []
        for land_type in p_s['land']['boards']:
            if land_type == 'starter':
                type_str_arr.extend(['main'] * 2)
            else:
                type_str_arr.append(land_type) # Should be 4 characters
        print('|' + '|'.join(type_str_arr) + '|')
        print('='* 30)
        print('Initiative:', p_s['initiative'])
        stone = p_s['building_resources']['stone']
        wood = p_s['building_resources']['wood']
        wheat = p_s['building_resources']['wheat']
        print(f'Resources: Stone({stone}) Wood({wood}) Wheat({wheat})')
        #print(p_s)
    
    def display_game_board(self, game_board):
        b_s = game_board.status()
        print('Game board:')
        print('='* 30)
        print(b_s)


def main():
    term_game = Term_game()
    term_game.start()


if __name__ == '__main__':
    main()



