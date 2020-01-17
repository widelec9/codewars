def is_interesting(number, awesome_phrases, counter=0):
    numstr = str(number)
    followed_by_zeros, dig_inc_dec, is_palindrome, is_awesome = (int(numstr[1:]) == 0, numstr in '1234567890 9876543210', numstr == numstr[::-1], number in awesome_phrases) if number > 99 \
                                                                    else (False, False, False, False)
    counter += 1
    return 2 if followed_by_zeros or dig_inc_dec or is_palindrome or is_awesome \
        else 1 if counter < 3 and (is_interesting(number + 1, awesome_phrases, counter) == 2 or is_interesting(number + 2, awesome_phrases, counter) == 2) \
        else 0
