# SDMMCx\_BlockCountSet Function

**Parent topic:**[Secure Digital MultiMedia Card Controller \(SDMMC\)](GUID-670F0003-D51D-457F-BF15-845C30D30C12.md)

**Parent topic:**[Secure Digital MultiMedia Card Controller \(SDMMC\)](GUID-9384AD3C-4E33-479E-B7BB-005772421CB2.md)

## C

```c

/* x = SDMMC instance number */

void SDMMCx_BlockCountSet( uint16_t numBlocks )
```

## Summary

Sets the number of blocks to transfer.

## Description

Sets the number of blocks to transfer for a multi-block transfer. For example,<br />the block count must be set to the appropriate value before issuing the<br />multi-block read \(CMD 18\) or write \(CMD 25\) commands. For single blcok read<br />\(CMD 17\) or write \(CMD24\) commands, the block count must be set to 1.

## Precondition

SDMMCx\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|numBlocks|Number of blocks to transfer|

## Returns

None.

## Example

```c
SDMMC1_BlockCountSet(1);
```

## Remarks

None.

