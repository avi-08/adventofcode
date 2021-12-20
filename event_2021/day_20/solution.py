import os


DX = (-1, -1, -1, 0, 0, 0, 1, 1, 1)
DY = (-1, 0, 1, -1, 0, 1, -1, 0, 1)


def read_input(file_name='input.txt'):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    ie_algo = lines[0]
    return lines[2:], ie_algo


def add_padding(image: list, ch, size=2):
    padding_top_down = ch * (len(image[0]) + size * 2)
    padding_left_right = ch * size
    padded = [padding_top_down for _ in range(size)]
    for line in image:
        padded.append(f'{padding_left_right}{line}{padding_left_right}')
    for _ in range(size):
        padded.append(padding_top_down)
    return padded


def get_index(image, r, c):
    binary_str = ''
    for index in range(len(DX)):
        x = r + DX[index]
        y = c + DY[index]
        binary_str += '0' if image[x][y] == '.' else '1'
    return int(binary_str, 2)


def count_lit_pixels(image):
    lit_count = 0
    for row in image:
        for col in row:
            if col == '#':
                lit_count += 1
    return lit_count


def enhance_image(image, ie_algo):
    enhanced_image = []
    for row in range(1, len(image) - 1):
        pixel_row = ''
        for col in range(1, len(image[row]) - 1):
            index = get_index(image, row, col)
            pixel_row += ie_algo[index]
        enhanced_image.append(pixel_row)
    # print(f"Dimensions of enhanced image: {len(enhanced_image)} X {len(enhanced_image[0])}")
    return enhanced_image


def main():
    image, ie_algo = read_input('input.txt')
    print(f"Image dimensions: {len(image)} X {len(image[0])}")
    assert len(ie_algo) == 512
    
    # Part one
    image_new = image
    for i in range(2):
        border = '.' if i % 2 == 0 else '#'
        image_new = add_padding(image_new, border)
        image_new = enhance_image(image_new, ie_algo)
    lit_count = count_lit_pixels(image_new)
    print("After 2 iterations")
    print(f"Dimensions of enhanced image: {len(image_new)} X {len(image_new[0])}")
    print(f"Lit pixels: {lit_count}")
    
    # Part two: 2/50 iterations already done in part 1
    for i in range(48):
        border = '.' if i % 2 == 0 else '#'
        image_new = add_padding(image_new, border)
        image_new = enhance_image(image_new, ie_algo)
    lit_count = count_lit_pixels(image_new)
    print("After 50 iterations")
    print(f"Dimensions of enhanced image: {len(image_new)} X {len(image_new[0])}")
    print(f"Lit pixels: {lit_count}")

    # Dump image to file
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image.txt')
    with open(file_path, 'w') as f:
        for row in image_new:
            f.write(row)
            f.write('\n')

if __name__ == '__main__':
    main()
