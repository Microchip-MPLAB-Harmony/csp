import { Button } from 'primereact/button';
import { useEffect, useState } from 'react';
import { nonSecureColor, secureColor } from '../MainView/TrustZoneMainView';
import { useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';

const PeripheralButton = (props: {
  componentId: string;
  symbolId: string;
  nonSecureAppendText: string;
  secureText: string;
  nonSecureText: string;
  ButtonClicked: (buttonText: string, symbolValue: boolean, readOnlyState: boolean) => boolean;
}) => {
  const bNonSecureSymbol = useBooleanSymbol({
    componentId: props.componentId,
    symbolId: props.symbolId + props.nonSecureAppendText
  });
  function updateButtonState(butttonText: any) {
    let updateColor = props.ButtonClicked(
      butttonText,
      bNonSecureSymbol.value,
      bNonSecureSymbol.readOnly
    );
    if (updateColor) {
      bNonSecureSymbol.writeValue(!bNonSecureSymbol.value);
    }
  }
  let ttip = props.secureText;
  if (bNonSecureSymbol.value) {
    ttip = props.nonSecureText;
  }
  return (
    <div className='row p-3'>
      <Button
        label={props.symbolId}
        tooltip={ttip}
        tooltipOptions={{ position: 'bottom' }}
        style={{
          width: '120px',
          height: '40px',
          fontSize: '14px',
          fontWeight: 'bold',
          borderWidth: '0px',
          backgroundColor: bNonSecureSymbol.value ? nonSecureColor : secureColor,
          color: 'white'
        }}
        onClick={() => updateButtonState(props.symbolId)}
      />
    </div>
  );
};
export default PeripheralButton;
