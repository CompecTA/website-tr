import os
import shutil
from jinja2 import Environment, FileSystemLoader

def build():
    # Directories from blatter.ini
    static_dir = 'static'
    template_dir = 'templates'
    dynamic_dir = 'site'
    output_dir = 'out'

    # Ensure output directory exists and is empty
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_dir))

    # Render dynamic pages from 'site' directory
    for root, dirs, files in os.walk(dynamic_dir):
        for file in files:
            if file.endswith('.html'):
                # Get the relative path for the template
                rel_dir = os.path.relpath(root, dynamic_dir)
                if rel_dir == '.':
                    rel_dir = ''
                
                # Jinja2 expects template names with forward slashes
                template_path = os.path.join(dynamic_dir, rel_dir, file)
                
                # Create output directory structure
                out_page_dir = os.path.join(output_dir, rel_dir)
                if not os.path.exists(out_page_dir):
                    os.makedirs(out_page_dir)

                # Render the file
                # Note: blatter treats files in 'site' as templates themselves
                # but they usually extend a base template.
                # We'll load the file content and render it.
                with open(os.path.join(root, file), 'r') as f:
                    template_content = f.read()
                
                template = env.from_string(template_content)
                output = template.render()

                with open(os.path.join(out_page_dir, file), 'w') as f:
                    f.write(output)
                print(f"Rendered: {os.path.join(rel_dir, file)}")

    # Copy static assets
    if os.path.exists(static_dir):
        for item in os.listdir(static_dir):
            s = os.path.join(static_dir, item)
            d = os.path.join(output_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy(s, d)
        print(f"Copied static assets from {static_dir}")

    # Create CNAME file for GitHub Pages
    with open(os.path.join(output_dir, 'CNAME'), 'w') as f:
        f.write('compecta.com.tr')
    print("Created CNAME file for compecta.com.tr")

if __name__ == "__main__":
    build()
