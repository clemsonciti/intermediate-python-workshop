def specimen_ratio(img, threshold):
    specimen_area = 0
    N = len(img)
    for row in range(N):
        for col in range(N):
            value = img[row, col]
            if value > threshold:
                specimen_area = specimen_area + 1
    total_area = N*N
    return specimen_area/total_area
