# TWIHS\_SLAVE\_CALLBACK Typedef

**Parent topic:**[Two-wire Interface - TWIHS](GUID-C8012FE8-F7B4-4CE6-84B4-61EAAFAB03B0.md)

## C

```c
/* TWIHS slave in non-blocking/interrupt mode */
typedef bool (*TWIHS_SLAVE_CALLBACK) ( TWIHS_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle );

```

## Summary

Defines the data type and function signature for the TWIHS Slave callback function.

## Description

This data type defines the function signature for the TWIHS Slave callback function. The TWIHS peripheral will call back the client's function with this signature to report TWIHS slave events.

## Precondition

TWIHSx\_Initialize must have been called for the given TWIHS peripheral instance and TWIHSx\_CallbackRegister must have been called to set the function to be called. The callback register function should have been called before any transfer is initiated by the I2C master.

## Parameters

|Param|Description|
|-----|-----------|
|event|Indicates the data transfer event for which the callback function hasbeen called.|
|contextHandle|Allows the caller to provide a context value \(usually a pointerto the callers context for multi-instance clients\).|

## Returns

*bool* - The return value is ignored by the TWI slave PLIB

## Example

```c
void APP_TWIHS_Callback ( TWIHS_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle )
{
    switch(event)
    {
        case TWIHS_SLAVE_TRANSFER_EVENT_ADDR_MATCH:
        // Handle address match event
        break;
        
        case TWIHS_SLAVE_TRANSFER_EVENT_RX_READY:
        
        // Read the received data byte
        rxData = TWIHS1_ReadByte();
        
        break;
        case TWIHS_SLAVE_TRANSFER_EVENT_TX_READY:
        
        // Provide data to TWI master
        TWIHS1_WriteByte(txData);
        
        break;
        
        case TWIHS_SLAVE_TRANSFER_EVENT_TRANSMISSION_COMPLETE:
        // Handle stop bit received event
        break;
    }
}

// Register Callback function which is defined above
TWIHS1_CallbackRegister(APP_TWIHS_Callback, 0);

```

## Remarks

None

