# Class: RangeCheck

_A RangeCheck defines a constraint on the value of the enclosing item. It represents an expression that evaluates to True when the ItemData value is valid or False when the ItemData value is invalid. The expression is specified using either Comparator and CheckValue or using FormalExpressions._




URI: [odm:RangeCheck](http://www.cdisc.org/ns/odm/v2.0/RangeCheck)


```mermaid
erDiagram
RangeCheck {
    Comparator comparator  
    SoftOrHard softHard  
}
CheckValue {
    valueType content  
}
FormalExpression {
    text context  
}
ExternalCodeLib {
    nameType library  
    nameType method  
    text version  
    text ref  
    uriorcurie href  
}
Code {
    text content  
}
MethodSignature {

}
ReturnValue {
    nameType name  
    DataType dataType  
    text definition  
    positiveInteger orderNumber  
}
Parameter {
    nameType name  
    DataType dataType  
    text definition  
    positiveInteger orderNumber  
}
ErrorMessage {

}
TranslatedText {
    languageType language  
    text type  
    contentType content  
}
ItemDef {
    oid OID  
    nameType name  
    DataType dataType  
    positiveInteger length  
    text displayFormat  
    text variableSet  
}
Alias {
    text context  
    text name  
}
Coding {
    text code  
    uriorcurie system  
    text systemName  
    text systemVersion  
    text label  
    uriorcurie href  
    uriorcurie ref  
    text commentOID  
}
ValueListRef {

}
CodeListRef {

}
CDISCNotes {

}
ImplementationNotes {

}
CRFCompletionInstructions {

}
Prompt {

}
Question {

}
Definition {

}
Description {

}
CommentDef {
    oid OID  
}

RangeCheck ||--|o ItemDef : "itemOID"
RangeCheck ||--|o ErrorMessage : "errorMessage"
RangeCheck ||--|o MethodSignature : "methodSignature"
RangeCheck ||--}o FormalExpression : "formalExpression"
RangeCheck ||--}o CheckValue : "checkValue"
FormalExpression ||--|o Code : "code"
FormalExpression ||--|o ExternalCodeLib : "externalCodeLib"
MethodSignature ||--}o Parameter : "parameter"
MethodSignature ||--}o ReturnValue : "returnValue"
ErrorMessage ||--}o TranslatedText : "translatedText"
ItemDef ||--|o CommentDef : "commentOID"
ItemDef ||--|o Description : "description"
ItemDef ||--|o Definition : "definition"
ItemDef ||--|o Question : "question"
ItemDef ||--|o Prompt : "prompt"
ItemDef ||--|o CRFCompletionInstructions : "cRFCompletionInstructions"
ItemDef ||--|o ImplementationNotes : "implementationNotes"
ItemDef ||--|o CDISCNotes : "cDISCNotes"
ItemDef ||--}o RangeCheck : "rangeCheck"
ItemDef ||--|o CodeListRef : "codeListRef"
ItemDef ||--|o ValueListRef : "valueListRef"
ItemDef ||--}o Coding : "coding"
ItemDef ||--}o Alias : "alias"
ValueListRef ||--|| ValueListDef : "valueListOID"
CodeListRef ||--|| CodeList : "codeListOID"
CDISCNotes ||--}o TranslatedText : "translatedText"
ImplementationNotes ||--}o TranslatedText : "translatedText"
CRFCompletionInstructions ||--}o TranslatedText : "translatedText"
Prompt ||--}o TranslatedText : "translatedText"
Question ||--}o TranslatedText : "translatedText"
Definition ||--}o TranslatedText : "translatedText"
Description ||--}o TranslatedText : "translatedText"
CommentDef ||--|o Description : "description"
CommentDef ||--}o DocumentRef : "documentRef"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality* and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [comparator](comparator.md) | 0..1 <br/> [Comparator](Comparator.md) | Comparison operator used to compare the item and value(s). | direct |
| [softHard](softHard.md) | 0..1 <br/> [SoftOrHard](SoftOrHard.md) | Type of range check. Soft indicates that a warning occurs when the RangeCheck... | direct |
| [itemOID](itemOID.md) | 0..1 <br/> [ItemDef](ItemDef.md) | Identifies a variable to compare against. | direct |
| [errorMessage](errorMessage.md) | 0..1 <br/> [ErrorMessage](ErrorMessage.md) | ErrorMessage reference: Error message provided to user when the range check f... | direct |
| [methodSignature](methodSignature.md) | 0..1 <br/> [MethodSignature](MethodSignature.md) | MethodSignature reference: A MethodSignature defines the parameters and retur... | direct |
| [formalExpression](formalExpression.md) | 0..* <br/> [FormalExpression](FormalExpression.md) | FormalExpression reference: A FormalExpression used within a ConditionDef or ... | direct |
| [checkValue](checkValue.md) | 0..* <br/> [CheckValue](CheckValue.md) | CheckValue reference: A comparison value used in a range check. | direct |

_* See [LinkML documentation](https://linkml.io/linkml/schemas/slots.html#slot-cardinality) for cardinality definitions._




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [WhereClauseDef](WhereClauseDef.md) | [rangeCheck](rangeCheck.md) | range | [RangeCheck](RangeCheck.md) |
| [ItemDef](ItemDef.md) | [rangeCheck](rangeCheck.md) | range | [RangeCheck](RangeCheck.md) |






## See Also

* [https://wiki.cdisc.org/display/PUB/RangeCheck](https://wiki.cdisc.org/display/PUB/RangeCheck)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:RangeCheck |
| native | odm:RangeCheck |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RangeCheck
description: A RangeCheck defines a constraint on the value of the enclosing item.
  It represents an expression that evaluates to True when the ItemData value is valid
  or False when the ItemData value is invalid. The expression is specified using either
  Comparator and CheckValue or using FormalExpressions.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/RangeCheck
rank: 1000
slots:
- comparator
- softHard
- itemOID
- errorMessage
- methodSignature
- formalExpression
- checkValue
slot_usage:
  comparator:
    name: comparator
    description: Comparison operator used to compare the item and value(s).
    comments:
    - 'Conditional

      enum values: (LT | LE | GT | GE | EQ | NE | IN | NOTIN)'
    domain_of:
    - RangeCheck
    range: Comparator
  softHard:
    name: softHard
    description: Type of range check. Soft indicates that a warning occurs when the
      RangeCheck fails. Hard indicates that an error occurs when the RangeCheck fails.
    comments:
    - 'Conditional

      enum values: (Soft | Hard)'
    domain_of:
    - RangeCheck
    range: SoftOrHard
  itemOID:
    name: itemOID
    description: Identifies a variable to compare against.
    comments:
    - 'Conditional

      range: oidref'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
  errorMessage:
    name: errorMessage
    domain_of:
    - RangeCheck
    range: ErrorMessage
    maximum_cardinality: 1
  methodSignature:
    name: methodSignature
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    range: MethodSignature
    maximum_cardinality: 1
  formalExpression:
    name: formalExpression
    multivalued: true
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    - StudyEndPoint
    - StudyTargetPopulation
    range: FormalExpression
    inlined: true
    inlined_as_list: true
  checkValue:
    name: checkValue
    multivalued: true
    domain_of:
    - RangeCheck
    range: CheckValue
    inlined: true
    inlined_as_list: true
class_uri: odm:RangeCheck

```
</details>

### Induced

<details>
```yaml
name: RangeCheck
description: A RangeCheck defines a constraint on the value of the enclosing item.
  It represents an expression that evaluates to True when the ItemData value is valid
  or False when the ItemData value is invalid. The expression is specified using either
  Comparator and CheckValue or using FormalExpressions.
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/PUB/RangeCheck
rank: 1000
slot_usage:
  comparator:
    name: comparator
    description: Comparison operator used to compare the item and value(s).
    comments:
    - 'Conditional

      enum values: (LT | LE | GT | GE | EQ | NE | IN | NOTIN)'
    domain_of:
    - RangeCheck
    range: Comparator
  softHard:
    name: softHard
    description: Type of range check. Soft indicates that a warning occurs when the
      RangeCheck fails. Hard indicates that an error occurs when the RangeCheck fails.
    comments:
    - 'Conditional

      enum values: (Soft | Hard)'
    domain_of:
    - RangeCheck
    range: SoftOrHard
  itemOID:
    name: itemOID
    description: Identifies a variable to compare against.
    comments:
    - 'Conditional

      range: oidref'
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
  errorMessage:
    name: errorMessage
    domain_of:
    - RangeCheck
    range: ErrorMessage
    maximum_cardinality: 1
  methodSignature:
    name: methodSignature
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    range: MethodSignature
    maximum_cardinality: 1
  formalExpression:
    name: formalExpression
    multivalued: true
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    - StudyEndPoint
    - StudyTargetPopulation
    range: FormalExpression
    inlined: true
    inlined_as_list: true
  checkValue:
    name: checkValue
    multivalued: true
    domain_of:
    - RangeCheck
    range: CheckValue
    inlined: true
    inlined_as_list: true
attributes:
  comparator:
    name: comparator
    description: Comparison operator used to compare the item and value(s).
    comments:
    - 'Conditional

      enum values: (LT | LE | GT | GE | EQ | NE | IN | NOTIN)'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: comparator
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: Comparator
  softHard:
    name: softHard
    description: Type of range check. Soft indicates that a warning occurs when the
      RangeCheck fails. Hard indicates that an error occurs when the RangeCheck fails.
    comments:
    - 'Conditional

      enum values: (Soft | Hard)'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: softHard
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: SoftOrHard
  itemOID:
    name: itemOID
    description: Identifies a variable to compare against.
    comments:
    - 'Conditional

      range: oidref'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: itemOID
    owner: RangeCheck
    domain_of:
    - ItemRef
    - SourceItem
    - RangeCheck
    - ItemData
    - KeySet
    range: ItemDef
  errorMessage:
    name: errorMessage
    description: 'ErrorMessage reference: Error message provided to user when the
      range check fails.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: errorMessage
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: ErrorMessage
    maximum_cardinality: 1
  methodSignature:
    name: methodSignature
    description: 'MethodSignature reference: A MethodSignature defines the parameters
      and return values for a method. The MethodSignature improves traceability while
      enhancing the ability for automation engines to execute a MethodDef''s FormalExpression.
      Most Methods use one or more input parameters and return one or more values.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: methodSignature
    owner: RangeCheck
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    range: MethodSignature
    maximum_cardinality: 1
  formalExpression:
    name: formalExpression
    description: 'FormalExpression reference: A FormalExpression used within a ConditionDef
      or a RangeCheck must evaluate to True or False. A FormalExpression referenced
      within a MethodDef having Type Imputation, Computation, or Transpose must evaluate
      to the correct DataType for an Item that may be imputed or computed using the
      Method. A FormalExpression gets parameter and return value definitions from
      the MethodSignature element. The data types in the MethodSignature parameters
      and return values must match the corresponding data types in the FormalExpression.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: formalExpression
    owner: RangeCheck
    domain_of:
    - RangeCheck
    - MethodDef
    - ConditionDef
    - StudyEndPoint
    - StudyTargetPopulation
    range: FormalExpression
    inlined: true
    inlined_as_list: true
  checkValue:
    name: checkValue
    description: 'CheckValue reference: A comparison value used in a range check.'
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    multivalued: true
    alias: checkValue
    owner: RangeCheck
    domain_of:
    - RangeCheck
    range: CheckValue
    inlined: true
    inlined_as_list: true
class_uri: odm:RangeCheck

```
</details>