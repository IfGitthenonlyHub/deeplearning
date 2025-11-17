import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwpzeXMuc2V0cmVjdXJzaW9ubGltaXQoMTAqKjYpCmY9bGFtYmRhOm1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKQpuLG09ZigpCmc9W1tdIGZvciBfIGluIHJhbmdlKG4pXQpmb3IgXyBpbiByYW5nZShtKToKICB1LHYsbD1mKCkKICBnW3UtMV0rPVsodi0xLGwpXQogIGdbdi0xXSs9Wyh1LTEsbCldCmE9WzBdKm4KZGVmIGRmcyh2LHA9LTEsbD0xKToKICBhW3ZdPWwKICBmb3IgYyxtIGluIGdbdl06CiAgICBpZiBjPT1wIG9yIGFbY106IGNvbnRpbnVlCiAgICBpZiBsPT1tOiBtPTErKG09PTEpCiAgICBkZnMoYyx2LG0pCmRmcygwKQpwcmludCgqYSxzZXA9J1xuJyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
