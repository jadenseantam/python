import os
import sys
import ascii_magic
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init()

chars = "@%#*+=-:. "


def image_to_text(image_path, columns=100, use_color=True): # 50 cols fit in minimized terminal but 100 cols looks better and is fine when maximized

    try:
        my_art = ascii_magic.AsciiArt.from_image(image_path)
        
        ascii_str = my_art.to_ascii(columns=columns)

        base_name = os.path.splitext(image_path)[0]
        output_filename = f"{base_name}.txt"
        
        my_art.to_file(output_filename, columns=columns, monochrome=not use_color)

        print(f"📁 {image_path} ➜ {output_filename}")
        
        if use_color:
            colored_ascii = add_intensity_colors(ascii_str)
            print(colored_ascii)
        else:
            print(ascii_str)

    except Exception as e:
        print(f"❌ Error processing {image_path}: {e}")

def add_intensity_colors(ascii_str):
    # Map characters to colors based on intensity
    char_colors = {
        '@': Fore.WHITE + Style.BRIGHT,
        '%': Fore.LIGHTWHITE_EX,
        '#': Fore.LIGHTCYAN_EX,
        '*': Fore.CYAN,
        '+': Fore.LIGHTBLUE_EX,
        '=': Fore.BLUE,
        '-': Fore.LIGHTBLACK_EX,
        ':': Fore.BLACK + Style.BRIGHT,
        '.': Fore.BLACK,
        ' ': ''
    }
    
    colored_ascii = ""
    for char in ascii_str:
        if char == '\n':
            colored_ascii += char
        else:
            color = char_colors.get(char, Fore.WHITE)
            colored_ascii += color + char + Style.RESET_ALL
    
    return colored_ascii

def process_all_images(folder="./art", use_color=True):
    """Process all image files in the specified folder"""
    # Support multiple image formats
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')
    image_files = [f for f in os.listdir(folder) 
                   if f.lower().endswith(image_extensions)]
    
    if not image_files:
        print("No image files found in the current directory.")
        print(f"Supported formats: {', '.join(image_extensions)}")
        return
    
    print(f"Found {len(image_files)} image file(s). Processing...\n")
    
    for file in image_files:
        image_path = os.path.join(folder, file)
        image_to_text(image_path, use_color=use_color)
        print("-" * 60)  # Separator between images

def display_ascii_file(filename):
    """Display an ASCII art file"""
    try:
        with open(filename, "r", encoding='utf-8') as f:
            content = f.read()
        print(content)
        sys.stdout.flush()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    """Main function to handle command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert images to colored ASCII art')
    parser.add_argument('--folder', '-f', default='.', 
                       help='Folder to process (default: current directory)')
    parser.add_argument('--no-color', action='store_true', 
                       help='Disable color output')
    parser.add_argument('--columns', '-c', type=int, default=100,
                       help='Number of columns for ASCII output (default: 100)')
    parser.add_argument('--single', '-s', type=str,
                       help='Process a single image file')
    parser.add_argument('--display', '-d', type=str,
                       help='Display an existing ASCII art file')
    
    args = parser.parse_args()
    
    use_color = not args.no_color
    
    if args.display:
        display_ascii_file(args.display)
    elif args.single:
        if os.path.exists(args.single):
            image_to_text(args.single, columns=args.columns, use_color=use_color)
        else:
            print(f"File '{args.single}' not found.")
    else:
        process_all_images(args.folder, use_color=use_color)

if __name__ == "__main__":
    # If run directly, process all images in current directory with color
    if len(sys.argv) == 1:
        process_all_images()
    else:
        main()
