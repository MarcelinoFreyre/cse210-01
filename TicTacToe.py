def main():
    line1 = [1, 2, 3] 
    line2 = [4, 5, 6]
    line3 = [7, 8, 9]
    middle_symbols = "- + - + -"
    print("Welcome to Tic Tac Toe Game!")
    print()
    print(line1)
    print(middle_symbols)
    print(line2)
    print(middle_symbols)
    print(line3)
    print()
    print("First Player will be 'Xs' and Second Player 'Os'")
    counter = 1
    while counter < 10:
        if counter == 1 or counter == 3 or counter == 5 or counter == 7 or counter == 9:
            content = "X"
            response = int(input("Please, select an empty cell: "))
            game(content, response, line1, line2, line3, middle_symbols)
        else:
            content = "O"
            response = int(input("Please, select an empty cell: "))
            game(content, response, line1, line2, line3, middle_symbols)
        counter += 1
        
    print("Game Over")
        
def game(content, response, line1, line2, line3, middle_symbols):
    if response == 1:
        line1[0] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 2:
        line1[1] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 3:
        line1[2] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 4:
        line2[0] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 5:
        line2[1] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 6:
        line2[2] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 7:
        line3[0] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 8:
        line3[1] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    elif response == 9:
        line3[2] = content
        print(f"{line1[0]} | {line1[1]} | {line1[2]}")
        print(middle_symbols)
        print(f"{line2[0]} | {line2[1]} | {line2[2]}")
        print(middle_symbols)
        print(f"{line3[0]} | {line3[1]} | {line3[2]}")
    
main()
# def printing(line1, line2, line3, middle_symbols):
#     print(line1)
#     print(middle_symbols)
#     print(line2)
#     print(middle_symbols)
#     print(line3)