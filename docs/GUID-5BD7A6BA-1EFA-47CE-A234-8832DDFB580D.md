# MEM2MEM\_TRANSFER\_EVENT Enum

**Parent topic:**[Memory to Memory \(MEM2MEM\)](GUID-692A056B-1150-4194-963B-E39865A3B3C3.md)

## C

```c
typedef enum
{
    /* Data was transferred successfully. */
    MEM2MEM_TRANSFER_EVENT_COMPLETE,
    
    /* Error while processing the request */
    MEM2MEM_TRANSFER_EVENT_ERROR
    
} MEM2MEM_TRANSFER_EVENT;

```

## Summary

Enumeration of possible MEM2MEM transfer events.

## Description

This data type provides an enumeration of all possible MEM2MEM transfer events.<br />A data value of this type is returned in the MEM2MEM callback function and<br />indicates if the completed transfer was successful.

## Remarks

None.

