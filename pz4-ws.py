words = []
with open("en_US-large.txt") as fd:
    for line in fd:
        words.append(line.strip().lower())

def check_word(word):
    if word in words:
        return word

word_to_check = 'meddler'
checked = check_word(word_to_check)
if checked:
    print(checked)
word_to_check = 'trees'
checked = check_word(word_to_check)
if checked:
    print(checked)
word_to_check = 'traitors'
checked = check_word(word_to_check)
if checked:
    print(checked)
word_to_check = 'lkjg'
checked = check_word(word_to_check)
if checked:
    print(checked)

word_search = []
with open("pz4-ws.txt") as fd:
    for line in fd:
        word_search.append(list(line.strip()))
print(word_search)

def check_a_or_j(word_search, line_index, letter_index):
    pigpen_letters = "a or j"
    if letter_index-2 < 0:
        return
    if line_index+2 > len(word_search) - 1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index+1][letter_index]
    word_to_check += word_search[line_index+2][letter_index]
    word_to_check += word_search[line_index+2][letter_index-1]
    word_to_check += word_search[line_index+2][letter_index-2]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_b_or_k(word_search, line_index, letter_index):
    pigpen_letters = "b or k"
    if letter_index+2 > len(word_search[line_index]) - 1:
        return
    if line_index+2 > len(word_search) - 1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index+1][letter_index]
    word_to_check += word_search[line_index+2][letter_index]
    word_to_check += word_search[line_index+2][letter_index+1]
    word_to_check += word_search[line_index+2][letter_index+2]
    word_to_check += word_search[line_index+2][letter_index+1]
    word_to_check += word_search[line_index+2][letter_index]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_c_or_l(word_search, line_index, letter_index):
    pigpen_letters = "c or l"
    if letter_index+2 > len(word_search[line_index]) - 1:
        return
    if line_index+2 > len(word_search) - 1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index+1][letter_index]
    word_to_check += word_search[line_index+2][letter_index]
    word_to_check += word_search[line_index+2][letter_index+1]
    word_to_check += word_search[line_index+2][letter_index+2]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_d_or_m(word_search, line_index, letter_index):
    pigpen_letters = "d or m"
    if letter_index+2 > len(word_search[line_index]) - 1:
        return
    if line_index+2 > len(word_search) - 1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index][letter_index+1]
    word_to_check += word_search[line_index][letter_index+2]
    word_to_check += word_search[line_index+1][letter_index+2]
    word_to_check += word_search[line_index+2][letter_index+2]
    word_to_check += word_search[line_index+2][letter_index+1]
    word_to_check += word_search[line_index+2][letter_index]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_e_or_n(word_search, line_index, letter_index):
    pigpen_letters = "e or n"
    if letter_index+2 > len(word_search[line_index]) - 1:
        return
    if line_index+2 > len(word_search) - 1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index][letter_index+1]
    word_to_check += word_search[line_index][letter_index+2]
    word_to_check += word_search[line_index+1][letter_index+2]
    word_to_check += word_search[line_index+2][letter_index+2]
    word_to_check += word_search[line_index+2][letter_index+1]
    word_to_check += word_search[line_index+2][letter_index]
    word_to_check += word_search[line_index+1][letter_index]
    for i in range(0, len(word_to_check)-1):
        permutation_to_check = word_to_check[i:] + word_to_check[:i]
        checked = check_word(permutation_to_check)
        if checked:
            print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
        permutation_to_check = word_to_check[i::-1] + word_to_check[:i:-1]
        checked = check_word(permutation_to_check)
        if checked:
            print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_f_or_o(word_search, line_index, letter_index):
    pigpen_letters = "f or o"
    if letter_index-2 < 0:
        return
    if line_index+2 > len(word_search)-1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index][letter_index-1]
    word_to_check += word_search[line_index][letter_index-2]
    word_to_check += word_search[line_index+1][letter_index-2]
    word_to_check += word_search[line_index+2][letter_index-2]
    word_to_check += word_search[line_index+2][letter_index-1]
    word_to_check += word_search[line_index+2][letter_index]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_g_or_p(word_search, line_index, letter_index):
    pigpen_letters = "g or p"
    if letter_index+2 > len(word_search[line_index])-1:
        return
    if line_index+2 > len(word_search)-1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index][letter_index+1]
    word_to_check += word_search[line_index][letter_index+2]
    word_to_check += word_search[line_index+1][letter_index+2]
    word_to_check += word_search[line_index+2][letter_index+2]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_h_or_q(word_search, line_index, letter_index):
    pigpen_letters = "h or q"
    if letter_index+2 > len(word_search[line_index])-1:
        return
    if line_index-2 < 0:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index-1][letter_index]
    word_to_check += word_search[line_index-2][letter_index]
    word_to_check += word_search[line_index-2][letter_index+1]
    word_to_check += word_search[line_index-2][letter_index+2]
    word_to_check += word_search[line_index-1][letter_index+2]
    word_to_check += word_search[line_index][letter_index+2]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_i_or_r(word_search, line_index, letter_index):
    pigpen_letters = "i or r"
    if letter_index-2 < 0:
        return
    if line_index+2 > len(word_search)-1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index][letter_index-1]
    word_to_check += word_search[line_index][letter_index-2]
    word_to_check += word_search[line_index+1][letter_index-2]
    word_to_check += word_search[line_index+2][letter_index-2]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_s_or_w(word_search, line_index, letter_index):
    pigpen_letters = "s or w"
    if letter_index+4 > len(word_search[line_index])-1:
        return
    if line_index+2 > len(word_search)-1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index+1][letter_index+1]
    word_to_check += word_search[line_index+2][letter_index+2]
    word_to_check += word_search[line_index+1][letter_index+3]
    word_to_check += word_search[line_index][letter_index+4]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_t_or_x(word_search, line_index, letter_index):
    pigpen_letters = "t or x"
    if letter_index+2 > len(word_search[line_index])-1:
        return
    if line_index+4 > len(word_search)-1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index+1][letter_index+1]
    word_to_check += word_search[line_index+2][letter_index+2]
    word_to_check += word_search[line_index+3][letter_index+1]
    word_to_check += word_search[line_index+4][letter_index]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_u_or_y(word_search, line_index, letter_index):
    pigpen_letters = "u or y"
    if letter_index-2 < 0:
        return
    if line_index+4 > len(word_search)-1:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index+1][letter_index-1]
    word_to_check += word_search[line_index+2][letter_index-2]
    word_to_check += word_search[line_index+3][letter_index-1]
    word_to_check += word_search[line_index+4][letter_index]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

def check_v_or_z(word_search, line_index, letter_index):
    pigpen_letters = "v or z"
    if letter_index+4 > len(word_search[line_index])-1:
        return
    if line_index-2 < 0:
        return
    word_to_check = ""
    word_to_check += word_search[line_index][letter_index]
    word_to_check += word_search[line_index-1][letter_index+1]
    word_to_check += word_search[line_index-2][letter_index+2]
    word_to_check += word_search[line_index-1][letter_index+3]
    word_to_check += word_search[line_index][letter_index+4]
    checked = check_word(word_to_check)
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")
    checked = check_word(word_to_check[::-1])
    if checked:
        print(f"{checked} - {pigpen_letters} - {line_index},{letter_index}")

for line_index, line in enumerate(word_search):
    for letter_index, letter in enumerate(line):
        check_a_or_j(word_search, line_index, letter_index)
        check_b_or_k(word_search, line_index, letter_index)
        check_c_or_l(word_search, line_index, letter_index)
        check_d_or_m(word_search, line_index, letter_index)
        check_e_or_n(word_search, line_index, letter_index)
        check_f_or_o(word_search, line_index, letter_index)
        check_g_or_p(word_search, line_index, letter_index)
        check_h_or_q(word_search, line_index, letter_index)
        check_i_or_r(word_search, line_index, letter_index)
        check_s_or_w(word_search, line_index, letter_index)
        check_t_or_x(word_search, line_index, letter_index)
        check_u_or_y(word_search, line_index, letter_index)
        check_v_or_z(word_search, line_index, letter_index)

