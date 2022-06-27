# ICAP\_CALLBACK Typedef

**Parent topic:**[Input Capture \(ICAP\)](GUID-E126A9DC-A2E6-405E-85E7-9FB676BDEBD2.md)

## C

```c
typedef void (*ICAP_CALLBACK) (uintptr_t context)

```

## Summary

Defines the function pointer data type and function signature for the ICAP callback function.

## Description

This data type defines the function pointer and function signature for the<br />ICAPx callback function. The library will call back the client's function<br />with this signature from the interrupt routine.

