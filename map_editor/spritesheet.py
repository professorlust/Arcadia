import pygame, os, json

class Images:
    def __init__(self, program, image_path):
        self.image = pygame.image.load(image_path).convert()
        self.program = program

    def get_image(self, x, y):
        image32 = pygame.Surface((32, 32))
        image32.blit(self.image, (0, 0), (x*32, y*32, 32, 32))
        image32 = pygame.transform.scale(image32, (self.program.opt.TILE_SIZE, self.program.opt.TILE_SIZE))
        image32.set_colorkey((0,0,0))
        return image32

class Spritesheet:
    def __init__(self, program):
        self.program = program
        self.images = dict()
# BASICTILES_____________________________________________________________________________________________________
        image_path = os.path.join(self.program.path_img,"basictiles" + self.program.opt.IMAGE_FORMAT)
        self.basictiles = Images(self.program, image_path)
        self.images["basictiles"] = dict()
        get_image = self.basictiles.get_image

        coords = json.load(open(os.path.join(self.program.path_img,"basictiles" + self.program.opt.JSON_FORMAT)))
        for item_type, item_coords in coords.items():
            self.images["basictiles"][item_type] = dict()
            for code,coord in item_coords.items():
                if code == "_cumment": continue
                self.images["basictiles"][item_type][code] = get_image(coord["x"],coord["y"])
# BASICTILES_____________________________________________________________________________________________________
        image_path = os.path.join(self.program.path_img,"characters" + self.program.opt.IMAGE_FORMAT)
        self.characters = Images(self.program, image_path)
        self.images["characters"] = dict()
        get_image = self.characters.get_image

        coords = json.load(open(os.path.join(self.program.path_img,"characters" + self.program.opt.JSON_FORMAT)))
        for item_type, item_coords in coords.items():
            self.images["characters"][item_type] = dict()
            for code,coord in item_coords.items():
                if code == "_cumment": continue
                self.images["characters"][item_type][code] = get_image(coord["x"],coord["y"])
