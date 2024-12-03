DIRECTION = ["Up", "Down", "Right", "Left"]
TURN = [90, 270, 0, 180]
class Control:
    def __init__(self) -> None:
        pass

    def direction(slef, obj, input):
        for index in DIRECTION:
            if index == input:
                obj.setheading(TURN[index])  
        
        