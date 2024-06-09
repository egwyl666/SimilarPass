# Password Transformation Tool or SimilarPass

```bash
Remember. When you create a password and then add 123 to it after a while, it is not a new password, but exactly the same as the old one
``` 
## Overview
This tool provides various password transformations based on the configurations specified in `config.json`. It can modify passwords by applying transformations such as reversing, changing case, extracting numbers, and more. The tool is designed to extend easily by adding new types of transformations.

## Configuration
Transformations are defined in `config.json`. Here you can specify which transformations to enable and define lists of prefixes and suffixes that can be added to passwords.

### Config File Format
The configuration file is a JSON document with the following keys:
capitalize_first: Capitalizes the first character of the password, leaving the rest as is.
- `all_caps:` Converts the entire password to uppercase, enhancing readability and standardizing format.
- `reverse`: Reverses the order of characters in the password, creating a simple yet effective variation.
- `reverse_upper:` Reverses the order of characters and converts them all to uppercase, combining two transformations for stronger variance.
- `reverse_letters_numbers:` Reverses all alphabetical characters and appends numerical characters at the end, separating letters from digits.
- `reverse_upper_letters:` Similar to reverse_letters_numbers, but the reversed alphabetical characters are also converted to uppercase.
- `upper_no_numbers:` Removes all numerical digits and converts the remaining letters to uppercase.
- `numbers_only:` Extracts and retains only the numerical digits from the password, ignoring alphabetical characters.
- `numbers_reverse_letters:` Keeps the numerical digits at the beginning and appends the reversed alphabetical characters.
- `numbers_reverse_upper_letters:` Starts with the numerical digits and appends the reversed alphabetical characters converted to uppercase.
- `chess_case:` Alternates the case of the characters starting with uppercase, similar to the pattern on a chessboard.
- `reverse_chess_case:` Similar to chess_case, but starts with lowercase, altering the standard pattern.
- `symmetric_mirror:` Generates a password where the first half is mirrored in the second half with modifications such as case changes.
- `mirror_second_half:` Takes the second half of the password, mirrors it, and then appends this mirrored version to the original second half.
- `mirror_first_half_original:` Mirrors the first half of the password and appends this mirrored version to the original first half.
- `mirror_second_half_original:` Works like `mirror_first_half_original`, but with the second half: it mirrors it and then appends the mirrored version back to the original second half.

## Prefixes and Suffixes Configuration

- `prefixes:` A list of strings specified in the configuration that can be prepended to the password. Example prefixes in the configuration include numeric sequences and symbols which can be used to enhance password complexity.
- `suffixes:` A list similar to prefixes but these strings are appended to the password. They can be used to meet specific password policy requirements or add an additional layer of complexity.
- `enable_prefix_suffix:` A boolean setting that, when set to true, enables the application of prefixes and suffixes as defined in the configuration.

## Python Script
The Python script `SimilarPass.py` reads the configuration and applies the enabled transformations to the input password. It includes functions to handle different transformation logic as specified in the configuration.

### How to Use
1. Ensure Python 3 is installed on your system.
2. Place the `config.json` in the same directory as the script.
3. Run the script using the command:
```python
SimilarPass.py
```
4. Input passwords as prompted or modify the script to handle batch processing.

### Example Usage
Here's a sample usage in the script:
```python
input_password = "password123"
password_variants = generate_password_variants(input_password)
for variant in password_variants:
 print(variant)
```

This will output the transformed passwords based on the enabled configurations.

### Customization
You can customize the behavior by modifying config.json according to the needed transformations. New transformations can be added by extending the transform_password function.

### Support
For support, ensure all dependencies are correctly installed and the JSON configuration is correctly formatted. Check Python's documentation for details on handling JSON and file I/O.

```vbnet
This `README.md` gives an overview of your project, explains the configuration and usage, and provides a basic guide on how to run and customize the script. Adjust the documentation as necessary to fit more specific features or configurations you might add later.
```
