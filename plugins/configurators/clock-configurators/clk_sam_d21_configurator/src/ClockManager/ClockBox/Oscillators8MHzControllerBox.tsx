import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import { removeDuplicates } from 'clock-common/lib/Tools/Tools';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import {
  getDynamicSymbolsFromJSON,
  getDynamicLabelsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';

let group1RadioSymbolId = 'XOSC_OSCILLATOR_MODE';
let internal48MhzOscillatorSettingsSymbolArray = [
  'CONFIG_CLOCK_OSC8M_ENABLE',
  'CONFIG_CLOCK_OSC8M_ONDEMAND',
  'CONFIG_CLOCK_OSC8M_RUNSTDY',
  'CONFIG_CLOCK_OSC8M_FREQ',
  'CONFIG_CLOCK_OSC8M_PRES'
];
let crsytamOscillatorSymbolArray = [
  'CONFIG_CLOCK_XOSC_ENABLE',
  'XOSC_AMPGC',
  'XOSC_OSCILLATOR_MODE',
  'CONFIG_CLOCK_XOSC_FREQUENCY',
  'CONFIG_CLOCK_XOSC_ONDEMAND',
  'CONFIG_CLOCK_XOSC_STARTUP',
  'CONFIG_CLOCK_XOSC_RUNSTDBY'
];
const Oscillators8MHzControllerBox = (props: {
  oscillatorData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const oscillatorMode = useKeyValueSetSymbol({
    componentId,
    symbolId: group1RadioSymbolId
  });
  const osc8mPres = useKeyValueSetSymbol({ componentId, symbolId: 'CONFIG_CLOCK_OSC8M_PRES' });

  let symbols: any = props.oscillatorData.map((e) => e.symbol_id).filter((e) => e !== undefined);
  symbols = symbols.concat(
    internal48MhzOscillatorSettingsSymbolArray,
    crsytamOscillatorSymbolArray
  );
  symbols = removeDuplicates(symbols);

  const [dynamicSymbolsInfo] = useState(() => getDynamicSymbolsFromJSON(props.oscillatorData));
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.oscillatorData));

  // const AddFrencyLabels = () => {
  //   function customLabelConfigOnSymbolChange(symbolId: any, currentSymbolValue: any) {
  //     let labelStyle = { color: currentSymbolValue === 0 ? 'red' : 'black' };
  //     let labelVisibleStatus = true;
  //     if (symbolId === 'OSC48M_CLOCK_FREQ') {
  //       labelVisibleStatus = convertToBoolean(
  //         GetSymbolValue(component_id, 'CONFIG_CLOCK_OSC48M_ENABLE')
  //       )
  //         ? true
  //         : false;
  //     } else if (symbolId === 'XOSC_FREQ') {
  //       labelVisibleStatus = convertToBoolean(
  //         GetSymbolValue(component_id, 'CONFIG_CLOCK_XOSC_ENABLE')
  //       )
  //         ? true
  //         : false;
  //     }
  //     ChangeCustomLabelComponentState(
  //       symbolId,
  //       currentSymbolValue,
  //       labelStyle,
  //       labelVisibleStatus,
  //       null
  //     );
  //   }
  //   return (
  //     <div>
  //       <FreqencyLabels
  //         componentId={component_id}
  //         boxInfo={props.oscillatorData}
  //         ChangeCustomLabelComponentState={customLabelConfigOnSymbolChange}
  //       />
  //     </div>
  //   );
  // };
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
        redColorForZeroFrequency={true}
        cx={props.cx}
      />

      <PlainLabel
        disPlayText={osc8mPres.selectedOption.replace('FREQ/', '')}
        className={props.cx('internalOSC48DivLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={oscillatorMode}
        classResolver={props.cx}
        classPrefix={'externalOSCModeR'}
      />

      <SettingsDialog
        tooltip='48 MHz Internal Oscillator Configuration'
        componentId={componentId}
        className={props.cx('Internal8Mhz_oscillators_settings')}
        symbolArray={internal48MhzOscillatorSettingsSymbolArray}
        dialogWidth='50rem'
        dialogHeight='30rem'
      />
      <SettingsDialog
        tooltip='Crystal Oscillator Configuration'
        componentId={componentId}
        className={props.cx('crystal_oscillatoor_Settings')}
        symbolArray={crsytamOscillatorSymbolArray}
        dialogWidth='50rem'
        dialogHeight='35rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset 32 Khz Oscillator symbols to default value'
        className={props.cx('oscillators_reset')}
        componentId={componentId}
        resetSymbolsArray={symbols}
      />
    </div>
  );
};
export default Oscillators8MHzControllerBox;
