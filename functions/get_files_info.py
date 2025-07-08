import os


def get_files_info(working_directory, directory=None):
    target_directory = os.path.join(working_directory, directory)
    abs_workdir = os.path.abspath(working_directory)
    abs_tgtdir = os.path.abspath(target_directory)

    if os.path.commonpath((abs_workdir, abs_tgtdir)) != abs_workdir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_tgtdir):
        return f'Error: "{directory}" is not a directory'

    try:
        return "\n".join(
            f"- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}"
            for entry in os.scandir(abs_tgtdir)
        )
    except Exception as err:
        return f"Error: {err!s}"
