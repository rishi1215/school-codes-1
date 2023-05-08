def main():
    with open("poem.txt", "r") as f:
        lines = f.readlines()
    _ = [0 for a in lines if a[0].isupper()]
    count = len(_)
    print("No. of lines starting with upper case character:", count)

main()