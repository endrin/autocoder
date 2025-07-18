from functions._private import _resolve_path_within_workdir


def write_file(working_directory, file_path, content):
    try:
        abs_tgtfile = _resolve_path_within_workdir(working_directory, file_path)

        with open(abs_tgtfile, "w") as file:
            written = file.write(content)
            return f'Successfully wrote to "{file_path}" ({written} characters written)'

    except Exception as err:
        return f"Error: {err!s}"
