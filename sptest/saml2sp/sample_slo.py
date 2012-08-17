encoded = """jVJdq9wgEP0rwffdqDExkd1AYSks3Ja2W/rQl2Wi471CYmw05f785qOF2z4sRRA5M+fMnBlPEYY+qKfxeZzTF/wxY0zZ69D7qLbImcyTVyNEF5WHAaNKWt3efXhS/EhVmMY06rEnbyiPGRAjTsmNnmTXy5ncq0Y0rO60qGtBJe8MM6yktDQgJZVMCmYLUxQVNCT7hlNcmGeyCC30GGe8+pjApwWijB9ofWDyK6eqlErU30l2Wdw4D2ljvaQUVJ4zLo90OSyPbgg9rj3n68VzZ0J+c/65x30eN5x+Oo3H8BJIe1pz1FZ1ah9pDaOZ+42U79ohHzCBgQQbaNDC3KdDDKf8reZe4OMysuslu31aH59n6J11OD3u/v8rkuz9OA2QHi9pRZw52C1VpQl8dOgTae9VV1pbcKkNlqWkaG1ldMd4I0CIwhjQ2GGBjNPf3nY7u7egbhjXDV69wdf2TmthtLamBkqhFsCWXXPaWAHWcs4BNatMoRuodrF/+H/Av/5u+ws="""
from codex import decode_base64_and_inflate

assertion = decode_base64_and_inflate(encoded)
print assertion

GOT = (
'<samlp:LogoutRequest '
    'xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" '
    'xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" '
    'ID="_694918bc4884072bd1d15005da77071741f3d336a9" '
    'Version="2.0" '
    'IssueInstant="2012-08-17T20:57:48Z" '
    'Destination="http://127.0.0.1/simplesaml/saml2/idp/SingleLogoutService.php"'
    '>'
    '<saml:Issuer>http://127.0.0.1/simplesaml/module.php/saml/sp/metadata.php/default-sp</saml:Issuer>'
    '<saml:NameID '
        'SPNameQualifier="http://127.0.0.1/simplesaml/module.php/saml/sp/metadata.php/default-sp"'  
        'Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient"'
     '>_6b5ff327cde5570eff6dcb1294a443ddacebe3e120</saml:NameID>'
'<samlp:SessionIndex>_084dccfd8a00a84a11f3209f4aff222aec16d3c9a6</samlp:SessionIndex>'
'</samlp:LogoutRequest>'
)

#TODO: Finish XML template for SLO Assertion.
LOGOUT_REQUEST = (
    '<?xml version="1.0" encoding="UTF-8"?>'
        '<samlp:LogoutRequest '
                'Destination="${DESTINATION}" ' # Optional
                'ID="${LOGOUT_REQUEST_ID}" '
                'IssueInstant="${ISSUE_INSTANT}" '
                'ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" '
                'Version="2.0" '
                'xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol">'
            '<saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">${ISSUER}</saml:Issuer>'
            '<saml:NameID Format="${SUBJECT_FORMAT}" SPNameQualifier="${SP_NAME_QUALIFIER}">'
            '${SUBJECT}'
            '</saml:NameID>'
            '${LOGOUT_REQUEST_SIGNATURE}'
    '</samlp:LogoutRequest>'
)
