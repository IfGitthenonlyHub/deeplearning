import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZGVmIHBlcihYKToKICAgIFM9c2V0KFgpCiAgICBpZiBub3QgbGVuKFgpPT1sZW4oUyk6CiAgICAgICAgcmV0dXJuIEZhbHNlCiAgICBmb3IgaSBpbiByYW5nZSgxLGxlbihYKSsxKToKICAgICAgICBpZiBpIG5vdCBpbiBTOiByZXR1cm4gRmFsc2UKICAgIHJldHVybiBUcnVlCmZvciB5IGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBuPWludChpbnB1dCgpKQogICAgTD1saXN0KG1hcChpbnQsaW5wdXQoKS5zcGxpdCgpKSkKICAgIG09bWF4KEwpCiAgICByPVtdCiAgICBpZiBuIT1tOgogICAgICAgIGlmIHBlcihMWzptXSkgYW5kIHBlcihMW206XSk6CiAgICAgICAgICAgIHIuYXBwZW5kKChtLG4tbSkpCiAgICAgICAgaWYgcGVyKExbLW06XSkgYW5kIHBlcihMWzotbV0pOgogICAgICAgICAgICByLmFwcGVuZCgobi1tLG0pKQogICAgcj1saXN0KHNldChyKSkKICAgIHByaW50KGxlbihyKSkKICAgIGZvciBhLGIgaW4gcjoKICAgICAgICBwcmludChhLGIp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
