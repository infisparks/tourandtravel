import os

base_dir = '/Users/mudassirs472/Desktop/Travel agency'

old_number_digits = '91345533865'
old_number_display = '+91 345 533 865'

new_number_digits = '919289350752'
new_number_display = '+91-9289350752'

def update_phone_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace formatted display number
    content = content.replace(old_number_display, new_number_display)
    
    # Replace digits in tel links and wa.me links
    # tel:91345533865 -> tel:919289350752
    content = content.replace(f'tel:{old_number_digits}', f'tel:{new_number_digits}')
    content = content.replace(f'tel:+{old_number_digits}', f'tel:+{new_number_digits}')
    
    # wa.me/91345533865 -> wa.me/919289350752
    content = content.replace(f'wa.me/{old_number_digits}', f'wa.me/{new_number_digits}')
    content = content.replace(f'wa.me/+{old_number_digits}', f'wa.me/+{new_number_digits}')

    # Aggressive replacement for any remaining digits if they match exactly
    content = content.replace(old_number_digits, new_number_digits)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def walk_and_update():
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Updating phone numbers in: {file_path}")
                update_phone_in_file(file_path)

if __name__ == "__main__":
    walk_and_update()
    print("\nPhone number update complete.")
