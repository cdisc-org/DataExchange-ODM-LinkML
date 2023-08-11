# Class: WhereClauseRef



URI: [odm:WhereClauseRef](http://www.cdisc.org/ns/odm/v2.0/WhereClauseRef)



```mermaid
 classDiagram
    class WhereClauseRef
      WhereClauseRef : WhereClauseOID
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [WhereClauseOID](WhereClauseOID.md) | 1..1 <br/> [Oidref](Oidref.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ItemRef](ItemRef.md) | [WhereClauseRefRef](WhereClauseRefRef.md) | range | [WhereClauseRef](WhereClauseRef.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/WhereClauseRef](https://wiki.cdisc.org/display/ODM2/WhereClauseRef)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:WhereClauseRef |
| native | odm:WhereClauseRef |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WhereClauseRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/WhereClauseRef
slots:
- WhereClauseOID
slot_usage:
  WhereClauseOID:
    name: WhereClauseOID
    domain_of:
    - WhereClauseRef
    range: oidref
    required: true
class_uri: odm:WhereClauseRef

```
</details>

### Induced

<details>
```yaml
name: WhereClauseRef
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/WhereClauseRef
slot_usage:
  WhereClauseOID:
    name: WhereClauseOID
    domain_of:
    - WhereClauseRef
    range: oidref
    required: true
attributes:
  WhereClauseOID:
    name: WhereClauseOID
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: WhereClauseOID
    owner: WhereClauseRef
    domain_of:
    - WhereClauseRef
    range: oidref
    required: true
class_uri: odm:WhereClauseRef

```
</details>