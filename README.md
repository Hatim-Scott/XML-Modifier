# XML-Modifier

## Download

We provide **ready-to-use files** for Windows and macOS:

### Windows

1. Go to the [Releases page](https://github.com/Hatim-Scott/XML-Modifier/releases)  
2. Download the latest `.exe` file
3. Open the app — no need to install Python or any dependencies  

> ⚠️ Windows may warn that the app is from an unidentified developer
> Click on **more options** → **Run Anyway**

### MacOS

1. Go to the [Releases page](https://github.com/Hatim-Scott/XML-Modifier/releases)  
2. Download the latest `.zip` file
3. Extract the contents of the file
4. Open the app — no need to install Python or any dependencies  

> ⚠️ MacOS may warn that the app is from an unidentified developer
> To see how to open, go to [this page](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unknown-developer-mh40616/mac)

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
- Settings file is generated at root user directory for Windows and at app directory for macOS
