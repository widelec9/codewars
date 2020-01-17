class UnexpectedTypeException(BaseException):
    pass


def expected_type(return_types):
    def expected_type_generator(old_fun):
        def new_fun(sth):
            ret = old_fun(sth)
            if not any([isinstance(ret, x) for x in return_types]):
                raise UnexpectedTypeException(return_types)
            return ret
        return new_fun
    return expected_type_generator
