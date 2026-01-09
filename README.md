# DJ YAWN - EPK (Electronic Press Kit)

**Clean, organized, web-ready EPK project**

## 📁 Project Structure

```
_EPK-Claude/
├── index.html              # Main EPK file (web-ready)
├── images/
│   ├── albums/            # Album covers (muse-ep.png, yawnin-ep.png)
│   ├── backgrounds/       # Background textures
│   ├── icons/             # Value proposition icons
│   ├── logo/              # DJ YAWN logos (white & black)
│   ├── mixes/             # Mix background images
│   └── photos/            # Featured promo photos
├── downloads/
│   └── press-photos.zip   # Press photo package (if available)
├── copy_images.py         # Script to copy images from Dropbox
├── convert_to_web.py      # Script to convert paths to web-ready
└── README.md              # This file
```

## 🚀 Quick Start

### View Locally
1. Open `index.html` in your web browser
2. All images should load (they use relative paths)

### Deploy to GitHub Pages

#### First Time Setup:
1. Open GitHub Desktop
2. Click "Add" → "Add Existing Repository"
3. Choose this folder: `/Users/janorsag/Dropbox/SANDBOX_1/_EPK-Claude`
4. Click "Create Repository" if prompted
5. Name it: `dj-yawn-epk`
6. Click "Publish Repository"
7. **Uncheck** "Keep this code private" (for GitHub Pages to work on free plan)
8. Click "Publish Repository"

#### Enable GitHub Pages:
1. Go to: https://github.com/YOUR-USERNAME/dj-yawn-epk
2. Click "Settings" tab
3. Click "Pages" in the left sidebar
4. Under "Source", select "main" branch
5. Click "Save"
6. Wait 1-2 minutes
7. Your EPK will be live at: `https://YOUR-USERNAME.github.io/dj-yawn-epk/`

#### Future Updates (After First Setup):
1. Make your edits to `index.html`
2. Open GitHub Desktop
3. It will show your changes
4. Add a commit message (e.g., "Update bio section")
5. Click "Commit to main"
6. Click "Push origin"
7. Changes appear online in 1-2 minutes

## ✏️ Making Edits

### Edit Content
1. Open `index.html` in any text editor (VS Code recommended)
2. Search for the text you want to change
3. Edit it
4. Save the file
5. Test locally by opening `index.html` in browser
6. Push to GitHub (see above)

### Add New Images
1. Copy your image to the appropriate folder in `images/`
2. Give it a simple name (e.g., `new-photo.png`)
3. In `index.html`, reference it as: `images/photos/new-photo.png`
4. Test locally
5. Push to GitHub

### Update Album Covers
1. Replace files in `images/albums/` folder
2. Keep the same filenames (`muse-ep.png`, `yawnin-ep.png`)
3. OR edit `index.html` and change the filename
4. Test locally
5. Push to GitHub

## 🔄 Updating from Source

If you edit the original `DJ_YAWN_EPK_FINAL.html` in Content_Research:

```bash
# Run the conversion script
cd /Users/janorsag/Dropbox/SANDBOX_1/_EPK-Claude
python3 convert_to_web.py
```

This will:
- Read the latest `DJ_YAWN_EPK_FINAL.html`
- Convert all Dropbox paths to web-ready paths
- Save to `index.html`

## 🎯 What This Fixes

✅ **Album images now work on GitHub Pages**
✅ **All images use relative paths**
✅ **Clean, organized file structure**
✅ **Easy to edit and update**
✅ **No broken images online**

## 📋 Next Steps

1. ✅ Test locally - DONE (you just opened it in browser)
2. 🔲 Push to GitHub using GitHub Desktop
3. 🔲 Enable GitHub Pages in repository settings
4. 🔲 Share your live EPK link!

---

**Questions?** Check your GitHub repository at: https://github.com/YOUR-USERNAME/dj-yawn-epk

**The old `dj-yawn-epk-web` folder can be deleted** - everything you need is here in `_EPK-Claude`
