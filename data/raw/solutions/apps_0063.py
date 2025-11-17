import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("dD1pbnQoaW5wdXQoKSkKZm9yIGkgaW4gcmFuZ2UodCk6CiAgICBuLGs9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiAgICBhPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQogICAgdz1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKICAgIGEuc29ydCgpCiAgICBhLnJldmVyc2UoKQogICAgdy5zb3J0KCkKICAgIGFucz0wCiAgICBmb3IgaSBpbiByYW5nZShrKToKICAgICAgICBhbnMrPWFbaV0KICAgIHBvaW50ZXI9ay0xCiAgICBmb3IgaSBpbiByYW5nZShrKToKICAgICAgICBpZiB3W2ldPT0xOgogICAgICAgICAgICBhbnMrPWFbaV0KICAgICAgICAgICAgY29udGludWUKICAgICAgICBwb2ludGVyKz13W2ldLTEKICAgICAgICBhbnMrPWFbcG9pbnRlcl0KICAgIHByaW50KGFucyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
