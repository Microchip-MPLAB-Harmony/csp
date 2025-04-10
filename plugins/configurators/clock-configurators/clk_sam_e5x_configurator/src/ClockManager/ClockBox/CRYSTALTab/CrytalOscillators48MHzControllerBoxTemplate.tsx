import {
  CheckBoxDefault,
  InputNumberDefault,
  KeyValueSetRadio,
  useBooleanSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import FrequencyLabelComponent from 'clock-common/lib/Components/LabelComponent/FrequencyLabelComponent';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { removeDuplicates } from 'clock-common/lib/Tools/Tools';

const CrytalOscillators48MHzControllerBoxTemplate = (props: {
  index: string;
  crystalsettingsClassName: string;
  crystalresetClassName: string;
  crystalXoscFreqInputClassName: string;
  crystalEnableClassName: string;
  crystalCFDEnableClassName: string;
  crystalFrequencyClassName: string;
  crystalSettingsSymbolArray: string[];
  originalRadioButtonIdentificationId: string;
  crystalController: ControlInterface[];
  cx: (...classNames: string[]) => string;
  componentId: string;
}) => {
  const crystalOscillatorMode = useKeyValueSetSymbol({
    componentId: props.componentId,
    symbolId: 'XOSC' + props.index + '_OSCILLATOR_MODE'
  });
  const crystalOSC = useBooleanSymbol({
    componentId: props.componentId,
    symbolId: 'CONFIG_CLOCK_XOSC' + props.index + '_ENABLE'
  });

  let symbols: any = props.crystalController.map((e) => e.symbol_id).filter((e) => e !== undefined);
  symbols = symbols.concat(props.crystalSettingsSymbolArray);
  symbols = removeDuplicates(symbols);

  return (
    <div>
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={'CONFIG_CLOCK_XOSC' + props.index + '_FREQUENCY'}
        className={props.cx(props.crystalXoscFreqInputClassName)}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={'CONFIG_CLOCK_XOSC' + props.index + '_ENABLE'}
        className={props.cx(props.crystalEnableClassName)}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={'CONFIG_CLOCK_XOSC' + props.index + '_CFDEN'}
        className={props.cx(props.crystalCFDEnableClassName)}
      />
      {crystalOSC.value === true && (
        <FrequencyLabelComponent
          componentId={props.componentId}
          symbolId={'CONFIG_CLOCK_XOSC' + props.index + '_FREQUENCY'}
          className={props.cx('xosc48MFreq')}
        />
      )}
      <KeyValueSetRadio
        keyValueSetSymbolHook={crystalOscillatorMode}
        classResolver={props.cx}
        classPrefix={'crystal_8_48_OscillatorR'}
      />
      <SettingsDialog
        tooltip={'8-48 MHz Crystal Oscillator' + props.index + ' Configuration'}
        componentId={props.componentId}
        className={props.cx(props.crystalsettingsClassName)}
        symbolArray={props.crystalSettingsSymbolArray}
        dialogWidth='50rem'
        dialogHeight='45rem'
      />
      <ResetSymbolsIcon
        tooltip={'Reset Crystal Oscillator' + props.index + ' symbols to default value'}
        className={props.cx('crystal8_48_oscillators_reset')}
        componentId={props.componentId}
        resetSymbolsArray={symbols}
      />
    </div>
  );
};
export default CrytalOscillators48MHzControllerBoxTemplate;
