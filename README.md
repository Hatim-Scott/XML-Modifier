# XML-Modifier

## Download

We provide **ready-to-use files** for Windows and macOS:

1. Go to the [Releases page](https://github.com/Hatim-Scott/XML-Modifier/releases)  
2. Download the latest `.exe` file (Windows executable) **OR** Download the latest `.app` file (macOS executable)
3. Open the app — no need to install Python or any dependencies  

> ⚠️ macOS may warn that the app is from an unidentified developer.  
> Right-click → Open → Confirm to launch.

---

## Using the App

1. **Tag Name** – Name of the XML tag to modify
2. **Old Prefix** – Prefix to detect at the start of the tag text  
3. **Replace With** – New prefix to replace the old one  
4. **Folder** – Folder containing XML files  

**Buttons**:

- **Browse Folder** – select the folder containing XML files  
- **Run** – modify all XML files in the folder and save backups  
- **Restore from Backup** – restore all files from the `/backup` subfolder  

---

## Notes

- Backups are stored in a subfolder named `/backup` inside your selected folder.  
- Only `.xml` files in the selected folder are processed (subfolders are ignored).  
