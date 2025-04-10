import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import { removeDuplicates } from 'clock-common/lib/Tools/Tools';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import {
  InputNumber,
  KeyValueSetRadio,
  PluginConfigContext,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import {
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';

let dfllSettingsSymbolArray = [
  'CONFIG_CLOCK_DFLL_ENABLE',
  'CONFIG_CLOCK_DFLL_OPMODE',
  'CONFIG_CLOCK_DFLL_ONDEMAND',
  'CONFIG_CLOCK_DFLL_RUNSTDY',
  'CONFIG_CLOCK_DFLL_USB',
  'CONFIG_CLOCK_DFLL_WAIT_LOCK',
  'CONFIG_CLOCK_DFLL_BYPASS_COARSE',
  'CONFIG_CLOCK_DFLL_QUICK_LOCK',
  'CONFIG_CLOCK_DFLL_CHILL_CYCLE',
  'CONFIG_CLOCK_DFLL_LLAW',
  'CONFIG_CLOCK_DFLL_STABLE',
  'CONFIG_CLOCK_DFLL_COARSE',
  'CONFIG_CLOCK_DFLL_FINE',
  'CONFIG_CLOCK_DFLL_MUL'
];

const DFLLController = (props: {
  dfllControllerData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const dfllOPMode = useKeyValueSetSymbol({ componentId, symbolId: 'CONFIG_CLOCK_DFLL_OPMODE' });
  const CONFIG_CLOCK_DFLL_MUL = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DFLL_MUL'
  });

  let symbols: any = props.dfllControllerData
    .map((e) => e.symbol_id)
    .filter((e) => e !== undefined);
  symbols = symbols.concat(dfllSettingsSymbolArray);
  symbols = removeDuplicates(symbols);

  const [dynamicSymbolsInfo] = useState(() => getDynamicSymbolsFromJSON(props.dfllControllerData));
  const [dynamicLabelSymbolInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.dfllControllerData)
  );

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
      <InputNumber
        integerSymbolHook={CONFIG_CLOCK_DFLL_MUL}
        disabled={dfllOPMode.value === 0}
        className={props.cx('e5x_dfllMultiplier')}
        hidden={false}
      />
      <PlainLabel
        disPlayText={CONFIG_CLOCK_DFLL_MUL.value + ''}
        className={props.cx('e5x_dfllMulLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={dfllOPMode}
        classResolver={props.cx}
        classPrefix={'e5x_dfllRefClockRadio'}
      />
      <SettingsDialog
        tooltip='DFLL Configuration'
        componentId={componentId}
        className={props.cx('e5x_dfllSettings')}
        symbolArray={dfllSettingsSymbolArray}
        dialogWidth='55rem'
        dialogHeight='55rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset DFLL symbols to default value'
        className={props.cx('e5x_dfllReset')}
        componentId={componentId}
        resetSymbolsArray={symbols}
      />
    </div>
  );
};
export default DFLLController;
