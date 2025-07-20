import os

TEMPLATES = {
    "README.md": """# Project Overview

Welcome! This folder contains part of a larger project managed by CosmicJesterX.

## About

Briefly describe this part of your project here.  
If this is a standalone module or package, add usage instructions.

## How to Use

- (If required) Install dependencies listed in [requirements.txt](./requirements.txt).
- Follow additional instructions in this README or the main project README.

## Contributing

Improvements are welcome! If you spot a bug or want to contribute, please open an issue or pull request.

## License

See [LICENSE](./LICENSE) for details.
""",
    "LICENSE": """MIT License

Copyright (c) 2025 CosmicJesterX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
    "SECURITY.md": """# Security Policy

## Reporting Issues

If you discover a security vulnerability or have a concern, please open an issue or contact CosmicJesterX directly.

## Commitment

We are committed to keeping this project and its users safe. Thank you for helping us improve security!
""",
    "requirements.txt": """# List Python dependencies here, one per line.
# Example:
# requests>=2.0.0
"""
}

def get_target_dirs(root):
    # Collect root, first-level, and second-level directories
    dirs = set([root])
    for dirpath, dirnames, _ in os.walk(root):
        # Only go two levels deep
        rel_path = os.path.relpath(dirpath, root)
        if rel_path == ".":
            # Add first-level dirs
            for d in dirnames:
                dirs.add(os.path.join(dirpath, d))
        elif len(rel_path.split(os.sep)) == 1:
            # Add second-level dirs
            for d in dirnames:
                dirs.add(os.path.join(dirpath, d))
    return dirs

def main():
    root = os.path.abspath(".")
    target_dirs = get_target_dirs(root)
    for d in target_dirs:
        for fname, content in TEMPLATES.items():
            fpath = os.path.join(d, fname)
            if not os.path.exists(fpath):
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Created {fpath}")

if __name__ == "__main__":
    main()
