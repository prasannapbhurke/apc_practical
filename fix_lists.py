import docx
import glob
import os

doc = docx.Document('list.docx')
paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

# Manual mapping of program numbers to paragraph ranges
program_ranges = {
    65: (0, 0),
    66: (1, 4),
    67: (5, 5),
    68: (6, 10),
    69: (11, 15),
    70: (16, 16),
    71: (17, 19),
    72: (20, 22),
    73: (23, 23),
    74: (24, 24),
    75: (25, 30),
    76: (31, 31),
    77: (32, 34),
    78: (35, 35),
    79: (36, 36),
    80: (37, 41),
    81: (42, 42),
    82: (43, 48),
    83: (49, 53),
    84: (54, 59),
    85: (60, 60),
    86: (61, 61),
    87: (62, 62),
    88: (63, 65),
    89: (66, 66),
    90: (67, 72),
    91: (73, 78),
    92: (79, 85),
    93: (86, 91),
    94: (92, 97),
}

for num, (start, end) in program_ranges.items():
    files = glob.glob(f'{num}_list_*.py')
    if not files:
        continue
    fpath = files[0]
    
    # Get program text from paragraphs
    prog_text = '\n'.join(paragraphs[start:end+1])
    
    with open(fpath, 'r', encoding='latin-1') as f:
        lines = f.readlines()
    
    # Remove existing comment lines at the top
    code_lines = []
    skipping_comments = True
    for line in lines:
        if skipping_comments and line.strip().startswith('#'):
            continue
        skipping_comments = False
        code_lines.append(line)
    
    # Build new comment block with proper newlines
    comment_lines = ['# ' + line + '\n' for line in prog_text.split('\n')]
    comment_lines.append('\n')  # blank line after comment
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.writelines(comment_lines + code_lines)
    
    print(f'Updated {os.path.basename(fpath)}')
