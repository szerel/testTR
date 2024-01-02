

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count

    except FileNotFoundError:
        print('FileNotFound.')
        return

    except Exception as e:
        print('Error: {}'.format(str(e)))
        return
