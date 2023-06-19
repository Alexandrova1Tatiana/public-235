def flatten(*args):
    return helper(args, [])
def helper(args, res):
    for i in args:
        if isinstance(i, list):
            helper(i, res)
        else:
            res.append(i)
    return res