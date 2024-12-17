from ursina import Draggable, Texture, Vec2, camera, scene
import xml.etree.ElementTree as ET
import PIL

class Card(Draggable):
    def __init__(self, value: str, is_face_up: bool, position: Vec2):
        super().__init__(model='quad',
                         texture=f'assets/cards/{value}.png',
                         scale=(0.3, 0.3),
                         collider='box',
                         position=position)
        self.is_face_up = is_face_up # Whether the card is face up or face down
        self.value = value
        self.position = position
        
    def update(self):
        if not self.is_face_up:
            self.texture = f'./assets/card_backs/tile000.png'

    def on_drop(self) -> None:
        print(f'{self.value} dropped at: {self.position.X}, {self.position.Y}')

        # Snap to nearest integer position
        self.position.X = round(self.position.X)
        self.position.Y = round(self.position.Y)

    def flip_card(self) -> None:
        self.is_face_up = not self.is_face_up

    def get_aspect_ratio(self) -> any:
        return self.aspect_ratio