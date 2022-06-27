# SERCOM\_I2C\_SLAVE\_ACK\_STATUS Enum

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c

/* I2C slave mode */

typedef enum
{
    /* Received ACK from I2C master for the last byte sent */
    SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_ACK = 0,
    
    /* Received NAK from I2C master for the last byte sent */
    SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_NAK,
}SERCOM_I2C_SLAVE_ACK_STATUS;

```

## Summary

Defines the enum for the I2C slave acknowledgement.

## Description

Defines the enum for the I2C slave acknowledgement. Enum of this type is returned by the SERCOMx\_I2C\_LastByteAckStatusGet\(\) function.

## Remarks

None.

