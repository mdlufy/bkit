from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import emoji



def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)


    print(r, "\N{grinning face}", "\N{slightly smiling face}", "\N{winking face}")
    print(c, emoji.emojize('Python is :cookie:'))
    print(s, emoji.emojize(':new_moon_with_face:', use_aliases=True))

    print(emoji.emojize('MGTU is :thumbsup:', use_aliases=True))


if __name__ == "__main__":
    main()
