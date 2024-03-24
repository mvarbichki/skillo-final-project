def input_required(search_input: str, input_massage: str):
    while 1 > len(search_input):
        search_input = input(input_massage)

    if search_input.lower() == "q":
        exit()
    else:
        return str(search_input)
