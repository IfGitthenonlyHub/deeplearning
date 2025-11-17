import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIGZpbmRfY29tYmluYXRpb25zKGxpc3QsIHN1bSk6CiBpZiBub3QgbGlzdDoKICBpZiBzdW0gPT0gMDoKICAgcmV0dXJuIFtbXV0KICByZXR1cm4gW10KIHJldHVybiBmaW5kX2NvbWJpbmF0aW9ucyhsaXN0WzE6XSwgc3VtKSArIFwKICBbW2xpc3RbMF1dICsgdGFpbCBmb3IgdGFpbCBpbgogICBmaW5kX2NvbWJpbmF0aW9ucyhsaXN0WzE6XSwgc3VtIC0gbGlzdFswXSldCmZvciB0YyBpbiByYW5nZShpbnQoaW5wdXQoKSkpOgogbixrPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQogYT1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKIGEuc29ydCgpCiBpZiBsZW4oZmluZF9jb21iaW5hdGlvbnMoYSxrKSk9PTA6CiAgcHJpbnQoIk5PIikKIGVsc2U6CiAgcHJpbnQoIllFUyIp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
