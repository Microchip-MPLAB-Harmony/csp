import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import LoadDynamicComponents from 'clock-common/lib/Components/LoadDynamicComponents';
import { useContext, useState } from 'react';
import {
  PluginConfigContext,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
  getAllSymbolsFromJSON,
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import FreqencyLabels from 'clock-common/lib/Components/LabelComponent/FreqencyLabels';
import KeyValueSetRadio from './ClientLib/KeyValueSetRadio';

const SlowClockControllerBox = (props: {
  slowClockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const cmb_Slclk_oscsel = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CLK_TD_OSCSEL'
  });

  const [allJsonSymbols] = useState<string[]>(getAllSymbolsFromJSON(props.slowClockController));
  const [dynamicSymbolInfo] = useState(() => getDynamicSymbolsFromJSON(props.slowClockController));
  const [dynamicLabelSymbolInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.slowClockController)
  );

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        boxInfo={dynamicSymbolInfo}
        cx={props.cx}
      />
      <FreqencyLabels
        componentId={componentId}
        boxInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
      <PlainLabel
        disPlayText={'Use bootloader Clock tree'}
        className={props.cx('useBootloaderLabel')}
      />
      <PlainLabel
        disPlayText={'32K Hz'}
        className={props.cx('lbl_Slclk_SecMod')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={cmb_Slclk_oscsel}
        classPrefix='slowClockR'
        classResolver={props.cx}
      />
      <SettingsDialog
        tooltip='Slow Clock Settings Configuration'
        componentId={componentId}
        className={props.cx('slclk_settings')}
        symbolArray={allJsonSymbols}
        dialogWidth='40rem'
        dialogHeight='20rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset Slow Clock symbols to default value'
        className={props.cx('slclk_reset')}
        componentId={componentId}
        resetSymbolsArray={allJsonSymbols}
      />
    </div>
  );
};

export default SlowClockControllerBox;
