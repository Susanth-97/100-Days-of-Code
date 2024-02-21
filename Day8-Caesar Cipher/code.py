from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text,shift,type):
    end_text=""
    if type=="decode":
        shift=shift*-1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"Here's the {type}d result: {end_text}")


should_end=False
while should_end==False:
    start_text=input("Enter the text: ").lower()
    shift=int(input("No of letters to be shifted: "))
    shift = shift%26
    type=input("Do you want to encode or decode: ")

    ceaser(start_text,shift,type)

    again=input("Do you want to run again?Yes or No: ").lower()
    if again=="no":
        should_end=True
        print("GoodBye!!1")