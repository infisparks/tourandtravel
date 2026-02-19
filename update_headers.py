import os
import re

base_dir = '/Users/mudassirs472/Desktop/Travel agency'

def get_mega_menu():
    index_path = os.path.join(base_dir, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the mega-menu div. It's inside the Destination li.
    # Looking for <div class="mega-menu"> up to its closing </div>
    # Usually it contains nested divs so we need a balanced search or a greedy one if we know the end.
    # From previous view, the mega-menu ends with </div> and some vectors.
    
    match = re.search(r'<div class="mega-menu">.*?<!--\s*header Section End\s*-->', content, re.DOTALL)
    # That's too much. Let's try to find the specific closing </div> for mega-menu.
    
    # Let's use a simpler approach: finding the Destination <li> and extracting the mega-menu from it.
    li_match = re.search(r'<li class="menu-item-has-children position-inherit">.*?Destination.*?<div class="mega-menu">(.*?)</div>\s*<img src="images/mega-menu-vector1\.svg".*?<img src="images/mega-menu-vector2\.svg".*?</div>\s*</li>', content, re.DOTALL)
    
    if li_match:
        # We want the content inside the <li> but after Destination link
        # Actually, let's just grab the whole <div class="mega-menu">...</div>
        mega_start = content.find('<div class="mega-menu">')
        # Find the end of this div (it contains nested containers/rows)
        depth = 0
        end_idx = -1
        for i in range(mega_start, len(content)):
            if content[i:i+4] == '<div':
                depth += 1
            elif content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    end_idx = i + 6
                    break
        if end_idx != -1:
            return content[mega_start:end_idx]
    
    # Fallback: if script fails, just return a semi-hardcoded one or try another regex
    return None

def update_pages():
    mega_menu_html = get_mega_menu()
    if not mega_menu_html:
        print("Failed to extract mega menu from index.html")
        # I'll use a simplified version or try harder
        return

    # Modernized Destination Mega Menu (point all details links to placedetail/index.html)
    mega_menu_html = mega_menu_html.replace('destination-details.html', 'placedetail/index.html')

    pages = [
        ('index.html', ''),
        ('placedetail/index.html', 'placedetail'),
        ('travelpackage/index.html', 'travelpackage'),
        ('hoteldetail/index.html', 'hoteldetail')
    ]

    for rel_path, folder in pages:
        full_path = os.path.join(base_dir, rel_path)
        if not os.path.exists(full_path):
            continue
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        root_prefix = '../' if folder else ''
        
        # Prepare page-specific mega menu
        target_mega = mega_menu_html.replace('placedetail/index.html', f'{root_prefix}placedetail/index.html')
        # Flags use images/ which is local to each folder, so we keep them as is.
        # Except maybe if they aren't in the subfolder images? 
        # But my check on placedetail/images showed they ARE there.

        new_menu = f"""<ul class="menu-list">
                        <li>
                            <a href="{root_prefix}index.html">Home</a>
                        </li>
                        <li class="menu-item-has-children position-inherit">
                            <a href="#" class="drop-down">
                                Destination
                                <i class="bi bi-caret-down-fill"></i>
                            </a>
                            <i class="bi bi-plus dropdown-icon"></i>
                            {target_mega}
                        </li>
                        <li>
                            <a href="{root_prefix}travelpackage/index.html">Travel Package</a>
                        </li>
                        <li>
                            <a href="{root_prefix}hoteldetail/index.html">Hotel Booking</a>
                        </li>
                    </ul>"""

        # Replace the main menu-list
        start_marker = '<ul class="menu-list">'
        start_idx = content.find(start_marker)
        if start_idx != -1:
            depth = 0
            end_idx = -1
            for i in range(start_idx, len(content)):
                if content[i:i+3] == '<ul':
                    depth += 1
                elif content[i:i+5] == '</ul>':
                    depth -= 1
                    if depth == 0:
                        end_idx = i + 5
                        break
            
            if end_idx != -1:
                new_content = content[:start_idx] + new_menu + content[end_idx:]
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {rel_path}")

if __name__ == "__main__":
    update_pages()
    print("Header update complete.")
