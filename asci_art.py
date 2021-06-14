from PIL import Image

path = 'yin-yang.jpg'
characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
characters = characters[::-1]


def load_image(path):
    im = Image.open(path)
    im = im.resize((127, 180))
    im_width, im_height = im.size
    px = im.load()
    return px, im_width, im_height


def create_rgb_matrix(px, im_width, im_height):
    rgb_matrix = []
    for i in range(im_width):
        col = []
        for j in range(im_height):
            col.append(px[i, j])
        rgb_matrix.append(col)
    return rgb_matrix


def create_brightness_matrix(rgb_matrix, im_width, im_height, mapping):
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


def create_chararters_matrix(brightness_matrix, im_width, im_height, tripple=False):
    if tripple:
        n = 3
    else:
        n = 1
    characters_matrix = []
    for i in range(im_width):
        col = []
        for j in range(im_height):
            m = brightness_matrix[i][j]
            character = characters[int(((m-0)/255)*(64))]
            col.append(character*n)
        characters_matrix.append(col)
    return characters_matrix


def rotated_matrix(matrix):
    rotated_matrix = list(zip(*matrix[::-1]))
    return rotated_matrix


def render(matrix):
    for row in matrix:
        print(row)


def main():
    px, im_width, im_height = load_image(path)
    rgb_matrix = create_rgb_matrix(px, im_width, im_height)
    brightness_matrix = create_brightness_matrix(
        rgb_matrix, im_width, im_height, mapping='luminosity')
    characters_matrix = create_chararters_matrix(
        brightness_matrix, im_width, im_height, tripple=False)

    matrix = rotated_matrix(characters_matrix)
    render(matrix)


if __name__ == "__main__":
    main()
