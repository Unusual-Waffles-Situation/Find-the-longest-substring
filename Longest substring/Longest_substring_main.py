import Longest_substring_function as lsf

if __name__ == "__main__":
    while(True):
        int_input = input("Input a string of letters without spaces: ")

        string_input_check = int_input.isdigit()

        if string_input_check:
            break

    while(True):
        difference_input = int(input("Input the difference value (n > 0 && n < 10): "))

        if difference_input > 0 and difference_input < 10:
            break

    int_input_len = len(int_input)

    print("The longest substring of the string '" + int_input + "' is: " + lsf._get_longest_substring(int_input, int_input_len, difference_input))