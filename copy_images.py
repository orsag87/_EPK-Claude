#!/usr/bin/env python3
import shutil
import os

# Define source and destination paths
images_to_copy = {
    # Album covers
    "/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Music/! 2025/YAWNIN' EP/Artboard 1.png":
        "images/albums/yawnin-ep.png",

    # Logo files
    "/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Graphic Design/! DJY_Brand Assets/DJ YAWN Logo 2025_White.png":
        "images/logo/logo-white.png",
    "/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Graphic Design/! DJY_Brand Assets/DJ YAWN Logo 2025_Black.png":
        "images/logo/logo-black.png",

    # Featured photos
    "/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/Feature Photos/DJ YAWN 3_Mid2024.png":
        "images/photos/featured-1.png",
    "/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/Feature Photos/SXSW2024(3)-@jasonvaughan.ca-172 copy.png":
        "images/photos/featured-2.png",
    "/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/DJ YAWN_Promo Photos/DJ YAWN_Shambs.png":
        "images/photos/featured-3.png",

    # Background textures
    "/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v.13/Assets/Images/Glitch_texture_1.png":
        "images/backgrounds/glitch-1.png",
    "/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Graphic Design/Pro Templates/hardtone-gradient-texture-2022-11-30-23-55-08-utc/04.-Hardtone-Gradient-Texture.jpg":
        "images/backgrounds/gradient.jpg",
    "/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v.13/Assets/Images/Glitch_texture_3.png":
        "images/backgrounds/glitch-3.png",
    "/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v.13/Assets/Images/Glitch_texture_4.png":
        "images/backgrounds/glitch-4.png",
    "/Users/janorsag/Dropbox/! Motion Graphics/FX_Presets_Bundle_v.13/Assets/Images/Glitch_texture_2.png":
        "images/backgrounds/glitch-2.png",

    # Icons for value proposition
    "/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/88.png":
        "images/icons/icon-88.png",
    "/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/77.png":
        "images/icons/icon-77.png",
    "/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/89.png":
        "images/icons/icon-89.png",
    "/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/76.png":
        "images/icons/icon-76.png",
    "/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/74.png":
        "images/icons/icon-74.png",
    "/Users/janorsag/Dropbox/! Graphic Design_Textures_Mock Ups_Etc/Main/PNG/63.png":
        "images/icons/icon-63.png",

    # Mix backgrounds
    "/Users/janorsag/Dropbox/! DJ YAWN/! DJ YAWN_Vids & Assets/! DJ YAWN_Sets/Shambhala 2025/Screenshots/DJ YAWN Shambhala.png":
        "images/mixes/shambs-bg.png",
    "/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/DJ YAWN_Promo Photos/DJ YAWN 4_Early2023 wide.jpg":
        "images/mixes/rooftop-bg.jpg",
    "/Users/janorsag/Dropbox/! DJ YAWN/! Photos & Videos_DJ YAWN/Photos DJ YAWN/DJ YAWN_Promo Photos/DJ YAWN_SXSW2024.png":
        "images/mixes/festival-bg.png",
}

# Get the base directory (where this script is located)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Copy each file
copied = 0
failed = 0
for source, dest_relative in images_to_copy.items():
    dest = os.path.join(base_dir, dest_relative)
    try:
        if os.path.exists(source):
            shutil.copy2(source, dest)
            print(f"✓ Copied: {os.path.basename(dest)}")
            copied += 1
        else:
            print(f"✗ Not found: {source}")
            failed += 1
    except Exception as e:
        print(f"✗ Error copying {os.path.basename(dest)}: {e}")
        failed += 1

print(f"\n{copied} files copied successfully, {failed} failed")
