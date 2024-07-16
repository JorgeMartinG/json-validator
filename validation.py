from pathlib import Path
import json
import sys

def validate(dir_name: str) -> None:
    '''
    Validate the JSON content of the specified file.\n
    Args:\n
    \t- filename (str): The path to the JSON file to be validated.
    '''
    dir_path = Path(dir_name)
    if not Path(dir_path).is_dir():
        print(f'Directory not found: {dir_name}')
        # (2) No such file or directory.
        sys.exit(2)

    json_files = list(dir_path.glob('*.json'))

    if not json_files:
        print(f'No JSON files found.')
        # (2) No such file or directory.
        sys.exit(2)

    for file in json_files:
        try:
            with file.open('r', encoding='utf-8') as f:
                json.load(f)
            print(f'{file}: JSON is valid')
            validate = True
            
        except json.JSONDecodeError as decode_error:
            print(f'{file}: JSON is invalid - {decode_error}')
            validate = False

        except Exception as e:
            print(f'An error ocurred - {e}')
            # (1) Standard runtime error.
            sys.exit(1)

    if validate:
        print('All JSON files are valid.')
        sys.exit(0) # (0) All JSON file syntax are valid.
    else:
        print('There are invalid JSON files.')
        sys.exit(1) # (1) JSON file syntax is invalid.
    
if __name__ == '__main__':
    validate('json')
    