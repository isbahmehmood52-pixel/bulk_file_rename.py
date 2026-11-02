# bulk_file_rename.py
📁 Bulk File Renamer (Python)

A powerful, efficient, and versatile Python utility designed to rename multiple files in bulk based on customizable patterns, prefixes, suffixes, extensions, and sequential numbering.

✨ Features

🔢 Sequential Numbering: Automatically number files sequentially (e.g., file_001.jpg, file_002.jpg).

🏷️ Custom Prefixes & Suffixes: Add custom text to the beginning or end of file names.

🔄 Find & Replace: Search for specific text patterns across all files and replace them.

🏷️ Extension Modification: Convert or change file extensions in bulk (e.g., .JPEG to .png).

🛑 Dry-Run / Preview Mode: Preview the new file names before actually committing any changes to disk.

⚡ Regex Support: Use Regular Expressions for complex pattern matching and renaming.

📂 Recursive Directory Renaming: Process files in subdirectories recursively.

🛠️ Built With

Python 3.x - Core programming language.

os & pathlib - Native modules for filesystem interaction and path manipulation.

argparse - Command-line interface parsing.

🚀 Getting Started

Prerequisites

Make sure you have Python 3.8+ installed. Check your version with:

python --version


Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/bulk-file-renamer.git
cd bulk-file-renamer


Run directly (No third-party packages required for standard CLI version):

python main.py --help


🕹️ Usage & Examples

1. Add Prefix to All Files

python main.py --dir "/path/to/folder" --prefix "Vacation2026_"


2. Replace Text in File Names

python main.py --dir "/path/to/folder" --find "OLD_NAME" --replace "NEW_NAME"


3. Sequential Numbering

python main.py --dir "/path/to/folder" --base-name "Photo" --digits 3
# Output: Photo_001.jpg, Photo_002.jpg, ...


4. Change File Extensions

python main.py --dir "/path/to/folder" --old-ext ".JPEG" --new-ext ".jpg"


5. Dry-Run (Safe Preview)

python main.py --dir "/path/to/folder" --prefix "Test_" --dry-run


🗺️ Roadmap & Future Enhancements

[ ] 🖥️ GUI Interface: Add a graphical desktop interface using Tkinter or PyQt.

[ ] ↩️ Undo Feature: Save a local history log to easily undo accidental renames.

[ ] 🖼️ EXIF Metadata Renaming: Rename image files automatically based on their Creation Date/Time or Camera Model.

[ ] 🎵 ID3 Tag Renaming: Rename MP3 files based on Artist, Album, and Track Title metadata.

🤝 Contributing

Contributions make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are greatly appreciated!

Fork the Project.

Create your Feature Branch (git checkout -b feature/NewFeature).

Commit your Changes (git commit -m 'Add NewFeature').

Push to the Branch (git push origin feature/NewFeature).
