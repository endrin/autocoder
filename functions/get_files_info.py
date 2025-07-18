import os

from functions._private import _resolve_path_within_workdir


def get_files_info(working_directory, directory=None):
    try:
        if not directory:
            directory = "."

        abs_tgtdir = _resolve_path_within_workdir(working_directory, directory)

        if not os.path.isdir(abs_tgtdir):
            raise RuntimeError(f'"{directory}" is not a directory')

        return "\n".join(
            f"- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}"
            for entry in os.scandir(abs_tgtdir)
        )
    except Exception as err:
        return f"Error: {err!s}"
