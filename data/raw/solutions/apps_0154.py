import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4QXJlYShzZWxmLCBoOiBpbnQsIHc6IGludCwgaGM6IExpc3RbaW50XSwgdmM6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIGhjLCB2YyA9IFswXSArIHNvcnRlZChoYykgKyBbaF0sIFswXSArIHNvcnRlZCh2YykgKyBbd10KICAgICAgICByZXR1cm4gbWF4KGhjW2ldIC0gaGNbaS0xXSBmb3IgaSBpbiByYW5nZSgxLCBsZW4oaGMpKSkgKiBtYXgodmNbaV0gLSB2Y1tpLTFdIGZvciBpIGluIHJhbmdlKDEsIGxlbih2YykpKSAlIDEwMDAwMDAwMDc=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
