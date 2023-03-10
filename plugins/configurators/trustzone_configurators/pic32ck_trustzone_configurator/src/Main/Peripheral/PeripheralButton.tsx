import {
  AddSymbolListener,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { convertToBoolean } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolUtils';
import { Button } from 'primereact/button';
import { useEffect, useState } from 'react';
import {
  component_id,
  nonSecureColor,
  secureColor,
} from '../MainView/TrustZoneMainView';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { ConfigSymbolEvent } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';

const PeripheralButton = (props: {
  symbolId: string;
  nonSecureAppendText: string;
  secureText: string;
  nonSecureText: string;
  ButtonClicked: (buttonText: any) => boolean;
}) => {
  useEffect(() => {
    addListener(props.symbolId + props.nonSecureAppendText);
  }, []);

  function addListener(symbolId: string) {
    AddSymbolListener(symbolId);
    globalSymbolSStateData.set(symbolId, {
      symbolChanged: symbolChanged,
    });
  }

  const symbolChanged = (symbol: ConfigSymbolEvent) => {
    let bNonSecure = convertToBoolean(symbol.value);
    if (bNonSecure) {
      setColor(nonSecureColor);
    } else {
      setColor(secureColor);
    }
  };

  function updateButtonState(butttonText: any) {
    let updateColor = props.ButtonClicked(butttonText);
    if (updateColor) {
      if (color === nonSecureColor) {
        setColor(secureColor);
      } else {
        setColor(nonSecureColor);
      }
    }
  }
  let symbolIdStatus = props.symbolId + props.nonSecureAppendText;
  let bNonSecure = convertToBoolean(
    GetSymbolValue(component_id, symbolIdStatus)
  );
  let ttip = props.secureText;
  const [color, setColor] = useState(bNonSecure ? nonSecureColor : secureColor);
  if (bNonSecure) {
    ttip = props.nonSecureText;
  }
  return (
    <div className="row p-3">
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
          backgroundColor: color,
          color: 'white',
        }}
        onClick={() => updateButtonState(props.symbolId)}
      />
    </div>
  );
};
export default PeripheralButton;
