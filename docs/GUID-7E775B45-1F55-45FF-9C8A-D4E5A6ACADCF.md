# SEFCx\_PageBufferCommit Function

**Parent topic:**[Secure Embedded Flash Controller \(SEFC\)](GUID-E586E73A-F607-48C1-A0B8-EC4E231FB77A.md)

## C

```c
bool SEFCx_PageBufferCommit( const uint32_t address) // x - Instance of the SEFC peripheral
```

## Summary

Commits the data present in SEFCx internal latch buffer to flash memory

## Description

Writes data loaded in the SEFCx internal latch buffer to the flash memory.

## Precondition

The SEFCx\_Initialize\(\) function should have been called once.

## Parameters

|Param|Description|
|-----|-----------|
|address|Data Flash address to be modified.|

## Returns

true if the operation was successful, else returns false.

## Example

```c
uint32_t* data; //data - pointer to the buffer to be written to flash memory
uint32_t flashAddr; //flashAddr - variable containing flash address

//populate data and flashAddr

SEFC0_PageBufferWrite((uint32_t*)data, (uint32_t)flashAddr);

//update data here

SEFC0_PageBufferWrite((uint32_t*)data, (uint32_t)flashAddr);

//Commit the final data in the SEFCx internal latch buffer to the flash memory
SEFC0_PageBufferCommit((uint32_t)flashAddr);

//Wait until the SEFCx controller is busy
while (SEFC0_IsBusy());

```

## Remarks

None

