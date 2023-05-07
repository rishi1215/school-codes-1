def is_to_up_count():
    to_count = ["is", "to", "up"]
    with open("writer.txt") as file:
        count = len([file.read().lower().split().count(a) for a in to_count])
        print("Total number of occurence of is,to,up =", count)


is_to_up_count()
