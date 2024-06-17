import {
  AddSymbolListener,
  GetSymbolArray,
  GetSymbolValue,
  UpdateSymbolValue
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { RadioButton } from 'primereact/radiobutton';
import { useEffect, useState } from 'react';
import ControlInterface from '../Tools/ControlInterface';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { ConfigSymbolEvent } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import { StateLabel } from '@mplab_harmony/harmony-plugin-ui';

let onChangeData: Map<String, any>;

const RadioButtonGroup = (props: {
  componentId: string;
  radioButtonSymbolId: string;
  originalRadioButtonIdentificationId?: string;
  boxInfo: ControlInterface[];
  symbolListeners?: any;
  onChange?: (onChangeData: Map<String, any>) => void;
}) => {
  useEffect(() => {
    if (props.onChange !== undefined) {
      onChangeData = new Map<String, any>();
      onChangeData.set('symbolId', props.radioButtonSymbolId);
    }
    addListener(props.radioButtonSymbolId);
  }, []);

  let radioButtonIdentifactionId = props.originalRadioButtonIdentificationId
    ? props.originalRadioButtonIdentificationId
    : props.radioButtonSymbolId;

  let radioNamesInfo = props.boxInfo.filter(
    (e) => e.type === 'radio_name' && e.symbol_id === radioButtonIdentifactionId
  );

  let radioControlInfo = props.boxInfo.filter(
    (e) => e.type === 'radio' && e.symbol_id === radioButtonIdentifactionId
  );

  let symbolArray = GetSymbolArray(props.componentId, props.radioButtonSymbolId);
  const [selectedValue, setselectedValue] = useState(
    GetSymbolValue(props.componentId, props.radioButtonSymbolId)
  );

  function addListener(symbolId: string) {
    AddSymbolListener(symbolId);
    globalSymbolSStateData.set(symbolId, {
      symbolChanged: symbolChanged
    });
  }

  const symbolChanged = (symbol: ConfigSymbolEvent) => {
    setselectedValue(symbol.value);
  };

  function radioButtonChanged(newValue: string) {
    UpdateSymbolValue(props.componentId, props.radioButtonSymbolId, newValue);
    setselectedValue(newValue);
    if (props.onChange !== undefined) {
      onChangeData.set('symbolValue', newValue);
      props.onChange(onChangeData);
    }
  }
  return (
    <div>
      {radioNamesInfo.map((id, i) => {
        return (
          <div key={id.id}>
            {symbolArray[i] !== undefined && (
              <StateLabel
                labelId={id.id}
                labelStyle={{ fontWeight: selectedValue === symbolArray[i] ? 'bold' : 'normal' }}
                labelDisplayText={symbolArray[i]}
                className={id.class[0]}
              />
            )}
          </div>
        );
      })}
      {}
      {radioControlInfo.map((id, i) => {
        return (
          <div key={id.id}>
            {symbolArray[i] !== undefined && (
              <RadioButton
                inputId={id.id}
                value={symbolArray[i]}
                className={id.class[0]}
                tooltip={symbolArray[i]}
                checked={selectedValue === symbolArray[i]}
                onChange={(e) => {
                  radioButtonChanged(e.value);
                }}
              />
            )}
          </div>
        );
      })}
    </div>
  );
};
export default RadioButtonGroup;
