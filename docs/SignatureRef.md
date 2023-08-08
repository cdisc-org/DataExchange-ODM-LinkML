# Class: SignatureRef



URI: [odm:SignatureRef](http://www.cdisc.org/ns/odm/v2.0/SignatureRef)



```mermaid
 classDiagram
    class SignatureRef
      SignatureRef : SignatureOID
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [SignatureOID](SignatureOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Signature](Signature.md) | [SignatureRefRef](SignatureRefRef.md) | range | [SignatureRef](SignatureRef.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:SignatureRef |
| native | odm:SignatureRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SignatureRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
slots:
- SignatureOID
slot_usage:
  SignatureOID:
    name: SignatureOID
    domain_of:
    - SignatureRef
    range: oidref
    required: true
class_uri: odm:SignatureRef

```
</details>

### Induced

<details>
```yaml
name: SignatureRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
slot_usage:
  SignatureOID:
    name: SignatureOID
    domain_of:
    - SignatureRef
    range: oidref
    required: true
attributes:
  SignatureOID:
    name: SignatureOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: SignatureOID
    owner: SignatureRef
    domain_of:
    - SignatureRef
    range: oidref
    required: true
class_uri: odm:SignatureRef

```
</details>