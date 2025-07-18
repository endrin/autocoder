import os


def _resolve_path_within_workdir(working_directory, path, resolution=""):
    target_directory = os.path.join(working_directory, path)
    abs_workdir = os.path.abspath(working_directory)
    abs_tgtdir = os.path.abspath(target_directory)

    if os.path.commonpath((abs_workdir, abs_tgtdir)) != abs_workdir:
        err = (
            f'"{path}" is outside the permitted working directory'
            if not resolution
            else f'{resolution} "{path}" as it is outside the permitted working directory'
        )
        raise RuntimeError(err)

    return abs_tgtdir
