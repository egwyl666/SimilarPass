import json

def read_config():
    try:
        with open("config.json", "r") as file:
            # Load and return the config settings
            return json.load(file)
    except FileNotFoundError:
        print("config.json not found. Initialize the settings.")
        return {}
    except json.JSONDecodeError:
        print("JSON decode error. Check config formatting.")
        return {}
    
def transform_password(input_password, transformation_type, config):
    if transformation_type == "upper_no_numbers":
        return ''.join(filter(str.isalpha, input_password)).upper()
    
    elif transformation_type == "capitalize_first": 
        return input_password.capitalize()
    
    elif transformation_type == "all_caps":  
        return input_password.upper()
    
    elif transformation_type == "reverse":  
        return input_password[::-1]
    
    elif transformation_type == "reverse_upper": 
        return input_password[::-1].upper()
    
    elif transformation_type == "reverse_letters_numbers":  
        letters = ''.join(filter(str.isalpha, input_password))[::-1]
        numbers = ''.join(filter(str.isdigit, input_password))
        return letters + numbers
    
    elif transformation_type == "reverse_upper_letters":
        letters = ''.join(filter(str.isalpha, input_password))[::-1].upper()
        numbers = ''.join(filter(str.isdigit, input_password))
        return letters + numbers  

    elif transformation_type == "numbers_only": 
        return ''.join(filter(str.isdigit, input_password))

    elif transformation_type == "numbers_reverse_letters": 
        numbers = ''.join(filter(str.isdigit, input_password))
        letters = ''.join(filter(str.isalpha, input_password))[::-1]
        return numbers + letters

    elif transformation_type == "numbers_reverse_upper_letters": 
        numbers = ''.join(filter(str.isdigit, input_password))
        letters = ''.join(filter(str.isalpha, input_password))[::-1].upper()
        return numbers + letters
    
    elif transformation_type == "chess_case" and config.get("chess_case", False):
        transformed = []
        for i, char in enumerate(input_password):
            if i % 2 == 0:
                transformed.append(char.upper())
            else:
                transformed.append(char.lower())
        return ''.join(transformed)
    
    elif transformation_type == "reverse_chess_case" and config.get("reverse_chess_case", False):
        transformed = []
        for i, char in enumerate(input_password):
            if i % 2 == 0:
                transformed.append(char.lower())
            else:
                transformed.append(char.upper())
        return ''.join(transformed)

    elif transformation_type == "symmetric_mirror":
        mid_point = len(input_password) // 2
        first_half = input_password[:mid_point]
        mirrored = first_half[::-1]

        modified_mirror = ''.join(char.upper() if char.islower() else char.lower() for char in mirrored)

        result = first_half + (input_password[mid_point] if len(input_password) % 2 != 0 else '') + modified_mirror
        return result
    
    elif transformation_type == "mirror_second_half":
        mid_point = len(input_password) // 2
        second_half = input_password[mid_point:] if len(input_password) % 2 == 0 else input_password[mid_point + 1:]
        mirrored_second = second_half[::-1]

        modified_mirror = ''.join(char.upper() if char.islower() else char.lower() for char in mirrored_second)

        result = second_half + modified_mirror
        return result

    elif transformation_type == "mirror_first_half_original":
        mid_point = len(input_password) // 2
        first_half = input_password[:mid_point]

        mirrored_first = first_half[::-1]
        result = first_half + mirrored_first
        return result

    elif transformation_type == "mirror_second_half_original":
        mid_point = len(input_password) // 2
        second_half = input_password[mid_point:]

        mirrored_second = second_half[::-1]
        result = second_half + mirrored_second
        return result

    
    elif transformation_type == "modify_prefix_suffix":
        if config.get("enable_prefix_suffix", False):
            password_variants = []
            prefixes = config.get("prefixes", [])
            suffixes = config.get("suffixes", [])
            
            for prefix in prefixes:
                password_variants.append(prefix + input_password)
            
            for suffix in suffixes:
                password_variants.append(input_password + suffix)
            
            return password_variants
        
        return input_password


def generate_password_variants(input_password):
    config = read_config()
    variants = []
    transformations = config.get("transformations", ["upper_no_numbers", "capitalize_first", "all_caps", "reverse", "reverse_upper", "reverse_letters_numbers", "reverse_upper_letters", "numbers_only", "numbers_reverse_letters", "numbers_reverse_upper_letters", "modify_prefix_suffix", "chess_case", "reverse_chess_case", "symmetric_mirror", "mirror_second_half", "mirror_first_half_original", "mirror_second_half_original"])

    for transformation in transformations:
        result = transform_password(input_password, transformation, config)
        if isinstance(result, list):
            variants.extend(result)
        else:
            variants.append(result)
    
    return variants

input_password = "password123"
password_variants = generate_password_variants(input_password)
for variant in password_variants:
    print(variant)
