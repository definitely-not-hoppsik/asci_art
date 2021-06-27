from PIL import Image

PATH = 'yin-yang.jpg'
CHARACTERS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
CHARACTERS = CHARACTERS[::-1]


def load_image(path: str) -> tuple:
    im = Image.open(path)
    im = im.resize((127, 180))
    im_width, im_height = im.size
    px = im.load()
    print(type(px))
    return px, im_width, im_height


def create_rgb_matrix(px: Image, im_width: int, im_height: int) -> list:
    rgb_matrix = []
    for i in range(im_width):
        col = []
        for j in range(im_height):
            col.append(px[i, j])
        rgb_matrix.append(col)
    return rgb_matrix


def create_brightness_matrix(rgb_matrix: list, im_width: int, im_height: int, mapping: str) -> list:
    brightness_matrix = []
    for i in range(im_width):
        col = []
        for j in range(im_height):
            if mapping == 'average':
                new_mapping = sum(rgb_matrix[i][j])//3
            elif mapping == 'lightness':
                new_mapping = (
                    max(rgb_matrix[i][j]) + min(rgb_matrix[i][j]))//2
            elif mapping == 'luminosity':
                new_mapping = 0.21*rgb_matrix[i][j][0] + 0.72 * \
                    rgb_matrix[i][j][1] + 0.07*rgb_matrix[i][j][2]
            col.append(new_mapping)
        brightness_matrix.append(col)
    return brightness_matrix


def create_chararters_matrix(brightness_matrix: list,
                             im_width: int, im_height: int, tripple=False) -> list:
    if tripple:
        n = 3
    else:
        n = 1
    characters_matrix = []
    for i in range(im_width):
        col = []
        for j in range(im_height):
            m = brightness_matrix[i][j]
            character = CHARACTERS[int(((m-0)/255)*(64))]
            col.append(character*n)
        characters_matrix.append(col)
    return characters_matrix


def rotated_matrix(matrix: list) -> list:
    rotated_matrix = list(zip(*matrix[::-1]))
    return rotated_matrix


def render(matrix: list) -> None:
    for row in matrix:
        print(row)


def main() -> None:
    px, im_width, im_height = load_image(PATH)
    rgb_matrix = create_rgb_matrix(px, im_width, im_height)
    brightness_matrix = create_brightness_matrix(
        rgb_matrix, im_width, im_height, mapping='luminosity')
    characters_matrix = create_chararters_matrix(
        brightness_matrix, im_width, im_height, tripple=False)

    matrix = rotated_matrix(characters_matrix)
    render(matrix)


if __name__ == "__main__":
    main()
