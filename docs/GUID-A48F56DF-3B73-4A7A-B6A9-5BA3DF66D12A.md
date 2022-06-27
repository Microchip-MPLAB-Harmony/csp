# TC\_TIMER Macros and Typedefs

**Parent topic:**[Basic Timer Counter \(TC\)](GUID-D805E0EA-6923-41A3-A27E-5A159783D12C.md)

## C

```c

#define TC_TIMER_STATUS_NONE        0U
/*  overflow */
#define TC_TIMER_STATUS_OVERFLOW    TC_INTFLAG_OVF_Msk

/* match compare 1 */
#define TC_TIMER_STATUS_MATCH1      TC_INTFLAG_MC1_Msk

#define TC_TIMER_STATUS_MSK         (TC_TIMER_STATUS_OVERFLOW | TC_TIMER_STATUS_MATCH1)

/* Invalid timer status */
#define TC_TIMER_STATUS_INVALID     0xFFFFFFFFU

/* TC_TIMER_STATUS type */
typedef uint32_t TC_TIMER_STATUS;

```

## Summary

Defines macros and typedefs associated with tc timer status

## Description

Provides convenience macros and type definitions for status flags associated with timer mode of TC

