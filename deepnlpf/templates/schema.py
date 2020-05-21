import sys

from jsonschema import validate

SCHEMA_OUPUT_PLUGIN = {
    "type": "array",
    "properties": {
        "_id": {"type": "number"},
        "text": {"type": "string"},
        "annotation": {"type": "array"},
    },
}

def validate_annotation(doc_annotated):
    result = validate(instance=doc_annotated, schema=SCHEMA_OUPUT_PLUGIN)
    if result != None:
        sys.exit(0)