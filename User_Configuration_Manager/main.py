def add_setting(settings, new_setting):
    raw_key, raw_value = new_setting
    key = str(raw_key).lower()
    value = str(raw_value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new_setting):
    raw_key, raw_value = new_setting
    key = str(raw_key).lower()
    value = str(raw_value).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, raw_key):
    key = str(raw_key).lower()

    if key in settings_dict:
        settings_dict.pop(key)
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."

    result = "Current User Settings:"

    for key, value in settings_dict.items():
        result += f"\n{key.capitalize()}: {value}"
        
    return result + "\n"

test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high'
}