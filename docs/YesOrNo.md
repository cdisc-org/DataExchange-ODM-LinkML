# Enum: YesOrNo




_Enumeration used in mandatory, repeating, isReferenceData, usedMethod_



URI: [YesOrNo](YesOrNo)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Yes | None |  |
| No | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [isReferenceData](isReferenceData.md) | Specifies whether this ItemGroupDef is used for non-subject data. |
| [mandatory](mandatory.md) | Indicator of whether this StudyEventGroup must appear in the study clinical d... |
| [usedMethod](usedMethod.md) | Indicates that the action was made by the system rather than a data entry for... |
| [mandatory](mandatory.md) | Indicator of whether this StudyEventGroup must appear in the study clinical d... |
| [mandatory](mandatory.md) | The Mandatory flag indicates that the clinical data for the containing MetaDa... |
| [repeating](repeating.md) | The Repeating flag indicates when this type of study event can occur repeated... |
| [mandatory](mandatory.md) | The Mandatory flag indicates that the clinical data for an instance of the co... |
| [isReferenceData](isReferenceData.md) | Specifies whether this ItemGroupDef is used for non-subject data. |
| [mandatory](mandatory.md) | Indicator of whether this ItemGroup must appear in the study clinical data fo... |
| [usedMethod](usedMethod.md) | Indicates that the action was made by the system rather than a data entry for... |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: YesOrNo
description: Enumeration used in mandatory, repeating, isReferenceData, usedMethod
from_schema: http://www.cdisc.org/ns/odm/v2.0
rank: 1000
permissible_values:
  'Yes':
    text: 'Yes'
    is_a: YesOrNo
  'No':
    text: 'No'
    is_a: YesOrNo

```
</details>
