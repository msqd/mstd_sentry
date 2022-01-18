import sentry_sdk


def disable_sentry_transaction_log():
    """
    Sentry transactions are the APM-side of sentry, and some recurring tasks will saturate our event quota without real
    value. For example, background jobs have no real value of being logged in sentry transactions and a lot ot them
    are run on a regular basis.
    """

    with sentry_sdk.configure_scope() as scope:
        if scope.transaction:
            scope.transaction.sampled = False
