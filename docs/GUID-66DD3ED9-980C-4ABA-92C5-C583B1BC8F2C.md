# TMR\_CALLBACK Typedef

**Parent topic:**[Timer\(TMR\)](GUID-493DD237-5B81-441C-B4FC-53AA6191C224.md)

**Parent topic:**[Timer\(TMR\)](GUID-4FD9BFDE-4887-4C40-B254-C39D2B1DE0F5.md)

## C

```c
typedef void (*TMR_CALLBACK)(uint32_t status, uintptr_t context);

```

## Summary

Defines the function pointer data type and function signature for the TMRx callback function.

## Description

This data type defines the function pointer and function signature for the TMRx callback function. The library will call back the client's function with this signature from the interrupt routine.

