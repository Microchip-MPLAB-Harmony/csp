import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import { useContext, useState } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { getDynamicSymbolsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';

const settingsArray = [
  'CONFIG_CLOCK_DFLL_ENABLE',
  'CONFIG_CLOCK_DFLL_OPMODE',
  'CONFIG_CLOCK_DFLL_ONDEMAND',
  'CONFIG_CLOCK_DFLL_USB',
  'CONFIG_CLOCK_DFLL_WAIT_LOCK',
  'CONFIG_CLOCK_DFLL_QUICK_LOCK',
  'CONFIG_CLOCK_DFLL_CHILL_CYCLE',
  'CONFIG_CLOCK_DFLL_LLAW',
  'CONFIG_CLOCK_DFLL_STABLE',
  'CONFIG_CLOCK_DFLL_STEP',
  'CONFIG_CLOCK_DFLL_MUL'
];

const DFLLControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmb_dfll_Mode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DFLL_OPMODE'
  });
  const checkdfllEnable = useBooleanSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DFLL_ENABLE'
  });

  const mulValue = useIntegerSymbol({ componentId, symbolId: 'CONFIG_CLOCK_DFLL_MUL' });

  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.clockController));

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      {checkdfllEnable.value === true && (
        <FrequencyLabelComponent
          componentId={componentId}
          redColorForZeroFrequency={true}
          symbolId={'DFLL_CLOCK_FREQ'}
          class={props.cx('dfllFreq')}
        />
      )}

      <PlainLabel
        disPlayText={'' + mulValue.value}
        className={props.cx('dfllMulLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmb_dfll_Mode}
        classPrefix='dfllRefClockR'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('dflll_settings')}
        symbolArray={settingsArray}
        dialogWidth='50rem'
        dialogHeight='47rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Clock symbols to default value'
        className={props.cx('dfll_reset')}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default DFLLControllerBox;
