def solve() -> int:
    limit = 2 * 1000 * 1000
    min_distance = limit
    area = 0
    for width in range(2000):
        for height in range(width):
            count = width * (width + 1) * height * (height + 1) // 4
            distance = abs(count - limit)
            if distance < min_distance:
                min_distance = distance
                area = width * height
            elif count > limit:
                break
    return area
