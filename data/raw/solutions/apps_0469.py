import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgdmFsaWRhdGVCaW5hcnlUcmVlTm9kZXMoc2VsZiwgbiwgbGVmdCwgcmlnaHQpOgogICAgICAgIHJvb3RzPXsqcmFuZ2Uobil9CiAgICAgICAgZm9yIHggaW4gbGVmdCtyaWdodDoKICAgICAgICAgICAgaWYgeD09LTE6CiAgICAgICAgICAgICAgICBjb250aW51ZQogICAgICAgICAgICBpZiB4IG5vdCBpbiByb290czoKICAgICAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgICAgICByb290cy5kaXNjYXJkKHgpCiAgICAgICAgaWYgbGVuKHJvb3RzKSE9MToKICAgICAgICAgICAgcmV0dXJuIEZhbHNlCiAgICAgICAgaz0wCiAgICAgICAgc3RrPVtyb290cy5wb3AoKV0KICAgICAgICB3aGlsZSBzdGs6CiAgICAgICAgICAgIG5vZGU9c3RrLnBvcCgpCiAgICAgICAgICAgIGsrPTEKICAgICAgICAgICAgbCxyPWxlZnRbbm9kZV0scmlnaHRbbm9kZV0KICAgICAgICAgICAgaWYgbCE9LTE6CiAgICAgICAgICAgICAgICBzdGsuYXBwZW5kKGwpCiAgICAgICAgICAgIGlmIHIhPS0xOgogICAgICAgICAgICAgICAgc3RrLmFwcGVuZChyKQogICAgICAgIHJldHVybiBrPT1u").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
