# Class: CodeListRef



URI: [odm:CodeListRef](http://www.cdisc.org/ns/odm/v2.0/CodeListRef)



```mermaid
 classDiagram
    class CodeListRef
      CodeListRef : CodeListOID
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [CodeListOID](CodeListOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemDef](ItemDef.md) | [CodeListRefRef](CodeListRefRef.md) | range | [CodeListRef](CodeListRef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/CodeListRef](https://wiki.cdisc.org/display/ODM2/CodeListRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:CodeListRef |
| native | odm:CodeListRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CodeListRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/CodeListRef
slots:
- CodeListOID
slot_usage:
  CodeListOID:
    name: CodeListOID
    domain_of:
    - CodeListRef
    - FlagValue
    - FlagType
    range: oidref
    required: true
class_uri: odm:CodeListRef

```
</details>

### Induced

<details>
```yaml
name: CodeListRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/CodeListRef
slot_usage:
  CodeListOID:
    name: CodeListOID
    domain_of:
    - CodeListRef
    - FlagValue
    - FlagType
    range: oidref
    required: true
attributes:
  CodeListOID:
    name: CodeListOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: CodeListOID
    owner: CodeListRef
    domain_of:
    - CodeListRef
    - FlagValue
    - FlagType
    range: oidref
    required: true
class_uri: odm:CodeListRef

```
</details>