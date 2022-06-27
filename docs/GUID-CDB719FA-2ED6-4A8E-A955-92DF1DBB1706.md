# SUPC\_SetOutputPin Function

**Parent topic:**[Supply Controller \(SUPC\)](GUID-5A020BA6-D697-4D83-94D7-0289AB443AF1.md)

**Parent topic:**[Supply Controller \(SUPC\)](GUID-09165D4A-27D7-4560-B218-E23AC70218F8.md)

**Parent topic:**[Supply Controller \(SUPC\)](GUID-CAEF0560-90E6-45AA-96D0-FAEAF26EDC48.md)

## C

```c
void SUPC_SetOutputPin( SUPC_OUTPIN pin );
```

## Summary

Sets a specific output pin \(OUTx\) to logic HIGH.

## Description

There are two pins controlled by the SUPC. This API helps to drive<br />a logic HIGH on a given OUTx pin.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|pin|Identifies the output pin to be set|

## Returns

None.

## Example

```c
SUPC_SetOutputPin( SUPC_OUTPIN_OUT0 );
```

## Remarks

None.

