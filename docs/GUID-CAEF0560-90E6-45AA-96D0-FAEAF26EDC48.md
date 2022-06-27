# Supply Controller \(SUPC\)

The Supply Controller \(SUPC\) manages the voltage reference, power<br />supply and supply monitoring of the device. It is also able to control<br />two output pins.

The SUPC controls the voltage regulators for the core \(VDDCORE\) and<br />backup \(VDDBU\) domains. It sets the voltage regulators according to the<br />sleep modes, or the user configuration. In active mode, the voltage<br />regulators can be selected on the fly between LDO \(low-dropout\) type<br />regulator or Buck converter.

The SUPC supports connection of a battery backup to the VBAT power pin.<br />It includes functionality that enables automatic power switching<br />between main power and battery backup power. This ensures power to the<br />backup domain when the main battery or power source is unavailable.

The SUPC embeds two Brown-Out Detectors. BOD33 monitors the voltage<br />applied to the device \(VDD or VBAT\) and BOD12 monitors the internal<br />voltage to the core \(VDDCORE\). The BOD33 can monitor the supply voltage<br />continuously \(continuous mode\) or periodically \(sampling mode\), in<br />normal or low power mode.

The SUPC generates also a selectable reference voltage and a voltage<br />dependent on the temperature which can be used by analog modules like<br />the ADC.

**Using The Library**

The Brown-Out Detector \(BOD33\) when enabled, monitors the VDD supply<br />and compares the voltage with the brown-out threshold level.<br />When VDD crosses the brown-out threshold level, the BOD33 can perform<br />one of the following actions,

-   Generate a reset

-   Generates an interrupt

-   Puts the device in battery backup sleep mode


The triggering voltage threshold for the BOD33 and the action can be<br />configured via fuse bits in the NVM User Row. These bits can also be<br />written after disabling BOD33. Brown out interrupt enables user to save<br />critical data to prepare the system for a power-down.

SUPC Peripheral library provides non-Blocking API's and they can be<br />used to perform below functionalities. Settings configured via MHC are<br />written into SUPC registers when initialization function is called.

-   Initialize BOD33, VREF and VREG of the SUPC peripheral.

-   Modify the main voltage regulation selection.

-   Select temperature sensor channel to be used by the ADC peripheral.

-   Set or clear OUTx pins of the SUPC peripheral.


**Callback method**

This example demonstrates how to get callback on brown-out detection to<br />save critical work.

```c
MY_APP_OBJ myAppObj;

void BOD_EventHandler(uintptr_t context)
{
    // The context was set to an application specific object.
    // It is now retrievable easily in the event handler.
    MY_APP_OBJ myAppObj = (MY_APP_OBJ *) context;

    // Brown-out interrupt occurred. Save critical data.
}

int main(void)
{
    /* Register callback function */
    SUPC_BOD33CallbackRegister(BOD_EventHandler, (uintptr_t)&myAppObj);

    while(true)
    {

    }
}
```

**Library Interface**

Supply Controller peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|SUPC\_Initialize|Initializes the SUPC peripheral|
|SUPC\_SelectVoltageRegulator|Selects the main voltage regulator|
|SUPC\_SelectTempSenorChannel|Selects a specific channel of the temperature sensor|
|SUPC\_SetOutputPin|Sets a specific output pin \(OUTx\) to logic HIGH|
|SUPC\_ClearOutputPin|Clears a specific output pin \(OUTx\) to logic LOW|
|SUPC\_BOD33CallbackRegister|Registers the function to be called when a Brown Out Event has occurred|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|SUPC\_OUTPIN|Enum|Identifies the output pins of SUPC peripheral|
|SUPC\_TSSEL|Enum|Identifies the temperature sensor channels of SUPC peripheral|
|SUPC\_VREGSEL|Enum|Identifies the Main Voltage Regulators|
|SUPC\_BOD33\_CALLBACK|Typedef|Defines the data type and function signature for the SUPC peripheral callback function|

-   **[SUPC\_Initialize Function](GUID-D18356A1-3487-41FC-A6AA-5E425483A02C.md)**  

-   **[SUPC\_SelectVoltageRegulator Function](GUID-45EBB2E1-C6FD-4A01-AA8A-5F2680800A65.md)**  

-   **[SUPC\_SelectTempSenorChannel Function](GUID-F1F3CD6F-C0C2-4121-BD46-00CC6E8DBD90.md)**  

-   **[SUPC\_SetOutputPin Function](GUID-CDB719FA-2ED6-4A8E-A955-92DF1DBB1706.md)**  

-   **[SUPC\_ClearOutputPin Function](GUID-8F52D2BD-6421-4FF7-A4FD-D908E4C4F686.md)**  

-   **[SUPC\_BOD33CallbackRegister Function](GUID-BB6D83A3-F3D7-47A2-A151-23EACE5AA25E.md)**  

-   **[SUPC\_OUTPIN Enum](GUID-140606A3-FD67-4ED2-9726-4BBA4755F5D2.md)**  

-   **[SUPC\_TSSEL Enum](GUID-D627CE4B-6A78-45A0-AD4A-AB2FE974630B.md)**  

-   **[SUPC\_VREGSEL Enum](GUID-AC111116-62C6-40E1-956B-4E73EFF5B55B.md)**  

-   **[SUPC\_BOD33\_CALLBACK Typedef](GUID-647FC8A2-346B-44CF-84F7-DE2BA1F6254A.md)**  


**Parent topic:**[SAM D51 E51 E53 E54 Peripheral Libraries](GUID-E33B93DD-6680-477E-AA96-966208DC9A50.md)

