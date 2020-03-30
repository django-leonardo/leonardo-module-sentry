import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

try:
    from local_settings import SENTRY_DSN
except ImportError:
    SENTRY_DSN = 'http://public:secret@example.com/1'

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()]
)
