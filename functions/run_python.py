import os
import subprocess
from functions._private import _resolve_path_within_workdir


def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_tgtfile = _resolve_path_within_workdir(
            working_directory, file_path, resolution="Cannot execute"
        )

        if not os.path.exists(abs_tgtfile):
            raise RuntimeError(f'File "{file_path}" not found.')

        _, ext = os.path.splitext(abs_tgtfile)
        if ext != ".py":
            raise RuntimeError(f'"{file_path}" is not a Python file.')

        try:
            completed_process = subprocess.run(
                ["python", abs_tgtfile, *args],
                capture_output=True,
                cwd=os.path.dirname(abs_tgtfile),
                timeout=30,
            )
            res = []

            if completed_process.stdout:
                res += [
                    "\n".join(("STDOUT:", completed_process.stdout.decode("utf-8")))
                ]

            if completed_process.stderr:
                res += [
                    "\n".join(("STDERR:", completed_process.stderr.decode("utf-8")))
                ]

            if not res:
                res += ["No output produced"]

            if completed_process.returncode > 0:
                res += [f"Process exited with code {completed_process.returncode}"]

            return "\n\n".join(res)

        except Exception as err:
            raise RuntimeError(f"executing Python file: {err!s}")

    except Exception as err:
        return f"Error: {err!s}"
