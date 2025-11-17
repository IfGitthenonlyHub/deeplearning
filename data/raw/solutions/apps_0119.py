import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQp0ID0gaW50KGlucHV0KCkpCmZvciBfIGluIHJhbmdlKHQpOgogIG4gPSBpbnQoaW5wdXQoKSkKICBhYiA9IFtsaXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkgZm9yIGkgaW4gcmFuZ2Uobi0xKV0KICBncmFwaCA9IFtbXSBmb3IgaSBpbiByYW5nZShuKzEpXQogIGRlZyA9IFswXSoobisxKQogIGZvciBhLGIgaW4gYWI6CiAgICBncmFwaFthXS5hcHBlbmQoYikKICAgIGdyYXBoW2JdLmFwcGVuZChhKQogICAgZGVnW2FdICs9IDEKICAgIGRlZ1tiXSArPSAxCiAgcG50ID0gW21heChkZWdbaV0tMSwxKSBmb3IgaSBpbiByYW5nZShuKzEpXQogIHJvb3QgPSAxCiAgc3RhY2sgPSBbcm9vdF0KICBkaXN0ID0gWzBdKihuKzEpCiAgZGlzdFtyb290XSA9IHBudFtyb290XQogIHdoaWxlIHN0YWNrOgogICAgeCA9IHN0YWNrLnBvcCgpCiAgICBmb3IgeSBpbiBncmFwaFt4XToKICAgICAgaWYgZGlzdFt5XSA9PSAwOgogICAgICAgIGRpc3RbeV0gPSBkaXN0W3hdK3BudFt5XQogICAgICAgIHN0YWNrLmFwcGVuZCh5KQogIGZhciA9IGRpc3QuaW5kZXgobWF4KGRpc3QpKQogIHJvb3QgPSBmYXIKICBzdGFjayA9IFtyb290XQogIGRpc3QgPSBbMF0qKG4rMSkKICBkaXN0W3Jvb3RdID0gcG50W3Jvb3RdCiAgd2hpbGUgc3RhY2s6CiAgICB4ID0gc3RhY2sucG9wKCkKICAgIGZvciB5IGluIGdyYXBoW3hdOgogICAgICBpZiBkaXN0W3ldID09IDA6CiAgICAgICAgZGlzdFt5XSA9IGRpc3RbeF0rcG50W3ldCiAgICAgICAgc3RhY2suYXBwZW5kKHkpCiAgcHJpbnQobWF4KGRpc3QpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
