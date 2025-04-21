import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext } from 'react';
import {
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useKeyValueSetSymbol,
  useIntegerSymbol,
  InputNumber,
  CheckBox
} from '@mplab_harmony/harmony-plugin-client-lib';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';

const settingsArray = [
  "CONFIG_CLOCK_XOSC_ENABLE",
  "CONFIG_CLOCK_XOSC_AGC_ENABLE",
  "CONFIG_CLOCK_XOSC_SWBEN",
  "XOSC_OSCILLATOR_MODE",                        
  "CONFIG_CLOCK_XOSC_FREQUENCY",
  "CONFIG_CLOCK_XOSC_ONDEMAND",
  "CONFIG_CLOCK_XOSC_STARTUP",
  "CONFIG_CLOCK_XOSC_CFDEN",
  "CONFIG_CLOCK_XOSC_CFDPRESC",
  "CONFIG_CLOCK_XOSC_USBHSDIV"
];

const CrystalOscillator = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const xoscFrequency = useIntegerSymbol({componentId,symbolId:'CONFIG_CLOCK_XOSC_FREQUENCY'})
  const externalOSCMode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'XOSC_OSCILLATOR_MODE'
  });
  const crystalOSC = useBooleanSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_XOSC_ENABLE'
  });



  return (
    <div>
      <InputNumber integerSymbolHook={xoscFrequency} className={props.cx('xoscFrequency')}/>
      <CheckBox booleanSymbolHook={crystalOSC} className={props.cx('crystalOSC')}/>
      {crystalOSC.value === true && (
        <FrequencyLabelComponent
          componentId={componentId}
          redColorForZeroFrequency={true}
          symbolId={'XOSC_FREQ'}
          className={props.cx('xoscFreq')}
        />
      )}
      <KeyValueSetRadio
        keyValueSetSymbolHook={externalOSCMode}
        classPrefix='externalOSCMode'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Settings Configuration'
        componentId={componentId}
        className={props.cx('crystalOscSetting')}
        symbolArray={settingsArray}
        dialogWidth='50rem'
        dialogHeight='47rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset clock symbols to default value'
        className={props.cx('crystalOscReset')}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default CrystalOscillator;
