"""
Stratigo
"""

import random
import arcade
#add logic about landing in an ocupied space
#add movement restrictions
#add start up (probalby a column of pieces that you can pull from to set up you board)
#add pass screen
#add special spy enhancments and bomb/ flag restrictions
#add win screen
#maybe add suspicioun clicking.. stretch

SCALE = 2

SCREEN_WIDTH = 480*SCALE
SCREEN_HEIGHT = 400*SCALE

SCREEN_TITLE = "Stratigo"

PIECE_SIZE = (SCREEN_WIDTH/15)*SCALE

BOARD = {
    (1,1) : 'open', (1,2) : 'open', (1,3) : 'open', (1,4) : 'open', (1,5) : 'open',(1,6) : 'open', (1,7) : 'open', (1,8) : 'open', (1,9) : 'open', (1,10) : 'open',
    (2,1) : 'open', (2,2) : 'open', (2,3) : 'open', (2,4) : 'open', (2,5) : 'open',(2,6) : 'open', (2,7) : 'open', (2,8) : 'open', (2,9) : 'open', (2,10) : 'open',
    (3,1) : 'open', (3,2) : 'open', (3,3) : 'open', (3,4) : 'open', (3,5) : 'open',(3,6) : 'open', (3,7) : 'open', (3,8) : 'open', (3,9) : 'open', (3,10) : 'open',
    (4,1) : 'open', (4,2) : 'open', (4,3) : 'open', (4,4) : 'open', (4,5) : 'open',(4,6) : 'open', (4,7) : 'open', (4,8) : 'open', (4,9) : 'open', (4,10) : 'open',
    (5,1) : 'open', (5,2) : 'open', (5,3) : 'blocked', (5,4) : 'blocked', (5,5) : 'open',(5,6) : 'open', (5,7) : 'blocked', (5,8) : 'blocked', (5,9) : 'open', (5,10) : 'open',
    (6,1) : 'open', (6,2) : 'open', (6,3) : 'blocked', (6,4) : 'blocked', (6,5) : 'open',(6,6) : 'open', (6,7) : 'blocked', (6,8) : 'blocked', (6,9) : 'open', (6,10) : 'open',
    (7,1) : 'open', (7,2) : 'open', (7,3) : 'open', (7,4) : 'open', (7,5) : 'open',(7,6) : 'open', (7,7) : 'open', (7,8) : 'open', (7,9) : 'open', (7,10) : 'open',
    (8,1) : 'open', (8,2) : 'open', (8,3) : 'open', (8,4) : 'open', (8,5) : 'open',(8,6) : 'open', (8,7) : 'open', (8,8) : 'open', (8,9) : 'open', (8,10) : 'open',
    (9,1) : 'open', (9,2) : 'open', (9,3) : 'open', (9,4) : 'open', (9,5) : 'open',(9,6) : 'open', (9,7) : 'open', (9,8) : 'open', (9,9) : 'open', (9,10) : 'open',
    (10,1) : 'open', (10,2) : 'open', (10,3) : 'open', (10,4) : 'open', (10,5) : 'open',(10,6) : 'open', (10,7) : 'open', (10,8) : 'open', (10,9) : 'open', (10,10) : 'open',
}

RANK = ['10','9','8','6','5','4','3','2','1','11','0']
FREQUENCY = [1,1,2,3,4,4,4,5,8,1,6,1]
TEAM = ["red", "blue"]

class Piece(arcade.Sprite):
    def __init__(self, team, rank, scale = SCALE):
       
        self.team = team
        self.rank = rank
        self.image_file_name = f"./images/{self.team}_{self.rank}.png"

        
       
        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")




class WholeBoard(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        #all the pieces on the board
        self.red_list = None
        self.blue_list = None
        self.background_color = arcade.color.AMAZON
        #the piece that is currently being moved
        self.picked_up_piece = None
        #where the peice goes abck to if it's dropped
        self.picked_up_piece_original_position = None


    def setup(self):
        """call to reset the game"""
        self.picked_up_piece = ""
        self.picked_up_piece_original_position = ""


        self.red_list = self.build_team("red")
        self.blue_list = self.build_team("blue")
        # self.space_list = []
        #create all the pieces
        #shuffle the pieces
        
        #place the pieces on the board
        for i, piece in enumerate(self.red_list):
            piece.position = (PIECE_SIZE*.75), (PIECE_SIZE*.75+i*.0625*PIECE_SIZE)
            
        for i, piece in enumerate(self.blue_list):
            piece.position = (SCREEN_WIDTH- PIECE_SIZE*.75), (PIECE_SIZE*.75+i*.0625*PIECE_SIZE)
             
            

    def build_team(self, color):
        """make a team"""
        self.color = color
        self.team_list = arcade.SpriteList()
        for i, unit in enumerate(RANK):
            for _ in range(FREQUENCY[i-1]):
                piece = Piece(color, unit)
                
                self.team_list.append(piece)
        return self.team_list

    def on_draw(self):
        self.clear()
        # self.board.draw()
        self.red_list.draw()   
        self.blue_list.draw()
        

    def move_piece(self, x, y):
        """move the piece to the new position"""
        # cards = arcade.get_sprites_at_point((x, y), self.card_list)
        # if self.picked_up_piece:
        #     self.picked_up_piece.center_x = x
        #     self.picked_up_piece.center_y = y

    def capture_piece(self, x, y, lifted_piece, occupying_piece):
        """capture the piece at the given position"""
        # if lifted_piece and occupying_piece.rank != #the same team:
        #    >>
        if occupying_piece == '11': 
            if lifted_piece == '3':
                #remove bomb
                pass
            else:
                #kill lifted piece
                pass
        elif lifted_piece == '1' and occupying_piece == '10':
            #kill occupying piece
            pass
        else:
            if lifted_piece > occupying_piece:
                #kill occupying piece
                pass
            elif lifted_piece < occupying_piece:
                #kill lifted piece
                pass
            elif lifted_piece == occupying_piece:
                #kill both
                pass
            else:
                print("you broke the game by getting to an impossible match up")
                pass

    def kill_piece(self, piece_to_kill):
        """remove the piece from the board"""
        # self.piece_list.remove(piece)
    def on_mouse_press(self, x, y, button, key_modifiers):
        red_pieces = arcade.get_sprites_at_point((x, y), self.red_list)
        blue_pieces = arcade.get_sprites_at_point((x, y), self.blue_list)

        if red_pieces:
            self.picked_up_piece = red_pieces[-1]
            self.picked_up_piece_original_position = (self.picked_up_piece.center_x, self.picked_up_piece.center_y)

        elif blue_pieces:
            self.picked_up_piece = blue_pieces[0]
            self.picked_up_piece_original_position = (self.picked_up_piece.center_x, self.picked_up_piece.center_y)

    def on_mouse_motion(self, x, y, dx, dy):
        """called whenever the mouse moves"""
        if self.picked_up_piece:
            self.picked_up_piece.center_x += dx
            self.picked_up_piece.center_y += dy
    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if not self.picked_up_piece:
            return
        self.picked_up_piece = None
        


def main():
    window = WholeBoard()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

