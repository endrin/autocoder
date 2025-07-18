import functions

from google.genai import types

from functions.config import CWD
import functions.get_file_content
import functions.get_files_info
import functions.run_python
import functions.write_file


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of a file, truncated to 10000 characters if too long, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to get content from, relative to the working directory. Must point to an existing regular file.",
            ),
        },
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided contents to a file, creating it if not exists and overwriting if it does exist. Returns number of characters written.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write content to, relative to the working directory. Will be created if does not exist.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to a file.",
            ),
        },
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with provided optional arguments. The file will be executed inside of the working directory and execution results will be returned.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python script file. The file is relative to the working directory and must exist and be a valid Python script file.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to the script. If not provided, the script will be run without arguments.",
            ),
        },
    ),
)

available_functions = {
    "get_files_info": functions.get_files_info.get_files_info,
    "get_file_content": functions.get_file_content.get_file_content,
    "run_python_file": functions.run_python.run_python_file,
    "write_file": functions.write_file.write_file,
}


def call_function(
    function_call_part: types.FunctionCall, verbose=False
) -> types.Content:
    function_name = function_call_part.name
    function_args = function_call_part.args

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    func = available_functions.get(function_name, None)
    if not func:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    function_result = func(CWD, **function_args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
