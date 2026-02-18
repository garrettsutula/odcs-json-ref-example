# odcs-json-ref-example

**Idea**: Use python package `jsonref` and JSON Schema `$ref` syntax in ODCS files when needed to re-use elements of an ODCS spec across multiple disparate physical schemas.

This idea is applied to `shipment.ocds.yaml` to minimize the metadata in that model to **logical** metadata, `shipment-table.odcs.yaml` extends the various properties of the logical model with additional, technology-specific physical attributes to make a distinct physical schema. Lastly, `shipment-message.odcs.yaml` refers back to the shipment logical schema as the `payload` object for the message to make another distinct physical schema.

The `./3.1.0` folder uses `$ref` with the current spec version. Because JSON Schemas use references with [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901#section-4) syntax, accessing the array elements is awkward and brittle:

_shipment-message.odcs_ excerpt:
```yaml
apiVersion: "v3.1.0"
kind: "DataContract"
id: "valid_odcs"
name: "Shipment Message"
version: "2.0.0"
...
schema:
- name: "shipment event"
  physicalType: "message"
...
  properties:
  - name: id
...
  - name: payload
    $ref: shipment.odcs.yaml#/schema/0

```

The `./json-ref-friendly` folder uses `$ref` with a fictional spec version that is revised to use object keys as identifiers instead of an array. This is more similar to how `$ref`s are commonly used to point to objects in OpenAPI's [Components structure](https://swagger.io/docs/specification/v3_0/components/).

_shipment-message.odcs_ excerpt:
```yaml
apiVersion: "v4.0.0"
kind: "DataContract"
id: "draft_odcs"
name: "Shipment Message"
version: "2.0.0"
...
schema:
- name: "shipment event"
  physicalType: "message"
...
  properties:
  - name: id
...
  - name: payload
    $ref: shipment.odcs.yaml#/schema/shipment
```

Ref [this github issue](https://github.com/gazpachoking/jsonref/issues/68#issuecomment-2349981248) for some additional perspective on the use of `$ref` in JSON Schema.