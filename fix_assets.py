import os
import shutil
import re

# Config
base_dir = '/Users/mudassirs472/Desktop/Travel agency'
target_folders = ['placedetail', 'travelpackage', 'hoteldetail']
assets_to_fix = ['css', 'js', 'fonts']

def fix_assets():
    for folder in target_folders:
        dir_path = os.path.join(base_dir, folder)
        if not os.path.isdir(dir_path):
            print(f"Directory {dir_path} not found, skipping.")
            continue

        # 1. Update index.html
        index_path = os.path.join(dir_path, 'index.html')
        if os.path.exists(index_path):
            print(f"Processing {index_path}...")
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Update assets paths: css/, js/, fonts/ -> ../css/, ../js/, ../fonts/
            # We use a regex that looks for href= or src= followed by the asset folder
            for asset in assets_to_fix:
                # Match: href="css/ or src="js/ or href='fonts/ etc.
                # Group 1: href or src
                # Group 2: quote (" or ')
                # Group 3: asset name (css, js, fonts)
                pattern = rf'(href|src)=(["\']){asset}/'
                replacement = r'\1=\2../' + asset + '/'
                content = re.sub(pattern, replacement, content)
            
            # Also update the home link index.html -> ../index.html
            # This is common in headers
            content = re.sub(r'href=(["\'])index\.html', r'href=\1../index.html', content)

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated paths in {index_path}")

        # 2. Remove asset folders
        for asset in assets_to_fix:
            asset_path = os.path.join(dir_path, asset)
            if os.path.exists(asset_path):
                try:
                    if os.path.isdir(asset_path):
                        shutil.rmtree(asset_path)
                        print(f"  Removed directory: {asset_path}")
                    else:
                        os.remove(asset_path)
                        print(f"  Removed file: {asset_path}")
                except Exception as e:
                    print(f"  Error removing {asset_path}: {e}")

if __name__ == "__main__":
    fix_assets()
    print("\nAll tasks completed successfully.")
