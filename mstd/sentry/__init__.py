from functools import wraps

import sentry_sdk

def _disable_sentry_transaction_log():
    """
    Sentry transactions are the APM-side of sentry, and some recurring tasks will saturate our event quota without real
    value. For example, background jobs have no real value of being logged in sentry transactions and a lot ot them
    are run on a regular basis.

    This is the actual implementation, while you most likely will use `disable_transaction_log()` which works both as a
    one time call AND a decorator.

    """

    with sentry_sdk.configure_scope() as scope:
        if scope.transaction:
            scope.transaction.sampled = False

def disable_sentry_transaction_log(f=None):
    """
    Disable sending transactions logs to sentry, either as a decorator or one time call function.

    :param f: function to decorate or None to just call it.
    :return: decorated function or None
    """

    # a function is passed to be decorated
    if f is not None:
        @wraps(f)
        def _wrapped(*args, **kwargs):
            _disable_sentry_transaction_log()
            return f(*args, **kwargs)
        return _wrapped

    # no decoration, just call it
    _disable_sentry_transaction_log()


