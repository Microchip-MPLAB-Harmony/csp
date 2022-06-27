# I2C\_SLAVE\_ERROR Enum

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-9FF2770C-87B8-47A2-830B-AA9EB23ACFEC.md)

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-84B7C9F3-533A-4A83-9104-9196F8070FF2.md)

## C

```c
/* I2C slave mode */

typedef enum
{
    // No Error
    I2C_SLAVE_ERROR_NONE,
    
    // Bus Collision Error
    I2C_SLAVE_ERROR_BUS_COLLISION,
    
} I2C_SLAVE_ERROR;

```

## Summary

Defines errors associated with I2C in slave mode

## Description

This enum defines errors associated with I2C in slave mode. An error of this type is returned by the I2Cx\_ErrorGet\(\) function

## Remarks

None.

