import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIG1haW4oKToKICAgIGZyb20gc3lzIGltcG9ydCBzdGRpbiwgc3Rkb3V0CiAgICBmb3IgXyBpbiByYW5nZShpbnQoc3RkaW4ucmVhZGxpbmUoKSkpOgogICAgICAgIG4gPSBpbnQoc3RkaW4ucmVhZGxpbmUoKSkKICAgICAgICBpbnAxID0gWy0xXSAqIChuICsgMSkKICAgICAgICBpbnAyID0gWy0xXSAqIChuICsgMSkKICAgICAgICBmb3IgaSwgYWkgaW4gZW51bWVyYXRlKG1hcChpbnQsIHN0ZGluLnJlYWRsaW5lKCkuc3BsaXQoKSkpOgogICAgICAgICAgICBpZiBpbnAxW2FpXSA8IDA6CiAgICAgICAgICAgICAgICBpbnAxW2FpXSA9IGkKICAgICAgICAgICAgaW5wMlthaV0gPSBpCiAgICAgICAgaW5wMSA9IHR1cGxlKChpbnAxaSBmb3IgaW5wMWkgaW4gaW5wMSBpZiBpbnAxaSA+PSAwKSkKICAgICAgICBpbnAyID0gdHVwbGUoKGlucDJpIGZvciBpbnAyaSBpbiBpbnAyIGlmIGlucDJpID49IDApKQogICAgICAgIG4gPSBsZW4oaW5wMSkKICAgICAgICBhbnMgPSAwCiAgICAgICAgY3VyID0gMAogICAgICAgIGZvciBpIGluIHJhbmdlKG4pOgogICAgICAgICAgICBpZiBpIGFuZCBpbnAxW2ldIDwgaW5wMltpIC0gMV06CiAgICAgICAgICAgICAgICBjdXIgPSAxCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBjdXIgKz0gMQogICAgICAgICAgICAgICAgYW5zID0gbWF4KGFucywgY3VyKQogICAgICAgIHN0ZG91dC53cml0ZShmJ3tuIC0gYW5zfVxuJykKCgptYWluKCk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
