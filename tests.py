from functions.get_files_info import get_files_info


def print_results_for(dir, base="calculator"):
    res = get_files_info(base, dir)
    dirname = "current" if dir == "." else f"'{dir}'"
    print(
        f"Result for {dirname} directory:",
        res,
        sep="\n",
        end="\n\n",
    )


print_results_for(".")
print_results_for("pkg")
print_results_for("/bin")
print_results_for("../")
print_results_for("main.py")
