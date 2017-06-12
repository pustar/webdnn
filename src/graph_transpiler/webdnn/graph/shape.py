import ast
from typing import Dict, Tuple, Union, List

from webdnn.graph.place_holder import PlaceHolder


class Shape:
    @staticmethod
    def parse(text: str) -> Tuple[List[Union[int, PlaceHolder]], Dict[str, PlaceHolder]]:

        try:
            tmp = ast.literal_eval(text.replace('_', 'None'))

        except ValueError:
            raise ValueError(f"Invalid shape format: '{text}'")

        shape = []
        placeholders = {}
        for i, t in enumerate(tmp):
            if t is None:
                t = PlaceHolder()
                placeholders["p" + str(i)] = t

            shape.append(t)

        return shape, placeholders
