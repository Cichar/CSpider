# -*- utf-8 -*-


class BaseError(Exception):
    """ Base Class For Exceptions In This CSpider """

    def __init__(self, err, *args, **kwargs):
        super(BaseError, self).__init__(self, *args)
        self.err = err

    def __str__(self, *args, **kwargs):
        return '< {0} > : {1}'.format(self.__class__.__name__, self.err)


class ParseUrlError(BaseError):
    """ Parse Url Exception """
    pass
