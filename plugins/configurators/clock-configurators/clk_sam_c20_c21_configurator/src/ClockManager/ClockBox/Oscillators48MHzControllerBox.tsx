import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import { removeDuplicates } from 'clock-common/lib/Tools/Tools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';

let internal48MhzOscillatorSettingsSymbolArray = [
  'CONFIG_CLOCK_OSC48M_ENABLE',
  'CONFIG_CLOCK_OSC48M_ONDEMAND',
  'CONFIG_CLOCK_OSC48M_RUNSTDY',
  'CONFIG_CLOCK_OSC48M_DIV'
];
let crsytamOscillatorSymbolArray = [
  'CONFIG_CLOCK_XOSC_ENABLE',
  'XOSC_AMPGC',
  'XOSC_OSCILLATOR_MODE',
  'CONFIG_CLOCK_XOSC_FREQUENCY',
  'CONFIG_CLOCK_XOSC_ONDEMAND',
  'CONFIG_CLOCK_XOSC_STARTUP',
  'CONFIG_CLOCK_XOSC_RUNSTDBY',
  'CONFIG_CLOCK_XOSC_CFDEN'
];
const OscillatorsControllerBox = (props: {
  oscillatorData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const oscillatorMode = useKeyValueSetSymbol({ componentId, symbolId: 'XOSC_OSCILLATOR_MODE' });
  const oscillatorDiv = useKeyValueSetSymbol({ componentId, symbolId: 'CONFIG_CLOCK_OSC48M_DIV' });
  let symbols: any = props.oscillatorData.map((e) => e.symbol_id).filter((e) => e !== undefined);
  symbols = symbols.concat(
    internal48MhzOscillatorSettingsSymbolArray,
    crsytamOscillatorSymbolArray
  );
  symbols = removeDuplicates(symbols);

  // const AddFrencyLabels = () => {
  //   //   function customLabelConfigOnSymbolChange(symbolId: any, currentSymbolValue: any) {
  //   //     let labelStyle = { color: currentSymbolValue === 0 ? 'red' : 'black' };
  //   //     let labelVisibleStatus = true;
  //   //     if (symbolId === 'OSC48M_CLOCK_FREQ') {
  //   //       labelVisibleStatus = convertToBoolean(
  //   //         GetSymbolValue(component_id, 'CONFIG_CLOCK_OSC48M_ENABLE')
  //   //       )
  //   //         ? true
  //   //         : false;
  //   //     } else if (symbolId === 'XOSC_FREQ') {
  //   //       labelVisibleStatus = convertToBoolean(
  //   //         GetSymbolValue(component_id, 'CONFIG_CLOCK_XOSC_ENABLE')
  //   //       )
  //   //         ? true
  //   //         : false;
  //   //     }
  //   //     ChangeCustomLabelComponentState(
  //   //       symbolId,
  //   //       currentSymbolValue,
  //   //       labelStyle,
  //   //       labelVisibleStatus,
  //   //       null
  //   //     );
  //   //   }
  //   //   return (
  //   //     <div>
  //   //       <FreqencyLabels
  //   //         componentId={component_id}
  //   //         boxInfo={props.oscillatorData}
  //   //         ChangeCustomLabelComponentState={customLabelConfigOnSymbolChange}
  //   //       />
  //   //     </div>
  //   //   );
  // };

  const [dynamicSymbolsInfo] = useState(() => getDynamicSymbolsFromJSON(props.oscillatorData));
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.oscillatorData));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolsInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={oscillatorMode}
        classResolver={props.cx}
        classPrefix={'crystalOscillatorR'}
      />
      <PlainLabel
        disPlayText={Number(oscillatorDiv.value + 1).toString()}
        className={props.cx('internalOSC48DivLabel')}
      />
      <SettingsDialog
        tooltip='48 MHz Internal Oscillator Configuration'
        componentId={componentId}
        className={props.cx('internalOsc48Settings')}
        symbolArray={internal48MhzOscillatorSettingsSymbolArray}
        dialogWidth='50rem'
        dialogHeight='30rem'
      />
      <SettingsDialog
        tooltip='Crystal Oscillator Configuration'
        componentId={componentId}
        className={props.cx('xosc_settings')}
        symbolArray={crsytamOscillatorSymbolArray}
        dialogWidth='50rem'
        dialogHeight='40rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Oscillator symbols to default value'
        className={props.cx('oscillatorsControllerReset')}
        componentId={componentId}
        resetSymbolsArray={symbols}
      />
    </div>
  );
};
export default OscillatorsControllerBox;
