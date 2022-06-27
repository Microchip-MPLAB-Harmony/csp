# FLEXCOM\_TWI\_SLAVE\_STATUS\_FLAG Enum

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c

/* TWI slave with interrupt disabled */

typedef enum
{
	/* Slave Access flag */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_SVACC     = FLEX_TWI_SR_SVACC_Msk,
	
	/* End of slave access flag */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_EOSACC    = FLEX_TWI_SR_EOSACC_Msk,
	
	/* TWI transfer direction is read */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_SVREAD    = FLEX_TWI_SR_SVREAD_Msk,
	
	/* Transmitter is ready */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_TXRDY     = FLEX_TWI_SR_TXRDY_Msk,
	
	/* Receiver has an unread character */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_RXRDY     = FLEX_TWI_SR_RXRDY_Msk,
	
	/* NACK received from master */
	FLEXCOM_TWI_SLAVE_STATUS_FLAG_NACK   	= FLEX_TWI_SR_NACK_Msk,
	
	/* Stop condtion or start condition with other slave address detected */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_TXCOMP    = FLEX_TWI_SR_TXCOMP_Msk,
}FLEXCOM_TWI_SLAVE_STATUS_FLAG;

```

## Summary

This enum defines the list of possible TWI slave events

## Description

This enum defines the list of possible TWI slave events returned by the FLEXCOMx\_TWI\_StatusGet API

## Remarks

None

