
def test_get_certificates(app):
    from lemur.plugins.base import plugins
    p = plugins.get('acme-issuer')
    p.create_certificate('', {})