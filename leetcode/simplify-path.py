
def simplifyPath(path="/home/user/Documents/../Pictures"):
        simplify = []
        paths = list(reversed(path.split('/')))
        while paths:
            c = paths.pop()
            if c and (c != "." and c != ".."): simplify.append(c)
            if c == ".." and simplify: simplify.pop()
        return "/"+"/".join(simplify)

simplifyPath()