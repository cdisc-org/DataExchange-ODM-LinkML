# Enum: YesOrNo



URI: [YesOrNo](YesOrNo)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Yes | None |  |
| No | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [IsReferenceData](IsReferenceData.md) | Specifies whether this ItemGroupDef is used for non-subject data |
| [UsedMethod](UsedMethod.md) | Indicates that the action was made by the system rather than a data entry for... |
| [Mandatory](Mandatory.md) | Indicator of whether this StudyEventGroup must appear in the study clinical d... |
| [Mandatory](Mandatory.md) | Indicator of whether this StudyEventGroup must appear in the study clinical d... |
| [Mandatory](Mandatory.md) | The Mandatory flag indicates that the clinical data for the containing MetaDa... |
| [Repeating](Repeating.md) | The Repeating flag indicates when this type of study event can occur repeated... |
| [Mandatory](Mandatory.md) | The Mandatory flag indicates that the clinical data for an instance of the co... |
| [IsReferenceData](IsReferenceData.md) | Specifies whether this ItemGroupDef is used for non-subject data |
| [Mandatory](Mandatory.md) | Indicator of whether this ItemGroup must appear in the study clinical data fo... |
| [UsedMethod](UsedMethod.md) | Indicates that the action was made by the system rather than a data entry for... |






## Identifier and Mapping Information







### Schema Source


* from schema: http://www.cdisc.org/ns/odm/v2.0




## LinkML Source

<details>
```yaml
name: YesOrNo
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
