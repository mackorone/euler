from path import (
    get_triangle,
    max_path_value,
)


def ans():
    triangle = get_triangle('067.txt')
    return max_path_value(triangle)
    

if __name__ == '__main__':
    print(ans())
