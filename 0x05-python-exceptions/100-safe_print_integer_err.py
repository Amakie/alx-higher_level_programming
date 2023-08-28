def safe_print_integer_err(value):
    import sys
    try:
        print("{}".format(value))
        return True
    except ValueError:
        print("Exception:", file=sys.stderr)
        return False
