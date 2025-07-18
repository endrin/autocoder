## `get_files_info` test

# from functions.get_files_info import get_files_info
#
#
# def print_results_for(dir, base="calculator"):
#     res = get_files_info(base, dir)
#     dirname = "current" if dir == "." else f"'{dir}'"
#     print(
#         f"Result for {dirname} directory:",
#         res,
#         sep="\n",
#         end="\n\n",
#     )
#
#
# print_results_for(".")
# print_results_for("pkg")
# print_results_for("/bin")
# print_results_for("../")
# print_results_for("main.py")


## `get_file_content` test

# from functions.get_file_content import get_file_content
#
#
# def print_results_for(filename, base="calculator"):
#     res = get_file_content(base, filename)
#
#     print(
#         f"Result for `{filename}` file in `{base}` directory:",
#         res,
#         sep="\n",
#         end="\n\n",
#     )
#
#
# print_results_for("lorem.txt")
# print_results_for("main.py")
# print_results_for("pkg/calculator.py")
# print_results_for("/bin/cat")
# print_results_for("pkg/does_not_exist.py")


## `write_file` test

from functions.write_file import write_file


def print_results_for(filename, content, base="calculator"):
    res = write_file(base, filename, content)

    print(
        f"Result for `{filename}` file in `{base}` directory:",
        res,
        sep="\n",
        end="\n\n",
    )


print_results_for("lorem.txt", "wait, this isn't lorem ipsum")
print_results_for("pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print_results_for("/tmp/temp.txt", "this should not be allowed")
