import os
from functions._private import _resolve_path_within_workdir
from functions.config import MAX_READ


def get_file_content(working_directory, file_path):
    try:
        abs_tgtfile = _resolve_path_within_workdir(working_directory, file_path)

        if not os.path.isfile(abs_tgtfile):
            raise RuntimeError(
                f'File not found or is not a regular file: "{file_path}"'
            )

        with open(abs_tgtfile, "r") as file:
            data = file.read(MAX_READ)
            if len(data) == MAX_READ and file.read(1) != "":
                data += f'[...File "{file_path}" truncated at {MAX_READ} characters]'

        return data

    except Exception as err:
        return f"Error: {err!s}"
