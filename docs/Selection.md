# Class: Selection


_Template for machine-readable/executable expression for retrieving the data or information from an external resource._





URI: [odm:Selection](http://www.cdisc.org/ns/odm/v2.0/Selection)



```mermaid
 classDiagram
    class Selection
      Selection : Path
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [Path](Path.md) | 1..1 <br/> [text](text.md) | Provides the machine-executable instruction or template for it to obtain the ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Resource](Resource.md) | [SelectionRef](SelectionRef.md) | range | [Selection](Selection.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Selection](https://wiki.cdisc.org/display/ODM2/Selection)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Selection |
| native | odm:Selection |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Selection
description: Template for machine-readable/executable expression for retrieving the
  data or information from an external resource.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Selection
slots:
- Path
slot_usage:
  Path:
    name: Path
    description: Provides the machine-executable instruction or template for it to
      obtain the data or information from the resource. The value of the Path attribute
      can either be an absolute path, or a relative path starting from the information
      in the "Name" and "Attribute" attributes of the parent Resource element.
    comments:
    - 'Required

      range:text'
    domain_of:
    - Selection
    range: text
    required: true
class_uri: odm:Selection

```
</details>

### Induced

<details>
```yaml
name: Selection
description: Template for machine-readable/executable expression for retrieving the
  data or information from an external resource.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Selection
slot_usage:
  Path:
    name: Path
    description: Provides the machine-executable instruction or template for it to
      obtain the data or information from the resource. The value of the Path attribute
      can either be an absolute path, or a relative path starting from the information
      in the "Name" and "Attribute" attributes of the parent Resource element.
    comments:
    - 'Required

      range:text'
    domain_of:
    - Selection
    range: text
    required: true
attributes:
  Path:
    name: Path
    description: Provides the machine-executable instruction or template for it to
      obtain the data or information from the resource. The value of the Path attribute
      can either be an absolute path, or a relative path starting from the information
      in the "Name" and "Attribute" attributes of the parent Resource element.
    comments:
    - 'Required

      range:text'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: Path
    owner: Selection
    domain_of:
    - Selection
    range: text
    required: true
class_uri: odm:Selection

```
</details>