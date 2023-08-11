# Class: Image



URI: [odm:Image](http://www.cdisc.org/ns/odm/v2.0/Image)



```mermaid
 classDiagram
    class Image
      Image : href
        
      Image : ImageFileName
        
      Image : MimeType
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [ImageFileName](ImageFileName.md) | 0..1 <br/> [FileName](FileName.md) |  | direct |
| [href](href.md) | 0..1 <br/> [Text](Text.md) | URL that can be used to identify the location of a document or dataset file r... | direct |
| [MimeType](MimeType.md) | 0..1 <br/> [Text](Text.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [User](User.md) | [ImageRef](ImageRef.md) | range | [Image](Image.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/Image](https://wiki.cdisc.org/display/ODM2/Image)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:Image |
| native | odm:Image |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Image
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Image
slots:
- ImageFileName
- href
- MimeType
slot_usage:
  ImageFileName:
    name: ImageFileName
    domain_of:
    - Image
    range: fileName
  href:
    name: href
    domain_of:
    - leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: text
  MimeType:
    name: MimeType
    domain_of:
    - Image
    range: text
class_uri: odm:Image

```
</details>

### Induced

<details>
```yaml
name: Image
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/Image
slot_usage:
  ImageFileName:
    name: ImageFileName
    domain_of:
    - Image
    range: fileName
  href:
    name: href
    domain_of:
    - leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: text
  MimeType:
    name: MimeType
    domain_of:
    - Image
    range: text
attributes:
  ImageFileName:
    name: ImageFileName
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: ImageFileName
    owner: Image
    domain_of:
    - Image
    range: fileName
  href:
    name: href
    description: URL that can be used to identify the location of a document or dataset
      file relative to the folder containing the ODM file.
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: href
    owner: Image
    domain_of:
    - leaf
    - Include
    - ExternalCodeLib
    - Image
    - Coding
    range: text
  MimeType:
    name: MimeType
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: MimeType
    owner: Image
    domain_of:
    - Image
    range: text
class_uri: odm:Image

```
</details>