def _get_longest_substring(string_input, length, difference_of):
    '''Function that returns the longest substring of a given string, and a given difference of number
    
    i.e: 
        1112 is a valid substring with a difference of one on the given string 11123.
        1123 is not a valid substring, as 3 has a difference of two with 1.
    '''
    counter = 0    # Control variable used to get the index of the current letter in the for loop

    longest_string = ''

    longest_string_len = len(longest_string)

    for i in range(length):
        for_break_counter = length - counter        

        # Control check if the remaining letters amount is lower than the length of the longest string length, as there's no reason to keep iterating
        if for_break_counter <= longest_string_len:
            break

        aux_string = ''    # Control variable that stores an auxiliar substring to check if it's the longest substring

        first_number = string_input[i]   # Get the first number for the aux_string variable

        aux_string += first_number

        # For that starts one index after the i index
        for j in range((i + 1), length):
            value = string_input[j]

            value_check = abs(int(value) - int(first_number))    # Get the absolute value of the second letter minus the first letter

            # If the value check is equals to the difference, or if the value is zero, add the number to the string.
            if value_check == difference_of or value_check == 0:
                aux_string += value

            else:
                break

        aux_string_len = len(aux_string)

        longest_string_len = len(longest_string)

        # Check if the aux_string length if greater than the current longest_string. If that's the case, set that string as the longest value
        if aux_string_len > longest_string_len:
            longest_string = aux_string

            longest_string_len = len(longest_string)

        # Check if the longest string length + 1 is greater or equals than the length of the string. If that's the case, break the for.
        # What this if does is avoid the for loop to keep looping when the longest possible string has been obtained
        if (longest_string_len + 1) >= length:
            break

        counter += 1

    return longest_string