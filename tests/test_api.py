import schemathesis

schemathesis.experimental.OPEN_API_3_1.enable()
schema = schemathesis.from_uri("http://127.0.0.1:8000/openapi.json")


@schema.parametrize()
def test_api(case):
    case.call_and_validate()
