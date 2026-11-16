# -*- coding: utf-8 -*-
import os
import sys
import re

from head import get_head_and_nav
from section_sum import get_section_sum
from section_lab1 import get_section_lab1
from section_lab2 import get_section_lab2
from section_lab3 import get_section_lab3
from section_lab4 import get_section_lab4
from section_lab5 import get_section_lab5
from section_lab6 import get_section_lab6
from section_lab7 import get_section_lab7
from section_lab8 import get_section_lab8
from section_lab9 import get_section_lab9
from section_lab10 import get_section_lab10
from section_lab11 import get_section_lab11
from section_exam import get_section_exam
from section_calc import get_section_calc
from section_ref import get_section_ref
from foot import get_foot

OUT_PATH = "/Users/thanaporn/.gemini/antigravity/scratch/CE272/index.html"
ARTIFACT_PATH = "/Users/thanaporn/.gemini/antigravity/brain/0086b3cd-d8df-4e9e-86fd-d675957ab350/CE272_all_chapters.html"

def build():
    sections = [
        get_head_and_nav(),
        get_section_sum(),
        get_section_lab1(),
        get_section_lab2(),
        get_section_lab3(),
        get_section_lab4(),
        get_section_lab5(),
        get_section_lab6(),
        get_section_lab7(),
        get_section_lab8(),
        get_section_lab9(),
        get_section_lab10(),
        get_section_lab11(),
        get_section_exam(),
        get_section_calc(),
        get_section_ref(),
        get_foot()
    ]
    
    html = "".join(sections)
    
    # Validation 1: Check for corrupt Thai OCR characters
    bad_chars = [
        "เปŨน", "ปŗด", "เปŗด", "โตŢะ", "นาŲิกา", "ปŦจจัย", "ผูš", "สŠง", 
        "อยŠาง", "ขšอมูล", "ตšอง", "เสšน", "สมดุลยŤ", "ศูนยŤ", "ทุŠน", 
        "ปŦũนปśวน", "ฝŦũง", "สัมประสิทธŤ", "เปล่ยีม", "บรเิวณ"
    ]
    found_bad = []
    for bc in bad_chars:
        if bc in html:
            found_bad.append(bc)
    if re.search(r'สัมประสิทธิ(?!์)', html):
        found_bad.append("สัมประสิทธิ (ไม่มีการันต์)")
            
    if found_bad:
        print("⚠️ WARNING: Found corrupted OCR characters in HTML:", found_bad)
        sys.exit(1)
    else:
        print("✅ Proofreading Check Passed: Zero corrupted Thai characters found!")

    # Validation 2: KaTeX balance check
    double_dollars = html.count("$$")
    if double_dollars % 2 != 0:
        print(f"⚠️ WARNING: Unbalanced $$ delimiters! Total count: {double_dollars}")
        sys.exit(1)
    else:
        print(f"✅ KaTeX Check Passed: All {double_dollars} $$ delimiters are balanced ({double_dollars//2} display equations).")

    inline_open = html.count(r"\(")
    inline_close = html.count(r"\)")
    if inline_open != inline_close:
        print(f"⚠️ WARNING: Unbalanced \\( ({inline_open}) and \\) ({inline_close}) delimiters!")
        sys.exit(1)
    else:
        print(f"✅ KaTeX Inline Check Passed: All {inline_open} inline \\(...\\) delimiters are balanced.")

    aligned_begin = html.count(r"\begin{aligned}")
    aligned_end = html.count(r"\end{aligned}")
    if aligned_begin != aligned_end:
        print(f"⚠️ WARNING: Unbalanced \\begin{{aligned}} ({aligned_begin}) and \\end{{aligned}} ({aligned_end})!")
        sys.exit(1)
    else:
        print(f"✅ KaTeX Aligned Check Passed: All {aligned_begin} aligned environments are balanced.")

    # Validation 3: Check for syntax bugs that KaTeX hates
    if re.search(r'\\text\{[^}]*\^', html):
        print("⚠️ WARNING: Found ^ inside \\text{...} in HTML! This will cause KaTeX parse errors.")
        sys.exit(1)
    if "√" in html:
        # Check if √ is used inside LaTeX math delimiters
        math_matches = re.findall(r'\$\$(.*?)\$\$|\\\((.*?)\\\)', html, re.DOTALL)
        for m in math_matches:
            expr = m[0] or m[1]
            if "√" in expr:
                print("⚠️ WARNING: Found unicode √ inside math expression! Use \\sqrt{} instead.")
                sys.exit(1)

    print("✅ KaTeX Syntax Audit Passed: Zero invalid constructs found!")

    # Write to local repo index.html
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Written {len(html):,} bytes to {OUT_PATH}")

    # Write to artifact directory and sync assets
    import shutil
    try:
        with open(ARTIFACT_PATH, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Written copy to Artifact path: {ARTIFACT_PATH}")
        brain_assets = os.path.dirname(ARTIFACT_PATH) + "/assets"
        os.makedirs(brain_assets, exist_ok=True)
        for item in os.listdir("/Users/thanaporn/.gemini/antigravity/scratch/CE272/assets"):
            s = os.path.join("/Users/thanaporn/.gemini/antigravity/scratch/CE272/assets", item)
            d = os.path.join(brain_assets, item)
            shutil.copy2(s, d)
        print(f"✅ Synchronized assets to {brain_assets}")
    except Exception as e:
        print("Artifact copy notice:", e)

if __name__ == "__main__":
    build()
