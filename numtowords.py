# ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# tens = [
#     "ten",
#     "twenty",
#     "thirty",
#     "forty",
#     "fifty",
#     "sixty",
#     "seventy",
#     "eighty",
#     "ninty",
# ]

# below_twenty = [
#     "eleven",
#     "twelve",
#     "thirteen",
#     "fourteen",
#     "fifteen",
#     "sixteen",
#     "seventeen",
#     "eighteen",
#     "nineteen",
# ]

# prefix = [
#     "",
#     "thousand",
#     "million",
#     "billion",
#     "trillion",
#     "quadrillion",
#     "quintillion",
# ]

# places = ["", "", "hundred and"]


# def num2words(num: int) -> str:
#     if num == 0:
#         return "Zero"

#     blocks = "{:,}".format(num).split(",")

#     def tran_block(n: int) -> str:
#         n = int(n)
#         place = 1
#         res = []
#         l = n

#         while l > 0:
#             rem = l % 10
#             if rem == 0:
#                 place += 1
#                 l //= 10
#                 continue

#             if place == 2 and 10 < n % 100 < 20:
#                 res = [below_twenty[(n % 10) - 1]]

#             else:
#                 if place == 2:
#                     res.insert(0, tens[rem - 1])
#                 else:
#                     if _ := places[place - 1]:
#                         res.insert(0, _)
#                     res.insert(0, ones[rem - 1])

#             place += 1
#             l //= 10
#         final = " ".join(res)
#         if final.endswith(" and"):
#             final = final[:-4]
#         return final

#     blocks = list(map(tran_block, blocks))
#     final = []
#     for block in blocks:
#         final.append(block + " " + prefix[len(blocks) - blocks.index(block) - 1])
#     return ", ".join(final)

# choice = 1
# while choice!=0:
#     print(num2words(int(input("Enter a number:\n"))))
#     print("\n\n0 .Exit\n1. Continue")
#     choice = int(input("Enter your choice: "))


ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

tens = [
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninty",
]

below_twenty = [
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

prefix = [
    "",
    "thousand",
    "lakh",
    "crore",
    "arab",
    "kharab"
]

places = ["", "", "hundred and"]


def num2words(num: int) -> str:
    if num == 0:
        return "Zero"

    num = str(num)
    blocks = []
    tmp = ''
    c = 1
    for n in num[::-1]:
        tmp = n + tmp
        if c==3:
            blocks.insert(0,tmp)
            tmp=""
        if c%2!=0 and c>3:
            blocks.insert(0, tmp)
            tmp = ""
        c+=1
    if tmp:
        blocks.insert(0,tmp)




    def tran_block(n: int) -> str:
        n = int(n)
        place = 1
        res = []
        l = n

        while l > 0:
            rem = l % 10
            if rem == 0:
                place += 1
                l //= 10
                continue

            if place == 2 and 10 < n % 100 < 20:
                res = [below_twenty[(n % 10) - 1]]

            else:
                if place == 2:
                    res.insert(0, tens[rem - 1])
                else:
                    if _ := places[place - 1]:
                        res.insert(0, _)
                    res.insert(0, ones[rem - 1])

            place += 1
            l //= 10
        final = " ".join(res)
        if final.endswith(" and"):
            final = final[:-4]
        return final
    print(",".join(blocks))
    blocks = list(map(tran_block, blocks))
    final = []
    for block in blocks:
        final.append(block + " " + prefix[len(blocks) - blocks.index(block) - 1])
    return ", ".join(final)

choice = 1
while choice!=0:
    print(num2words(int(input("Enter a number:\n"))))
    print("\n\n0 .Exit\n1. Continue")
    choice = int(input("Enter your choice: "))

