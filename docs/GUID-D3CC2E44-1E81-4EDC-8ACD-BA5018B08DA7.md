# PORT\_GroupWrite Function

**Parent topic:**[I/O Pin Controller \(PORT\)](GUID-7F443A35-9F1B-49DE-B591-83F974FA576B.md)

## C

```c
void PORT_GroupWrite(PORT_GROUP group, uint32_t mask, uint32_t value);
```

## Summary

Write value on the masked pins of the selected port group.

## Description

This function writes the value contained in the value parameter to the<br />port group. Port group pins which are configured for output will be updated.<br />The mask parameter provides additional control on the bits in the group to<br />be affected. Setting a bit to 1 in the mask will cause the corresponding<br />bit in the port group to be updated. Clearing a bit in the mask will cause<br />that corresponding bit in the group to stay unaffected. For example,<br />setting a mask value 0xFFFFFFFF will cause all bits in the port group<br />to be updated. Setting a value 0x3 will only cause port group bit 0 and<br />bit 1 to be updated.

For port pins which are not configured for output and have the pull feature<br />enabled, this function will affect pull value \(pull up or pull down\). A bit<br />value of 1 will enable the pull up. A bit value of 0 will enable the pull<br />down.

## Precondition

The PORT\_Initialize\(\) function should have been called.

## Parameters

|Param|Description|
|-----|-----------|
|group|One of the IO groups from the enum PORT\_GROUP.|
|value|Value which has to be written/driven on the I/O lines of the selected port for which mask bits are '1'. Values for the corresponding mask bit '0' will be ignored. Refer to the function description for effect on pins which are not configured for output.|
|mask|A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port group will be written.|

-   1's Will write to corresponding IO pins.

-   0's Will remain unchanged.


## Returns

None.

## Example

```c
// Write binary value 0011 to the pins PC3, PC2, PC1 and PC0 respectively.
PORT_GroupWrite(PORT_GROUP_C, 0x0F, 0xF563D453);

```

## Remarks

None.

