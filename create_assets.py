import os
import zipfile
from PIL import Image
import cairosvg

# Ensure downloads directory exists
os.makedirs('downloads', exist_ok=True)

# Convert SVG to PNG
cairosvg.svg2png(url='sou_portal_logo.svg', write_to='sou_portal_logo.png', output_width=1000, output_height=1000)

# Create ZIP file
with zipfile.ZipFile('downloads/logos_sou_portal.zip', 'w') as zipf:
    zipf.write('sou_portal_logo.svg', arcname='sou_portal_logo.svg')
    zipf.write('sou_portal_logo.png', arcname='sou_portal_logo.png')

print("Assets created successfully.")
