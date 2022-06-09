from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Returns for set country her code Pygal, consisting of 2 letters"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If country is not found, return None
    return None




