def count_substring(string, sub_string):
    substring_len = len(sub_string)
    string_len = len(string)
    return sum([1 for i in range(string_len - substring_len + 1) if string[i:i+substring_len] == sub_string])
    """
    for i in range(string_len - substring_len + 1):
        if string[i:i+substring_len] == sub_string:
            cnt += 1
    return cnt
        #string.find(sub_string, i, i + substring_len)
        """

