import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwppbnB1dHIgPSBsYW1iZGE6IHN5cy5zdGRpbi5yZWFkbGluZSgpLnJzdHJpcCgnXG4nKQppbnB1dCA9IHN5cy5zdGRpbi5yZWFkbGluZQoKZm9yIF8gaW4gcmFuZ2UoaW50KGlucHV0KCkpKToKCW4sIG0gPSBsaXN0KG1hcChpbnQsIGlucHV0KCkuc3BsaXQoKSkpCglhZGogPSBbW10gZm9yIF8gaW4gcmFuZ2UobildCgoJZm9yIF8gaW4gcmFuZ2UobSk6CgkJYSwgYiA9IGxpc3QobWFwKGludCwgaW5wdXQoKS5zcGxpdCgpKSkKCQlhIC09IDEKCQliIC09IDEKCQlhZGpbYV0uYXBwZW5kKGIpCgoJTFAgPSBbMF0gKiBuCglyID0gW10KCglmb3IgaSBpbiByYW5nZShuKToKCQlpZiBMUFtpXSA8IDI6CgkJCWZvciBqIGluIGFkaltpXToKCQkJCUxQW2pdID0gbWF4KExQW2pdLCBMUFtpXSArIDEpCgkJZWxzZToKCQkJci5hcHBlbmQoc3RyKGkrMSkpCgoJcHJpbnQobGVuKHIpKQoJcHJpbnQoKnIpCgoJYXNzZXJ0IDcgKiBsZW4ocikgPD0gNCAqIG4=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
