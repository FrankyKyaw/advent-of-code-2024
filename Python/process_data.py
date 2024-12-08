def process_data(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        left, right = [], []
        for line in lines:
            data = line.strip().split(':')
            left.append(data[0])
            right.append(data[1].split())