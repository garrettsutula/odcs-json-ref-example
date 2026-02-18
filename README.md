# odcs-json-ref-example

Use `jsonref` and `$ref` in ODCS files to dereference reusable schemas & properties into multiple disparate physical schemas.

The `./3.1.0` folder uses `$ref` with the current spec version. Because JSON Schemas use references with [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901#section-4) syntax, accessing the array elements is awkward:

_shipment-message.odcs_ excerpt:
```yaml
  - name: payload
    allOf:
      - $ref: shipment.odcs.yaml#/schema/0
```

The `./json-ref-friendly` folder uses `$ref` with a fictional spec version that is revised to use object keys as identifiers instead of an array. This is more similar to how `$refs` are commonly used in OpenAPI's [Components structure](https://swagger.io/docs/specification/v3_0/components/).

_shipment-message.odcs_ excerpt:
```yaml
  - allOf:
      - $ref: shipment.odcs.yaml#/schema/shipment
    name: payload
```