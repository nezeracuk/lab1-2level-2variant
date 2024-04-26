def compute_lps(needle):
    needle_len = len(needle)
    lps = [0] * needle_len
    current_match_length = 0
    i = 1

    while i < needle_len:
        if needle[i] == needle[current_match_length]:
            current_match_length += 1
            lps[i] = current_match_length
            i += 1
        else:
            if current_match_length != 0:
                current_match_length = lps[current_match_length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(haystack, needle):
    if needle == "":
        return "You must find something to search for"
    if haystack > needle:
        return "Haystack can't be longer than needle"

    haystack_len = len(haystack)
    needle_len = len(needle)
    lps = compute_lps(needle)
    i = 0
    j = 0
    result = []

    while i < haystack_len:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == needle_len:
            result.append(i - j)
            j = lps[j - 1]

        elif i < haystack_len and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result if result else "Not found"
