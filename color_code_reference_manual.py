from color_codes import MAJOR_COLORS, MINOR_COLORS, color_pair_to_string
from pair_number_from_color import get_pair_number_from_color

def create_reference_manual():
    manual = []
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major, minor)
            manual.append(f'{pair_number:2d} - {color_pair_to_string(major, minor)}')
    return '\n'.join(manual)
