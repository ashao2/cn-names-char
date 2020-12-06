import heapq
import sys

assert len(sys.argv) == 3

try:
    input_list = str(sys.argv[1])
    assert input_list[-4:] == ".txt"
except:
    raise Exception("Invalid file name string")
    sys.exit()

try:
    num_print = int(sys.argv[2])
    assert num_print > 0
except:
    raise TypeError("Not a valid integer input")
    sys.exit()

surnames = dict()
full_names = dict()  # full names
full_two = dict()  # full two-char given names
first_char = dict()  # 1st char of two-char given names
second_char = dict()  # 2nd char of two-char given names
one_char = dict()  # one-char names
all_given = dict()  # all chars in given names

def check_dict(zidian, char_name):
    if char_name not in zidian:
        zidian[char_name] = 1
    else:
        zidian[char_name] += 1

with open(input_list, 'r') as names_list:
    for line in names_list:
        cleaned = line.strip()
        if len(cleaned) < 2 or len(cleaned) > 3:
            continue
        # Full names:
        check_dict(full_names, cleaned)
        # Surnames:
        xing = cleaned[0]
        check_dict(surnames, xing)
        # Given names:
        if len(cleaned) == 2:
            ming = cleaned[1]
            check_dict(one_char, ming)
            check_dict(all_given, ming)
        elif len(cleaned) == 3:
            ming1 = cleaned[1]
            check_dict(first_char, ming1)
            check_dict(all_given, ming1)

            ming2 = cleaned[2]
            check_dict(second_char, ming2)
            check_dict(all_given, ming2)

            both = cleaned[1:]
            check_dict(full_two, both)
# Surnames heap:
sur_list = []
for name, count in surnames.items():
    sur_list.append((-1 * count, name))
heapq.heapify(sur_list)
# All given names heap:
all_first_list = []
for name, count in all_given.items():
    all_first_list.append((-1 * count, name))
heapq.heapify(all_first_list)
# 1-char given names heap:
single_name = []
for name, count in one_char.items():
    single_name.append((-1 * count, name))
heapq.heapify(single_name)
# 2-char given names heap:
full_shuang = []
for name, count in full_two.items():
    full_shuang.append((-1 * count, name))
heapq.heapify(full_shuang)
# 1st char of 2-char given names heap:
shuang_one = []
for name, count in first_char.items():
    shuang_one.append((-1 * count, name))
heapq.heapify(shuang_one)
# 2nd char of 2-char given names heap:
shuang_two = []
for name, count in second_char.items():
    shuang_two.append((-1 * count, name))
heapq.heapify(shuang_two)
# Full names heap:
xingming = []
for name, count in full_names.items():
    xingming.append((-1 * count, name))
heapq.heapify(xingming)

def write_names(writer, name_list, print_len):
    first_bool = True
    for num in range(0, print_len):
        tuple = heapq.heappop(name_list)
        #print(tuple)
        if tuple[0] == -1 and first_bool:
            writer.write("No names/characters occured more than once\n")
            break
        elif tuple[0] == -1 and not first_bool:
            writer.write("Stopped before reaching one\n")
            break
        else:
            to_write = str(tuple[1]) + ": " + str(-1 * tuple[0]) + "\n"
            writer.write(to_write)
            first_bool = False
        if not name_list:
            break

with open('results.txt', 'w') as name_counts:
    name_counts.write("Top Surnames:\n")
    write_names(name_counts, sur_list, num_print)

    name_counts.write("\nTop Characters in Given Names:\n")
    write_names(name_counts, all_first_list, num_print)

    name_counts.write("\nTop Two-Character Names:\n")
    write_names(name_counts, full_shuang, num_print)

    name_counts.write("\nTop 1st Characters in Two-Character Names:\n")
    write_names(name_counts, shuang_one, num_print)

    name_counts.write("\nTop 2nd Characters in Two-Character Names:\n")
    write_names(name_counts, shuang_two, num_print)

    name_counts.write("\nTop One-Character Names:\n")
    write_names(name_counts, single_name, num_print)

    name_counts.write("\nTop Full Names:\n")
    write_names(name_counts, xingming, num_print)

# Read in names from file
# Separate into surnames & given names
# Separate given names in 1-char & 2-char
# Count up most common for each group (surname, 1-char, 2-char), perhaps using dictionarries
# Create PQ for printing n most common names
