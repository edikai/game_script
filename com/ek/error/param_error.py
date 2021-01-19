class ParamError(RuntimeError):

    """
    自定义参数异常
    """

    def __init__(self, args):
        self.args = args
