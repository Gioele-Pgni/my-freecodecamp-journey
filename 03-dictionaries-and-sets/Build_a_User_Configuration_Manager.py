def add_setting(add_dizionario,add_tupla): 
    add_tupla = tuple(x.lower() for x in add_tupla)
    if not add_tupla[0] in add_dizionario:
        add_dizionario[add_tupla[0]] = add_tupla[1]
        return  f"Setting '{add_tupla[0]}' added with value 'high' successfully!"
    else:
        return f"Setting '{add_tupla[0]}' already exists! Cannot add a new setting with this name."
    
def update_setting(up_dizionario , up_tupla):
    up_tupla = tuple(x.lower() for x in up_tupla)
    if up_tupla[0] in up_dizionario:
        up_dizionario.update({up_tupla[0]:up_tupla[1]})
        return f"Setting '{up_tupla[0]}' updated to '{up_tupla[1]}' successfully!"
    else:
        return f"Setting '{up_tupla[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(del_dizionario , chiave):
    lower_chiave = chiave.lower()
    if lower_chiave in del_dizionario:
        del_dizionario.pop(lower_chiave)
        return f"Setting '{lower_chiave}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(view_dizionario):
    if not view_dizionario: 
        return "No settings available."
    stringa = "Current User Settings:\n"
    for chiave,valore in view_dizionario.items():
        stringa += chiave.title() + ": " + valore + "\n"
    return stringa
        
        

test_settings = {"CHIAVE":"VALORE"}
add_setting({'theme': 'light'}, ('volume', 'high'))
delete_setting({'theme': 'light'}, 'theme')
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
