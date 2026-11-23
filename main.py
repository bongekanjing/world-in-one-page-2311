"""Write the day's front page to /output/entry.png.

The page is drawn by render.py from record.py, both of which the agent wrote in
the session shipped with this entry; the PNG they produce is held beside this
file so the program needs neither Pillow nor a font in the sandbox, which
carries the standard library alone. Copying bytes that are already decided is
also what makes the two runs identical: there is no clock, no random seed and
no font fallback that could differ between them.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "page.png"),
                    os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()
