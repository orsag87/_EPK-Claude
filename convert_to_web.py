#!/usr/bin/env python3
"""
Convert DJ_YAWN_EPK_FINAL.html to web-ready version with relative paths
"""
import re

# Path mapping - convert absolute Dropbox paths to relative web paths
path_mappings = {
    # Logo
    r'/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Graphic Design/! DJY_Brand Assets/DJ YAWN Logo 2025_White\.png': 'images/logo/logo-white.png',
    r'/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Graphic Design/! DJY_Brand Assets/DJ YAWN Logo 2025_Black\.png': 'images/logo/logo-black.png',

    # Featured photos
    r'/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/Feature Photos/DJ YAWN 3_Mid2024\.png': 'images/photos/featured-1.png',
    r'/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/Feature Photos/SXSW2024\(3\)-@jasonvaughan\.ca-172 copy\.png': 'images/photos/featured-2.png',
    r'/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/DJ YAWN_Promo Photos/DJ YAWN_Shambs\.png': 'images/photos/featured-3.png',

    # Background images
    r'/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v\.13/Assets/Images/Glitch_texture_1\.png': 'images/backgrounds/glitch-1.png',
    r'/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Graphic Design/Pro Templates/hardtone-gradient-texture-2022-11-30-23-55-08-utc/04\.-Hardtone-Gradient-Texture\.jpg': 'images/backgrounds/gradient.jpg',
    r'/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v\.13/Assets/Images/Glitch_texture_3\.png': 'images/backgrounds/glitch-3.png',
    r'/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v\.13/Assets/Images/Glitch_texture_4\.png': 'images/backgrounds/glitch-4.png',
    r'/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v\.13/Assets/Images/Glitch_texture_2\.png': 'images/backgrounds/glitch-2.png',

    # Icons
    r'/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/88\.png': 'images/icons/icon-88.png',
    r'/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/77\.png': 'images/icons/icon-77.png',
    r'/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/89\.png': 'images/icons/icon-89.png',
    r'/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/76\.png': 'images/icons/icon-76.png',
    r'/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/74\.png': 'images/icons/icon-74.png',
    r'/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/63\.png': 'images/icons/icon-63.png',

    # Album covers
    r'/Users/janorsag/Dropbox/! ill\.Gates/ill\.GATES - Complete Discography/PDJ094_ill\.Gates \+ DJ YAWN - The Muse EP/Muse EP Take 1\.png': 'images/albums/muse-ep.png',
    r'/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Music/! 2025/YAWNIN\' EP/Artboard 1\.png': 'images/albums/yawnin-ep.png',

    # Mix backgrounds
    r'/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Vids & Assets/! DJ YAWN_Sets/Shambhala 2025/Screenshots/DJ YAWN Shambhala\.png': 'images/mixes/shambs-bg.png',
    r'/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/DJ YAWN_Promo Photos/DJ YAWN 4_Early2023 wide\.jpg': 'images/mixes/rooftop-bg.jpg',
    r'/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/DJ YAWN_Promo Photos/DJ YAWN_SXSW2024\.png': 'images/mixes/festival-bg.png',

    # Press photos zip (if referenced)
    r'/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/DJ YAWN_Press Photos\.zip': 'downloads/press-photos.zip',
}

def convert_paths(html_content):
    """Replace absolute paths with relative web paths"""
    converted = html_content
    replacements_made = 0

    for old_path, new_path in path_mappings.items():
        # Count matches before replacement
        matches = len(re.findall(old_path, converted))
        if matches > 0:
            converted = re.sub(old_path, new_path, converted)
            print(f"✓ Replaced {matches}x: {new_path}")
            replacements_made += matches

    return converted, replacements_made

def main():
    # Read the source HTML
    source_file = '/Users/janorsag/Dropbox/SANDBOX_1/Content_Research/DJ_YAWN_EPK_FINAL.html'
    output_file = '/Users/janorsag/Dropbox/SANDBOX_1/_EPK-Claude/index.html'

    print("Converting EPK to web-ready version...\n")

    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Convert paths
        converted_html, count = convert_paths(html_content)

        # Write output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(converted_html)

        print(f"\n✓ Successfully converted {count} paths")
        print(f"✓ Web-ready EPK saved to: {output_file}")

    except Exception as e:
        print(f"✗ Error: {e}")
        return 1

    return 0

if __name__ == '__main__':
    exit(main())
