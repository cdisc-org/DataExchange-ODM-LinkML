# Class: AuditRecord


_An AuditRecord carries information pertaining to the creation, deletion, or modification of clinical data. This information includes who performed that action, and where, when, and why that action was performed.AuditRecord information describes a change to clinical data, but is not itself clinical data. The value of some clinical data can always be changed by a subsequent transaction, but history cannot be changed, only added to. Element NameAuditRecordParent ElementsReferenceData, ClinicalData, SubjectData, StudyEventData, ItemGroupData, ItemData, QueryElement XPath(s)/ODM/AdminData/Location/Query/AuditRecord/ODM/ReferenceData/AuditRecord/ODM/ClinicalData/AuditRecord/ODM/ClinicalData/Query/AuditRecord/ODM/ClinicalData/SubjectData/AuditRecord/ODM/ClinicalData/SubjectData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/Query/AuditRecordElement Textual ValueNoneUsage/Business RulesBusiness Rule(s):For the Archive use case, all AuditRecord information in the data collection system must be provided within the ODM ClinicalData.When the ODM FileType attribute is set to Transactional, every ClinicalData that has a TransactionType must also have an AuditRecord.Other Information:An AuditRecord applies to any descendant data element that allows a TransactionType and does not have an AuditRecord. Query elements must have their own AuditRecord(s).AuditRecord information describes a change to clinical data, but is not itself clinical data. The value of some clinical data can always be changed by a subsequent transaction, but history cannot be changed -- only added to.AttributesEditPoint, UsedMethod.Child Elements(UserRef, LocationRef, DateTimeStamp, ReasonForChange?, SourceID?)_





URI: [odm:AuditRecord](http://www.cdisc.org/ns/odm/v2.0/AuditRecord)



```mermaid
 classDiagram
    class AuditRecord
      AuditRecord : DateTimeStampRef
        
          AuditRecord --|> DateTimeStamp : DateTimeStampRef
        
      AuditRecord : EditPoint
        
          AuditRecord --|> EditPointType : EditPoint
        
      AuditRecord : LocationRefRef
        
          AuditRecord --|> LocationRef : LocationRefRef
        
      AuditRecord : ReasonForChangeRef
        
          AuditRecord --|> ReasonForChange : ReasonForChangeRef
        
      AuditRecord : SourceIDRef
        
          AuditRecord --|> SourceID : SourceIDRef
        
      AuditRecord : UsedMethod
        
          AuditRecord --|> YesOrNo : UsedMethod
        
      AuditRecord : UserRefRef
        
          AuditRecord --|> UserRef : UserRefRef
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [EditPoint](EditPoint.md) | 0..1 <br/> [EditPointType](EditPointType.md) | Identifies the phase of data processing in which update action occurred | direct |
| [UsedMethod](UsedMethod.md) | 0..1 <br/> [YesOrNo](YesOrNo.md) | Indicates that the action was made by the system rather than a data entry for... | direct |
| [UserRefRef](UserRefRef.md) | 0..1 <br/> [UserRef](UserRef.md) |  | direct |
| [LocationRefRef](LocationRefRef.md) | 0..1 <br/> [LocationRef](LocationRef.md) |  | direct |
| [DateTimeStampRef](DateTimeStampRef.md) | 0..1 <br/> [DateTimeStamp](DateTimeStamp.md) |  | direct |
| [ReasonForChangeRef](ReasonForChangeRef.md) | 0..1 <br/> [ReasonForChange](ReasonForChange.md) |  | direct |
| [SourceIDRef](SourceIDRef.md) | 0..1 <br/> [SourceID](SourceID.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ReferenceData](ReferenceData.md) | [AuditRecordRef](AuditRecordRef.md) | range | [AuditRecord](AuditRecord.md) |
| [ClinicalData](ClinicalData.md) | [AuditRecordRef](AuditRecordRef.md) | range | [AuditRecord](AuditRecord.md) |
| [SubjectData](SubjectData.md) | [AuditRecordRef](AuditRecordRef.md) | range | [AuditRecord](AuditRecord.md) |
| [StudyEventData](StudyEventData.md) | [AuditRecordRef](AuditRecordRef.md) | range | [AuditRecord](AuditRecord.md) |
| [ItemGroupData](ItemGroupData.md) | [AuditRecordRef](AuditRecordRef.md) | range | [AuditRecord](AuditRecord.md) |
| [ItemData](ItemData.md) | [AuditRecordRef](AuditRecordRef.md) | range | [AuditRecord](AuditRecord.md) |
| [Query](Query.md) | [AuditRecordRef](AuditRecordRef.md) | range | [AuditRecord](AuditRecord.md) |






## See Also

* [https://wiki.cdisc.org/display/ODM2/AuditRecord](https://wiki.cdisc.org/display/ODM2/AuditRecord)

## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | odm:AuditRecord |
| native | odm:AuditRecord |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AuditRecord
description: An AuditRecord carries information pertaining to the creation, deletion,
  or modification of clinical data. This information includes who performed that action,
  and where, when, and why that action was performed.AuditRecord information describes
  a change to clinical data, but is not itself clinical data. The value of some clinical
  data can always be changed by a subsequent transaction, but history cannot be changed,
  only added to. Element NameAuditRecordParent ElementsReferenceData, ClinicalData,
  SubjectData, StudyEventData, ItemGroupData, ItemData, QueryElement XPath(s)/ODM/AdminData/Location/Query/AuditRecord/ODM/ReferenceData/AuditRecord/ODM/ClinicalData/AuditRecord/ODM/ClinicalData/Query/AuditRecord/ODM/ClinicalData/SubjectData/AuditRecord/ODM/ClinicalData/SubjectData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/Query/AuditRecordElement
  Textual ValueNoneUsage/Business RulesBusiness Rule(s):For the Archive use case,
  all AuditRecord information in the data collection system must be provided within
  the ODM ClinicalData.When the ODM FileType attribute is set to Transactional, every
  ClinicalData that has a TransactionType must also have an AuditRecord.Other Information:An
  AuditRecord applies to any descendant data element that allows a TransactionType
  and does not have an AuditRecord. Query elements must have their own AuditRecord(s).AuditRecord
  information describes a change to clinical data, but is not itself clinical data.
  The value of some clinical data can always be changed by a subsequent transaction,
  but history cannot be changed -- only added to.AttributesEditPoint, UsedMethod.Child
  Elements(UserRef, LocationRef, DateTimeStamp, ReasonForChange?, SourceID?)
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/AuditRecord
slots:
- EditPoint
- UsedMethod
- UserRefRef
- LocationRefRef
- DateTimeStampRef
- ReasonForChangeRef
- SourceIDRef
slot_usage:
  EditPoint:
    name: EditPoint
    description: Identifies the phase of data processing in which update action occurred.
    comments:
    - Optional
    domain_of:
    - AuditRecord
    range: EditPointType
  UsedMethod:
    name: UsedMethod
    description: Indicates that the action was made by the system rather than a data
      entry form user action.
    comments:
    - Optional
    domain_of:
    - AuditRecord
    range: YesOrNo
  UserRefRef:
    name: UserRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: UserRef
    maximum_cardinality: 1
  LocationRefRef:
    name: LocationRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: LocationRef
    maximum_cardinality: 1
  DateTimeStampRef:
    name: DateTimeStampRef
    domain_of:
    - AuditRecord
    - Signature
    range: DateTimeStamp
    maximum_cardinality: 1
  ReasonForChangeRef:
    name: ReasonForChangeRef
    domain_of:
    - AuditRecord
    range: ReasonForChange
    maximum_cardinality: 1
  SourceIDRef:
    name: SourceIDRef
    domain_of:
    - AuditRecord
    range: SourceID
    maximum_cardinality: 1
class_uri: odm:AuditRecord

```
</details>

### Induced

<details>
```yaml
name: AuditRecord
description: An AuditRecord carries information pertaining to the creation, deletion,
  or modification of clinical data. This information includes who performed that action,
  and where, when, and why that action was performed.AuditRecord information describes
  a change to clinical data, but is not itself clinical data. The value of some clinical
  data can always be changed by a subsequent transaction, but history cannot be changed,
  only added to. Element NameAuditRecordParent ElementsReferenceData, ClinicalData,
  SubjectData, StudyEventData, ItemGroupData, ItemData, QueryElement XPath(s)/ODM/AdminData/Location/Query/AuditRecord/ODM/ReferenceData/AuditRecord/ODM/ClinicalData/AuditRecord/ODM/ClinicalData/Query/AuditRecord/ODM/ClinicalData/SubjectData/AuditRecord/ODM/ClinicalData/SubjectData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/Query/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/AuditRecord/ODM/ClinicalData/SubjectData/StudyEventData/ItemGroupData/ItemData/Query/AuditRecordElement
  Textual ValueNoneUsage/Business RulesBusiness Rule(s):For the Archive use case,
  all AuditRecord information in the data collection system must be provided within
  the ODM ClinicalData.When the ODM FileType attribute is set to Transactional, every
  ClinicalData that has a TransactionType must also have an AuditRecord.Other Information:An
  AuditRecord applies to any descendant data element that allows a TransactionType
  and does not have an AuditRecord. Query elements must have their own AuditRecord(s).AuditRecord
  information describes a change to clinical data, but is not itself clinical data.
  The value of some clinical data can always be changed by a subsequent transaction,
  but history cannot be changed -- only added to.AttributesEditPoint, UsedMethod.Child
  Elements(UserRef, LocationRef, DateTimeStamp, ReasonForChange?, SourceID?)
from_schema: http://www.cdisc.org/ns/odm/v2.0
see_also:
- https://wiki.cdisc.org/display/ODM2/AuditRecord
slot_usage:
  EditPoint:
    name: EditPoint
    description: Identifies the phase of data processing in which update action occurred.
    comments:
    - Optional
    domain_of:
    - AuditRecord
    range: EditPointType
  UsedMethod:
    name: UsedMethod
    description: Indicates that the action was made by the system rather than a data
      entry form user action.
    comments:
    - Optional
    domain_of:
    - AuditRecord
    range: YesOrNo
  UserRefRef:
    name: UserRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: UserRef
    maximum_cardinality: 1
  LocationRefRef:
    name: LocationRefRef
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: LocationRef
    maximum_cardinality: 1
  DateTimeStampRef:
    name: DateTimeStampRef
    domain_of:
    - AuditRecord
    - Signature
    range: DateTimeStamp
    maximum_cardinality: 1
  ReasonForChangeRef:
    name: ReasonForChangeRef
    domain_of:
    - AuditRecord
    range: ReasonForChange
    maximum_cardinality: 1
  SourceIDRef:
    name: SourceIDRef
    domain_of:
    - AuditRecord
    range: SourceID
    maximum_cardinality: 1
attributes:
  EditPoint:
    name: EditPoint
    description: Identifies the phase of data processing in which update action occurred.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: EditPoint
    owner: AuditRecord
    domain_of:
    - AuditRecord
    range: EditPointType
  UsedMethod:
    name: UsedMethod
    description: Indicates that the action was made by the system rather than a data
      entry form user action.
    comments:
    - Optional
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    alias: UsedMethod
    owner: AuditRecord
    domain_of:
    - AuditRecord
    range: YesOrNo
  UserRefRef:
    name: UserRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: UserRefRef
    owner: AuditRecord
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: UserRef
    maximum_cardinality: 1
  LocationRefRef:
    name: LocationRefRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: LocationRefRef
    owner: AuditRecord
    domain_of:
    - AdminData
    - AuditRecord
    - Signature
    range: LocationRef
    maximum_cardinality: 1
  DateTimeStampRef:
    name: DateTimeStampRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: DateTimeStampRef
    owner: AuditRecord
    domain_of:
    - AuditRecord
    - Signature
    range: DateTimeStamp
    maximum_cardinality: 1
  ReasonForChangeRef:
    name: ReasonForChangeRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: ReasonForChangeRef
    owner: AuditRecord
    domain_of:
    - AuditRecord
    range: ReasonForChange
    maximum_cardinality: 1
  SourceIDRef:
    name: SourceIDRef
    from_schema: http://www.cdisc.org/ns/odm/v2.0
    rank: 1000
    identifier: false
    alias: SourceIDRef
    owner: AuditRecord
    domain_of:
    - AuditRecord
    range: SourceID
    maximum_cardinality: 1
class_uri: odm:AuditRecord

```
</details>