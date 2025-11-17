import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBiaXNlY3QgaW1wb3J0IGJpc2VjdF9sZWZ0IGFzIGJsCmltcG9ydCBzeXMKc3lzLnNldHJlY3Vyc2lvbmxpbWl0KDEwKio2KQpuPWludChpbnB1dCgpKQphPWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQp0PVtbXWZvciBpIGluIHJhbmdlKG4pXQpmb3IgaSBpbiByYW5nZShuLTEpOgogICAgdSx2PWxpc3QobWFwKGludCxpbnB1dCgpLnNwbGl0KCkpKQogICAgdFt1LTFdLmFwcGVuZCh2LTEpCiAgICB0W3YtMV0uYXBwZW5kKHUtMSkKYj1bMF0qbgpkcD1bZmxvYXQoImluZiIpXSpuCmRlZiBmKGMsZCk6CiAgICBoPWJsKGRwLGFbY10pCiAgICBnPWRwW2hdCiAgICBkcFtoXT1taW4oZHBbaF0sYVtjXSkKICAgIGJbY109YmwoZHAsZmxvYXQoIklORiIpKQogICAgZm9yIGkgaW4gdFtjXToKICAgICAgICBpZiBpIT1kOmYoaSxjKQogICAgZHBbaF09ZwpmKDAsLTEpCmZvciBpIGluIGI6CiAgICBwcmludChpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
