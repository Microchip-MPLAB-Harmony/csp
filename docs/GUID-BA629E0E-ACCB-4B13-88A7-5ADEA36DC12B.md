# TC\_COMPARE Macros and Typedefs

**Parent topic:**[Basic Timer Counter \(TC\)](GUID-D805E0EA-6923-41A3-A27E-5A159783D12C.md)

## C

```c

#define TC_COMPARE_STATUS_NONE          0U
/*  overflow */
#define TC_COMPARE_STATUS_OVERFLOW      TC_INTFLAG_OVF_Msk
/* match compare 0 */
#define TC_COMPARE_STATUS_MATCH0        TC_INTFLAG_MC0_Msk
/* match compare 1 */
#define TC_COMPARE_STATUS_MATCH1        TC_INTFLAG_MC1_Msk

#define TC_COMPARE_STATUS_MSK           (TC_COMPARE_STATUS_OVERFLOW | TC_COMPARE_STATUS_MATCH0 | TC_COMPARE_STATUS_MATCH1)

/* Invalid capture status */
#define TC_COMPARE_STATUS_INVALID       0xFFFFFFFFU

/* TC_COMPARE_STATUS type */
typedef uint32_t TC_COMPARE_STATUS;

```

## Summary

Defines macros and typedefs associated with tc compare status

## Description

Provides convenience macros and type definitions for status flags associated with compare mode of TC

