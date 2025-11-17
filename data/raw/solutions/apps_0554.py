import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBkZWNpbWFsIGltcG9ydCAqCmZvciBpIGluIHJhbmdlKGludChpbnB1dCgpKSk6CiB4LCB5ID0gaW5wdXQoKS5zcGxpdCgpCiB4ID0gaW50KHgpCiB5ID0gaW50KHkpCiBpZiAoeCA8IDEwMDApOgogIHExID0gc3RyKHggKiogeClbOnldCiBlbHNlOgogIHggPSBEZWNpbWFsKHgpCiAgcTEgPSBzdHIoaW50KDEwICoqKHgqKHgubG9nMTAoKSklMSArIHkgLSAxKSkpCiBxMiA9IHN0cihwb3coeCwgeCwgMTAgKiogeSkpLnpmaWxsKHkpIAogcHJpbnQocTEgKyAiICIgKyBxMik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
