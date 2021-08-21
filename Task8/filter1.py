valid_output = []
def filtersx(x):
    for i in x:
        if len(i) == 0:
            pass
        else:
            valid_output.append(i)
    return valid_output
